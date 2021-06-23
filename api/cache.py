import threading

class AppCache(object):
    _instance_lock = threading.Lock()

    def init_self(self):
        self.user = {
            "uuid": "Ks9FzR",
            "username": "simon", # 用户名
            "email": "sandbooox@gmail.com", # 邮箱
            "phone": "188xxxx8888", # 电话
            "customNumbers": 2, # 可自建的账号数
            "coinlistNumbers": 10, # 从平台购买的coinlist账号数
        }
        self.config = {
            "current": True,
        }
    
    def __new__(cls, *args, **kwargs):
        if not hasattr(AppCache, "_instance"):
            with AppCache._instance_lock:
                if not hasattr(AppCache, "_instance"):
                    AppCache._instance = object.__new__(cls, *args, **kwargs) 
                    AppCache._instance.init_self() 
        return AppCache._instance
