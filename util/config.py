import os, configparser
import threading

userHome = os.path.expanduser('~')
configPath = os.path.join(userHome, ".sandbooox-chrome.ini")

class LocalConfig(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        self.__config = configparser.ConfigParser()
        self.__config.read(configPath)
        if "auto" not in self.__config:
            self.__config['auto'] = {
                "showpass": "no"
            }
        if "coinlist" not in self.__config:
            self.__config["coinlist"] = {
                "email": "[]"
            }
        if "browser" not in self.__config:
            self.__config["browser"] = {
                "exec": ""
            }
        self.save(self.__config)
            
    @property
    def config(self):
        return self.__config

    def save(self, config):
        self.__config = config
        with open(configPath, 'w') as configfile:
            self.__config.write(configfile)
    
    def __new__(cls, *args, **kwargs):
        if not hasattr(LocalConfig, "_instance"):
            with LocalConfig._instance_lock:
                if not hasattr(LocalConfig, "_instance"):
                    LocalConfig._instance = object.__new__(cls, *args, **kwargs)  
        return LocalConfig._instance
