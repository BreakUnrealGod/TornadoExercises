import os

BASE_DIR = os.path.dirname(__file__)
options = {
    'port': 8080
}

config = {
    "cookie_secret": "bZJc2sW(90RRHD*((Hn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
    'debug': True,
    'template_path': os.path.join(BASE_DIR, 'templates'),
    'static_path': os.path.join(BASE_DIR, 'static'),
    'autoescape': None,
    "xsrf_cookies": True,
    "login_url": "/login",
    'default_host': '0.0.0.0'
}

# 数据库设置
mysql = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'port': 3306,
    'dbname': 'tornadotest'
}
