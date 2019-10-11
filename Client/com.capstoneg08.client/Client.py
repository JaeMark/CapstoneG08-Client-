import socket
import sys
import threading

class Client(threading.Thread):
    isConnected = False
    stopThisThread = False
    
    portNumber = 8888;
    host = 'localhost'
    
    def _inti_ (self, portNumber, host):
        self.portNumber = portNumber
        self.host = host
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        threading.Thread.__init__(self)
    
    def connectToServer(self):
        myClientThread = Client(self.ip, self.port)
        myClientThread.start()
        return True
    
    def disconnectFromServer(self):
        try:
            isConnected = False
            self.clientSocket.close()
            self.clientSocket is None
        except socket.error as SocketError:
            print("Unable to disconnect from server", repr(SocketError))
    
    def stopThread():
        stopThisThread = True
    
    def isConnceted():
        return isConnected
    
    def run(self):
        # create client socket
        try:
            isConnected = True
            self.clientSocket.connect(self.host, self.portNumber)
            stopThisThread = False
        except socket.error as SocketError:
            print("Unable to connect to server", repr(SocketError))
        
        # handle server messages 
        while stopThisThread == False:
            break