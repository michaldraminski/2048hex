import socket
import sys

class TcpClient:

    def __init__(self, host, gotServerTcpData):
        self.host = host
        self.gotServerTcpData = gotServerTcpData

    def startReceiving(self, host):
        # x = threading.Thread(target=self.listenThread)
        #
        # try:
        #     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # except socket.error as msg:
        #     sys.stderr.write("[ERROR] %s\n" % msg)
        #     sys.exit(1)
        #
        # try:
        #     sock.connect((host, self.port))
        # except socket.error as msg:
        #     sys.stderr.write("[ERROR] %s\n" % msg)
        #     sys.exit(2)
        #
        # sock.send(b'Hello World!\r\n')
        return