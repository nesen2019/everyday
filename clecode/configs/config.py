import os


class LoginMsg:
    def __init__(self):
        self.email = "nihaoma-u"
        self.password = "w2849337909"
        self.proxy_dict = dict(
            http="http://127.0.0.1:7890/",
            https="https://127.0.0.1:7890/"
        )
        self.proxy_dict = None


class LeetCode:
    def __init__(self):
        self.PATH_PROJECT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        self.PATH_ROOT = os.path.dirname(os.path.dirname(__file__))
        self.LOGINmsg = LoginMsg()
        self.PATH_ALL_CSV = os.path.join(self.PATH_ROOT, "datas/problems.csv")
        self.PATH_CTASKS = os.path.join(self.PATH_PROJECT, "ctasks")


cfg = LeetCode()
