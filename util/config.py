import os, configparser
import threading

userHome = os.path.expanduser('~')
configPath = os.path.join(userHome, ".sandbooox-chrome.ini")

class LocalConfig(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        self.__config = configparser.ConfigParser()
        self.__config.read(configPath)
    
    @property
    def config(self):
        return self.__config

    def save(self):
        # self.__config
        with open(configPath, 'w') as configfile:
            self.__config.write(configfile)
    
    def __new__(cls, *args, **kwargs):
        if not hasattr(LocalConfig, "_instance"):
            with LocalConfig._instance_lock:
                if not hasattr(LocalConfig, "_instance"):
                    LocalConfig._instance = object.__new__(cls)  
        return LocalConfig._instance
