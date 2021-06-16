import tqdm

from clecode.configs import cfg
import numpy as np
import json
import pandas as pd
import random
import io
import copy
import glob
import datetime
import os

from clecode.script.create_md_slugs import SeriesMd
from clecode.script.get_problem_py import OneSeriesPy

from bs4 import BeautifulSoup

from clecode.script.get_problem_detail import get_problem_detail
from clecode.script.get_problems import get_problems


def json_load(f=None):
    data = None
    if isinstance(f, str):
        with open(f, "r", encoding="utf-8") as jf:
            data = json.load(jf)
    elif isinstance(f, io.TextIOWrapper):
        data = json.load(f)
    elif isinstance(f, dict):
        data = data

    return data


def json_dump(data, f=None):
    if f is None:
        return json.dumps(data, indent=4)
    if isinstance(f, str):
        with open(f, "w", encoding="utf-8") as jf:
            json.dump(data, jf, indent=4)
    elif isinstance(f, io.TextIOWrapper):
        json.dump(data, f)
    else:
        return False
    return True


columns = [
    'status',
    'difficulty',
    'paid_only',
    'is_favor',
    'frequency',
    'progress',
    'question_id',
    'question__title',
    'question__title_slug',
    'question__hide',
    'total_acs',
    'total_submitted',
    'total_column_articles',
    'frontend_question_id',
    'is_new_question',
    "content",
    "translatedTitle",
    "translatedContent",
    "topicTags",
    "codeSnippets_python3",
]


def update_pair(columns, pair: dict):
    pair.update(pair.copy().pop("stat"))
    columns.update(pair)
    return columns


def update_detail(columns: dict, detail: dict):
    for det in [
        "content",
        "translatedTitle",
        "translatedContent",
        "topicTags",
        "codeSnippets_python3",
    ]:
        if det == "codeSnippets_python3":
            code = ""
            for c in detail["codeSnippets"]:
                if c["lang"] == "Python3":
                    code = c["code"]
            columns[det] = code
        elif det == "topicTags":
            tags = []
            for t in detail[det]:
                tags.append(t["slug"])
            columns[det] = tags

        elif det == "translatedContent" or det == "content":

            content = ""
            if detail[det]:
                content += BeautifulSoup(detail[det], "lxml").getText()
            columns[det] = "" if content is None else content

        else:
            value = detail.get(det, "")
            columns.update({det: "" if value is None else value})

    return columns


class RobotClecode(object):
    def __init__(self, is_online=False):
        self.is_online = is_online

        self.all_df = None

        self.init_robot()

    def init_robot(self):

        if self.is_online:
            self.load_df(is_online=True)
            self.dump_df()
            pass

        else:
            self.load_df()

    @staticmethod
    def get_basename_by_question_id(question_id, ext=".py"):
        return f"L{question_id:08}{ext}"

    @staticmethod
    def get_problems(*args, **kws):
        return get_problems(*args, **kws)

    @staticmethod
    def get_problem_detail(slug, *args, **kws):
        """

        :param slug:
        :param args:
        :param kws:
        :return: session, detail
        """
        return get_problem_detail(slug, *args, **kws)

    def load_df(self, path=None, is_online=False):
        path = cfg.PATH_ALL_CSV if path is None else path
        if is_online:
            data = RobotClecode.get_problems()
            session = None
            slug = ""
            for pair in tqdm.tqdm(data["stat_status_pairs"][:], desc=r"deal with paris: ", postfix=f"{slug}"):
                cols = dict(zip(columns.copy(), [""] * len(columns)))
                cols = update_pair(cols, pair)
                slug = pair["stat"]["question__title_slug"]
                session, detail = RobotClecode.get_problem_detail(slug, session=session,
                                                                  time_delay=random.random() * 0.75)
                cols = update_detail(cols, detail)
                if self.all_df is None:
                    self.all_df = pd.DataFrame(columns=cols.keys())
                self.all_df = self.all_df.append(cols, ignore_index=True)
        else:
            self.all_df = pd.read_csv(path)

    def dump_df(self, path=None):
        path = cfg.PATH_ALL_CSV if path is None else path
        self.all_df.to_csv(path)
        pass

    def create_py_base_slug(self, slug, f=None):

        rows = self.all_df.loc[self.all_df.question__title_slug == slug]
        assert len(rows) == 1
        row = rows.iloc[0]
        one = OneSeriesPy(row)
        return one.dump(f)

    def create_py_by_question_id(self, id, f=None):
        """
        demo:
        # >>> robot = RobotClecode()
        # >>> robot.create_py_by_question_id(id=0, f="L0.py")
        :param id:
        :param f:
        :return:
        """
        if isinstance(f, str):
            assert not glob.glob(os.path.join(cfg.PATH_CTASKS, f"**/{os.path.basename(f)}"), recursive=True)
        rows = self.all_df.loc[self.all_df.question_id == int(id)]
        assert len(rows) == 1
        row = rows.iloc[0]
        one = OneSeriesPy(row)
        return one.dump(f)

    def create_md_base_slugs(self, slugs, f=None):
        slugs_df = list()
        for slug in slugs:
            rows = self.all_df.loc[self.all_df.question__title_slug == slug]
            assert len(rows) == 1
            row = rows.iloc[0]
            slugs_df.append(row)
        one = SeriesMd(slugs_df)
        one.dump(f)

    @staticmethod
    def add_new_py(timedelta=1):
        robot = RobotClecode()
        df = robot.all_df.sort_values("frequency", ascending=False)

        timeday = datetime.datetime.today() + datetime.timedelta(days=timedelta)
        path_dir = os.path.join(
            cfg.PATH_CTASKS,
            "year_" + timeday.strftime("%Y"),
            "month_" + timeday.strftime("%m"),
            "day_" + timeday.strftime("%Y%m%d"),
        )
        os.makedirs(path_dir, exist_ok=True, )
        if not os.path.exists(os.path.join(path_dir, "__init__.py")):
            with open(os.path.join(path_dir, "__init__.py"), "w") as f:
                f.write("\n")

        has_exists_basename_list = glob.glob(os.path.join(cfg.PATH_CTASKS, "**/*.py"), recursive=True)
        has_exists_basename_list = [os.path.basename(path) for path in has_exists_basename_list]

        for i in range(len(df)):
            new_basename = RobotClecode.get_basename_by_question_id(df.iloc[i].question_id)
            if new_basename in has_exists_basename_list:
                continue
            one = OneSeriesPy(df.iloc[i])
            new_path = os.path.join(path_dir, new_basename)
            one.dump(f=os.path.join(new_path))
            print(f"You just added a file: {new_path}")
            break


if __name__ == '__main__':
    RobotClecode.add_new_py()
    RobotClecode.add_new_py()
    RobotClecode.add_new_py()

if __name__ == '__main__123':
    robot = RobotClecode()
    # robot.create_md_base_slugs(["two-sum", "add-two-numbers"])
    robot.create_md_base_slugs(robot.all_df["question__title_slug"], "a.md")

if __name__ == '__main__12':
    robot = RobotClecode()
    robot.create_py_base_slug("two-sum", "a.py")

if __name__ == '__main__123':
    print(cfg.PATH_ALL_CSV)

    c = RobotClecode(is_online=True)
    # c.load_df(is_online=True)
    # c.dump_df()
    print(c.all_df)
