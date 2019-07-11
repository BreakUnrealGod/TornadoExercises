import json

import requests
import tornado.web
import tornado.websocket


class ChatIndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('socketIndex.html')


users = set()


class ChatHandler(tornado.websocket.WebSocketHandler):
    # 建立连接
    def open(self, *args, **kwargs):
        users.add(self)
        # for user in users:
        #     user.write_message('[ %s ] 上线了' % self.request.remote_ip)

    def on_close(self):
        users.remove(self)

    # 给用户输出消息
    def write_message(self, message, binary=False):
        return self.ws_connection.write_message(message=message)

    # 获取websocket发送过来的消息
    def on_message(self, message):
        for user in users:
            user.write_message('[ %s ] 说[%s]' % (self.request.remote_ip, message))


class RobotIndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('robot.html')


robot_list = set()


class RobotHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        robot_list.add(self)

    def on_close(self):
        robot_list.remove(self)

    def on_message(self, message):
        print("------>", message)
        url = 'http://openapi.tuling123.com/openapi/api/v2'
        response = requests.post(url, json={
            "perception": {
                "inputText": {
                    "text": message
                },
            },
            "userInfo": {
                "apiKey": "0878ad4895b44f8387d9f8176cad742f",
                "userId": "432064"
            }
        })
        # 返回结果
        result = json.loads(response.text)
        results_list = result['results']
        # print(results_list)
        relay = results_list[0]['values']['text']
        self.write_message("小丽说:%s" % relay)
