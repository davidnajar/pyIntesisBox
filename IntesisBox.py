import asyncio
import logging
import socket
_LOGGER = logging.getLogger('pyintesisbox')

class IntesisBox(asyncio.Protocol):
    def __init__(self, ip, port):
        self._ip = ip
        self._port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server=(self._ip, self._port)


  

    def start(self):
        self._socket.connect(self._server)
        self._socket.sendall(str.encode('ID\r'))
        while 1:
            data = self._socket.recv(1024)
            if not data:
                break
            self.data_received(data)
        

 

    def data_received (self, data):
        if data != '':
            print(data)
            message = data.split(':')
            if message[0] == 'ID':
                parameters = message.split(',')
                self.model= parameters[0]
                self.mac = parameters [1]
                self.ip = parameters [2]
                print(self.ip)



        
      


    


