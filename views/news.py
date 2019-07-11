import asyncio
import json

import aiohttp
import tornado.web
import tornado.httpclient

import requests


class NewHandler(tornado.web.RequestHandler):
    # @asyncio.coroutine    # 协程
    # def get(self):
    #     url = 'http://api.tianapi.com/guonei/?key=772a81a51ae5c780251b1f98ea431b84'
    #     response = requests.get(url)
    #     jsondata = json.loads(response.text)
    #     newsList = jsondata.get('newslist')
    #     self.render('news.html', newsList=newsList)

    async def get(self):
        url = 'http://api.tianapi.com/guonei/?key=772a81a51ae5c780251b1f98ea431b84'
        async with aiohttp.ClientSession() as session:
            response = await session.get(url)
            jsonstr = await response.text()
            jsondata = json.loads(jsonstr)
            newsList = jsondata.get('newslist')
            self.render('news.html', newsList=newsList)


class News02Handler(tornado.web.RequestHandler):
    def __on_response(self, response):
        if response.error:
            self.send_error(500)  # 抛出500的错
        else:
            jsondata = json.loads(response.body)
            newsList = jsondata.get('newslist')
            self.render('news.html', newsList=newsList)
        self.finish()

    @tornado.web.asynchronous
    def get(self):
        url = 'http://api.tianapi.com/guonei/?key=772a81a51ae5c780251b1f98ea431b84'
        httpClient = tornado.httpclient.AsyncHTTPClient()  #
        httpClient.fetch(url, callback=self.__on_response)
    '''
    记住当你使用@tornado.web.asynchonous装饰器时，Tornado永远不会自己关闭连接。
    你必须在你的RequestHandler对象中调用finish方法来显式地告诉Tornado关闭连接。
    '''