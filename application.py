import tornado.web

import settings
from views.chat import ChatIndexHandler, ChatHandler, RobotIndexHandler, RobotHandler
from views.news import NewHandler, News02Handler

from views.user import UserRegisterHandler,UserHandler,UserLoginHandler,AddBookHandler


class Application(tornado.web.Application):
    def __init__(self):
        # 路由配置
        handler = [
            tornado.web.url(r'/',UserHandler,name='index'),
            tornado.web.url(r'/register', UserRegisterHandler, name='register'),
            tornado.web.url(r'/login', UserLoginHandler, name='login'),
            tornado.web.url(r'/addbook', AddBookHandler, name='addbook'),
            tornado.web.url(r'/news',NewHandler,name='news'),
            tornado.web.url(r'/news2',News02Handler,name='news2'),
            tornado.web.url(r'/cindex', ChatIndexHandler, name='cindex'),
            tornado.web.url(r'/chat', ChatHandler, name='chat'),
            tornado.web.url(r'/robotindex', RobotIndexHandler, name='cindex'),
            tornado.web.url(r'/robot', RobotHandler, name='chat'),
        ]

        super(Application, self).__init__(handler, **settings.config)
