import json
import os
import argparse
import requests
import argparse
from clecode.configs import cfg
from clecode.core.utils import login


def get_problems(url=None, user_agent=None, session=None):
    if url is None:
        url = "https://leetcode-cn.com/api/problems/all/"

    if user_agent is None:
        user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    session = requests.Session() if session is None else session
    is_ok, session = login(session, user_agent)
    headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}
    resp = session.get(url, headers=headers,
                       timeout=10,
                       proxies=cfg.LOGINmsg.proxy_dict)

    question_list = json.loads(resp.content.decode('utf-8'))

    return question_list

if __name__ == '__main__':
    data = get_problems()
    print(data)

if __name__ == '__main__as':
    data = get_problems()
    path = "problems01.json"
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
