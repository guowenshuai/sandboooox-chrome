import socket

def detect_port(ip,port):
    """检测ip上的端口是否开放
    """
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((ip,int(port)))
        s.shutdown(2)
        print('{0} is open'.format(port))
        return True
    except:
        print('{0} is close'.format(port))
        return False

if __name__ == '__main__':
    detect_port('127.0.0.1', 8080)
