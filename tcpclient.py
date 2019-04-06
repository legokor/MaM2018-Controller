import socket

TCP_IP = '192.168.4.1'
# TCP_IP = '192.168.0.151'
TCP_PORT = 1360
BUFFER_SIZE = 100

class TCPClient:
    def __init__(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(1)
            self.socket.connect((TCP_IP, TCP_PORT))
        except socket.timeout:
            print("Can't connect to "+str(TCP_IP)+":"+str(TCP_PORT))

    def send(self,message):
        print("sent: "+message)
        self.socket.send((message+"\r\n").encode())
    def recv(self):
        try:
            return self.socket.recv(BUFFER_SIZE)
        except socket.timeout:
            print("socket timeout")
    def close(self):
        self.socket.close()

