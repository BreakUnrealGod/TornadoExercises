from db.connect import session
from db.models import User


def add_user():
    user = User(username='admin', password='123344')
    session.add(user)
    session.commit()
    print('添加用户成功！')


def delete_user():
    user = session.query(User).filter(User.username == 'admin123')[0]
    session.delete(user)
    session.commit()
    print('删除用户成功！')

def update_user():
    user = session.query(User).filter(User.username == 'admin').update({User.username:'admin123'})
    # user.password='1111111'
    session.commit()
    print('更新成功！')

def query_user():
    users = session.query(User).all()
    print(users)
    print(users[0])

    # session.query(User).filter()


if __name__ == '__main__':
    # add_user()
    # delete_user()
    # update_user()
    query_user()