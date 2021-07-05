import requests, os

remote = "http://192.168.1.119:8000"
prefix = "/v1"

class API(object):

    headers = {'Content-Type': "application/json"}
    @classmethod
    def login(cls, username, password):
        res = requests.post(remote + prefix + "/login", headers=cls.headers, data={
            "username": username,
            "password": password
        })
        if res.status_code == 200:
            print("login success")
        print(res.json())
        # TODO
        cls.headers["Authorization"] = "Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    
    @classmethod
    def ping(cls):
        res = requests.get(remote + prefix + "/ping", headers=cls.headers)
    '''
    集成账号
    '''
#   同步集成账号
    @classmethod
    def syncCoinlistAccount(cls, emails):
        res = requests.post(remote + prefix + "/sync", headers=cls.headers, data=emails)

#   更新集成账号信息
    @classmethod
    def updateCoinlistAccount(cls):
        pass

#   彻底删除账号
    @classmethod
    def pureRemove(cls):
        pass

#   打开浏览器, 记录点击次数, 用户等信息
    @classmethod
    def openChrome(cls):
        pass
    '''
    自建账号
    '''


    '''
    广告
    '''
#   同步广告
    @classmethod
    def getannouncements(cls):
        pass


#   获取会员价格信息
    @classmethod
    def getPriceInfo(cls):
        pass

#   获取个人信息
    @classmethod
    def getUserInfo(cls):
        pass
    