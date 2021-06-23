import threading


class Connector(object):
    _instance_lock = threading.Lock()

    def bind(self, signal, cb):
        if signal not in self.__binder:
            self.__binder[signal] = []
        self.__binder[signal].append(cb)

    def send(self, signal, **kwargs):
        if signal in self.__binder:
            for fun in self.__binder[signal]:
                fun(**kwargs)

    def __new__(cls, *args, **kwargs):
        if not hasattr(Connector, "_instance"):
            with Connector._instance_lock:
                if not hasattr(Connector, "_instance"):
                    Connector._instance = object.__new__(cls, *args, **kwargs) 
                    Connector._instance.__binder = {} 
        return Connector._instance
