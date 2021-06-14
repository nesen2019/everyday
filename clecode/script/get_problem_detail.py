import json
import os
import argparse
import time

import requests
import argparse
import ast
from clecode.configs import cfg
from clecode.core.utils import login


def get_all(session, slug, user_agent=None):
    if user_agent is None:
        user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

    url = "https://leetcode-cn.com/graphql"
    params = {
        'operationName':
            "getQuestionDetail",
        'variables': {
            'titleSlug': slug
        },
        'query':
            '''query getQuestionDetail($titleSlug: String!) {
                question(titleSlug: $titleSlug) {
                    questionId
                    questionFrontendId
                    title
                    titleSlug
                    content
                    translatedTitle
                    translatedContent
                    difficulty
                    topicTags {
                        name
                        slug
                        translatedName
                        __typename
                    }
                    codeSnippets {
                        lang
                        langSlug
                        code
                        __typename
                    }
                    __typename
                }
            }'''
    }
    json_data = json.dumps(params).encode('utf8')
    headers = {
        'User-Agent': user_agent,
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Referer': 'https://leetcode-cn.com/problems/' + slug
    }
    resp = session.post(url, data=json_data,
                        headers=headers, timeout=10,
                        proxies=cfg.LOGINmsg.proxy_dict)
    resp.encoding = 'utf8'
    content = resp.json()
    # 题目详细信息
    question = content['data']['question']
    return question


def get_problem_detail(slug, session=None, user_agent=None, time_delay=0.5):
    if session is None:
        session = requests.Session()
        is_ok, session = login(session)
    time.sleep(time_delay)
    return session, get_all(session, slug, user_agent)


def get_problems_detail(*slugs, session=None, user_agent=None, time_delay=0.5, try_it_times=3):
    if session is None:
        for i in range(try_it_times):
            session = requests.Session()
            is_ok, session = login(session)
            if is_ok:
                break
    return session, [get_problem_detail(slug, session, user_agent, time_delay)[1] for slug in slugs]


if __name__ == '__main__':
    print(get_problem_detail("p0NxJO"))
    # print(get_problem_detail("shortest-supersequence-lcci"))
