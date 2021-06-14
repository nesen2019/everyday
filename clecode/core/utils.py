import ast
import json
import os
import requests
import inspect
from clecode.configs import cfg
from requests_toolbelt import MultipartEncoder


def decorator_default(method_name, class_name="Solution"):
    def decorator(func):
        def decorated(*args, **kwargs):

            kws = dict(class_name=class_name, method_name=method_name)

            signature = inspect.signature(func)
            for key, value in signature.parameters.items():
                if value.default and (value.default != inspect._empty):
                    kws.update({key: value.default})

            kws.update(kwargs)

            for a, b in zip(args, signature.parameters):
                kws.update({b: a})

            new_kws = dict()
            for key, value in kws.items():
                new_kws.update({key: value if isinstance(value, str) else value.__name__})

            new_args = list()
            for i, a, b in zip(range(max(len(args), len(signature.parameters))), args, signature.parameters):
                new_args.append(new_kws[b])
                new_kws.pop(b)

            return func(*new_args, **new_kws)

        return decorated
    return decorator


def login(session, user_agent=None):
    if user_agent is None:
        user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

    url = 'https://leetcode-cn.com'

    # cookies = session.get(url, proxies=cfg.LOGINmsg.proxy_dict)

    url = "https://leetcode-cn.com/accounts/login"

    params_data = dict(
        login=cfg.LOGINmsg.email,
        password=cfg.LOGINmsg.password,
        next="problems"
    )

    headers = {
        "User-Agent": user_agent,
        "Connection": 'keep-alive',
        'Referer': 'https://leetcode-cn.com/accounts/login/',
        "origin": "https://leetcode-cn.com"
    }
    m = MultipartEncoder(params_data)

    headers['Content-Type'] = m.content_type

    session.post(url, headers=headers, data=m,
                 timeout=10, allow_redirects=False,
                 proxies=cfg.LOGINmsg.proxy_dict)
    is_login = session.cookies.get('LEETCODE_SESSION') != None
    return is_login, session
