#!/usr/bin/python3

import socket
import sys
import threading

from capstoneg08_servermessagehandler.ServerMessageHandler import ServerMessageHandler

class Client(threading.Thread):    
    def __init__(self, portNumber, host):
        threading.Thread.__init__(self)
        self.isConnected = False
        self.stopThisThread = False
        self.portNumber = portNumber
        self.host = host
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.myServerMessageHandler = ServerMessageHandler(self)
    
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
    
    def sendMessageToServer(self, msg):
        self.clientSocket.send(msg)
    
    def stopThread():
        self.stopThisThread = True
    
    def isConnected(self):
        return self.isConnected
    
    def run(self):
        # create client socket
        try:
            self.isConnected = True
            self.clientSocket.connect(self.host, self.portNumber)
            self.myServerMessageHandler = ServerMessageHandler(self.clientSocket)
            stopThisThread = False
        except socket.error as SocketError:
            print("Unable to connect to server", repr(SocketError))
        
        # handle server messages 
        while stopThisThread == False:
            try:
                msg = self.clientSocket.recv()
            except BlockingIOError:
                print("Unable to receive message.", repr(BlockingIOError))
            finally:
                self.myServerMessageHandler.handleServerMessage(msg)
            break
