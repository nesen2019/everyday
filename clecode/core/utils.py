import ast
import json
import os
import glob
import sys
import requests
import inspect
from clecode.configs import cfg
from requests_toolbelt import MultipartEncoder


def load_module(file_path, module_name=None):
    """
    Load a module by name and search path

    This function should work with python 2.7 and 3.x

    Returns None if Module could not be loaded.
    """
    if module_name is None:
        module_name = os.path.basename(os.path.splitext(file_path)[0])
    if sys.version_info >= (3, 5,):
        import importlib.util

        spec = importlib.util.spec_from_file_location(module_name, file_path)
        if not spec:
            return

        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        return module
    else:
        import imp
        mod = imp.load_source(module_name, file_path)
        return mod



def auto_module_by_py_dir(py_dir):
    func_dir, func_basename = os.path.split(py_dir)
    import_basename = func_basename.strip().split("_v")[0]
    import_dir = glob.glob(os.path.join(func_dir, "../../../**", f"{import_basename}.py"), recursive=True)
    assert len(import_dir) == 1
    import_dir = import_dir[0]
    module = load_module(import_dir)
    return module



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

            if "_v" in os.path.basename(func.__code__.co_filename):
                module = auto_module_by_py_dir(func.__code__.co_filename)
                return getattr(module, "ctest")(*new_args, **new_kws)

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
