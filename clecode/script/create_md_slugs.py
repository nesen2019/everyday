import io


class SeriesMd(object):
    def __init__(self, slugs_df):
        self.slugs_df = slugs_df
        self.data_md = ""
        self.data_md += "".join([
            self.add_title(),
            "\n\n",
            self.add_problems(),
        ])
        pass

    def add_title(self):
        st = ""
        for slug in self.slugs_df:
            st += f"- [ ] `[{slug.question__title_slug}](https://leetcode-cn.com/problems/{slug.question__title_slug})`"
            st += f"-`{slug.frontend_question_id}`"
            st += f"-`{slug.translatedTitle}`\n"

        return st

    def add_problems(self):
        st = ""
        for slug in self.slugs_df:
            st += f"### [{slug.translatedTitle}](https://leetcode-cn.com/problems/{slug.question__title_slug})\n"
            st += "```text\n"
            st += f"{slug.translatedContent}\n"
            st += f"```\n\n"

            st += f"```python\n"
            st += f"{slug.codeSnippets_python3}\n"
            st += f"```\n\n"

        return st

    def dump(self, f=None):
        if f is None:
            return self.data_md
        elif isinstance(f, str):
            with open(f, "w", encoding="utf-8") as f:
                f.write(self.data_md)
        elif isinstance(f, io.TextIOWrapper):
            f.write(self.data_md)

        else:
            return False

        return True
