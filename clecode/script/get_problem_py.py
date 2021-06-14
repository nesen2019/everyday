import ast
import os
import json
import numpy as np
import pandas as pd
from pandas.core.series import Series
import pickle
from io import TextIOWrapper

from bs4 import BeautifulSoup
from markdown import markdown

class OneSeriesPy(object):
    def __init__(self, ds):
        """
        status                                                                  ac
        difficulty                                                          Medium
        paid_only                                                            False
        is_favor                                                             False
        frequency                                                          4.90788
        progress                                                           97.9972
        question_id                                                              5
        question__title                              Longest Palindromic Substring
        question__title_slug                         longest-palindromic-substring
        question__hide                                                       False
        total_acs                                                           490192
        total_submitted                                                    1474632
        total_column_articles                                                 2567
        frontend_question_id                                                     5
        is_new_question                                                      False
        content                  <p>Given a string <code>s</code>, return&nbsp;...
        translatedTitle                                                     最长回文子串
        translatedContent        <p>给你一个字符串 <code>s</code>，找到 <code>s</code> 中最...
        topicTags                                    [string, dynamic-programming]
        codeSnippets_python3     class Solution:\n    def longestPalindrome(sel...
        Name: 1982, dtype: object
        """
        # with open(r"D:/Prog/GithubProject/leetcode2021-dev/lecode0607/lecode0607/scripts/ds.pkl", "rb") as f:
        #     d2 = pickle.load(f)
        self.ds = ds
        self.data_py = ""
        self.data_py += "\n\n".join([
            self.add_doc(),
            self.add_import(),
            self.add_ctest(),
            self.add_code_snippet_python(),
            self.add_main_content(),
        ])
    def dump(self, f=None):
        if f is None:
            return self.data_py
        elif isinstance(f, str):
            with open(f, "w", encoding="utf8") as fw:
                fw.write(self.data_py)
        elif isinstance(f, TextIOWrapper):
            f.write(self.data_py)




    def add_doc(self):
        description = self.ds.translatedContent
        if not description:
            st = f"'''\n"
            st += "'''"
            return st

        snip_python3 = self.ds.codeSnippets_python3

        st = f"'''\n"
        st += f'{self.ds.frontend_question_id}.{self.ds.question__title}\n'
        st += f'{self.ds.frontend_question_id}.{self.ds.translatedTitle}\n'
        st += f"\nhttps://leetcode-cn.com/problems/\n"
        st += f"{self.ds.question__title_slug}\n\n"
        st += f"{description}\n"
        st += f"{snip_python3}\n"
        st += "'''"
        return st

    def add_import(self):
        code_snippet = self.ds.codeSnippets_python3
        if not code_snippet:
            return ""
        if not isinstance(code_snippet, str):
            code_snippet = ""
        st = ""
        if "List" in code_snippet:
            st += "from typing import List\n"
        if "ListNode" in code_snippet:
            st += "from clecode.structures import ListNode, HandleLink\n"
        if "TreeNode" in code_snippet:
            st += "from clecode.structures import TreeNode, HandleTreeTwo\n"
        if "NestedInteger" in code_snippet:
            st += "from typing import Any as NestedInteger\n"

        st += f"from clecode import decorator_default\n"
        return st

    def add_ctest(self):
        st = ""
        st += f'@decorator_default("")\n'
        st += f'def ctest(method_name, class_name):  \n'
        st += f'    return f"""\n'
        st += f'    \n'
        st += f'    >>> \n'
        st += f'    >>> res = {{class_name}}().{{method_name}}()\n'
        st += f'    """\n'
        return st

    def add_code_snippet_python(self):
        code_snippet = self.ds.codeSnippets_python3
        if not code_snippet:
            return ""
        if not isinstance(code_snippet, str):
            return ""
        is_des = False if "\n" not in code_snippet else True

        st = ""
        st += code_snippet.strip()
        st += f"\n        pass\n" if is_des else ""
        try:
            ast.parse(st)
        except:
            st = "\n"
        return st

    def add_main_content(self):
        st = ""
        st += f'if __name__ == "__main__":  \n'
        st += f'    import doctest  \n'
        st += f'    \n'
        st += f'    doctest.testmod()\n'
        return st


    @staticmethod
    def create_py_base_question_id(question_id=5, f=None, problems=None):
        if problems is None:
            problems = r"E:\progs\GitHub\leetcode2022\datas\problems.csv"
        df = pd.read_csv(problems)
        df1 = df.loc[df.question_id == question_id]
        if len(df1) == 1:
            c = OneSeriesPy(df1.iloc[0])
            c.dump(f)
            pass
        else:
            assert False, f"question_id={question_id} the series is more than 1"



if __name__ == '__main__':
    with open("b.py", "w", encoding="utf8")  as f:
        OneSeriesPy.create_py_base_question_id(46, f)

if __name__ == '__main__as':
    c = OneSeriesPy(None)
    with open("a.py", "w", encoding="utf8") as f:
        c.dump(f)

