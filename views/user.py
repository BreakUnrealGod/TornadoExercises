import tornado.web

from db.connect import session
from db.models import User


class UserRegisterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('user/register.html', msg='')

    def post(self):
        username = self.get_body_argument('username')
        password = self.get_body_argument('password')
        repassword = self.get_body_argument('repassword')
        if password == repassword:
            user = User()
            user.username = username
            user.password = password

            session.add(user)
            session.commit()
            # self.write('用户注册成功')
            self.redirect(self.reverse_url('login'))
        else:
            self.render('user/register.html', msg='密码不一致')


class BaseHandler(tornado.web.RequestHandler):
    def prepare(self):
        print('----->prepare')

    def _initialize(self):
        print('-------->_initialize')

    def get_current_user(self):
        super(BaseHandler,self).get_current_user()
        print('====>get_current_user')
        username = self.get_secure_cookie('username')
        if username:
            return username
        return None


class UserHandler(BaseHandler):

    # @tornado.web.authenticated
    def get(self):
        self.render('user/index.html')


class UserLoginHandler(BaseHandler):
    def get(self):
        self.render('user/login.html', msg='')

    def post(self):
        username = self.get_body_argument('username')
        password = self.get_body_argument('password')

        if username and password:
            user = session.query(User).filter(User.username == username, User.password == password)
            if user:
                # 用户登录成功
                self.set_secure_cookie('username', user[0].username)
                self.redirect(self.reverse_url('index'))
        self.render('user/login.html', msg='用户名或者密码有误！')


class AddBookHandler(BaseHandler):
    # @login_required    login_url=''
    @tornado.web.authenticated
    def get(self):
        self.render('book/add.html')

    def post(self):
        pass
