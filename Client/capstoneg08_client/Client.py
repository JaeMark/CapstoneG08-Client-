#!/usr/bin/python3

import socket
import sys
import threading

from capstoneg08_servermessagehandler.ServerMessageHandler import ServerMessageHandler

class Client(threading.Thread):    
    def __init__(self, buffSize, host, portNumber):
        threading.Thread.__init__(self)
        
        self.buffSize = buffSize
        self.host = host
        self.portNumber = portNumber
        
        self.isConnected = False
        self.stopThisThread = False
        
        self.myServerMessageHandler = ServerMessageHandler(self)

    def disconnectFromServer(self):
        try:
            self.isConnected = False
            self.clientSocket.close()
            self.clientSocket is None
        except socket.error as SocketError:
            print("Unable to disconnect from server, because ", repr(SocketError))
    
    def sendMessageToServer(self, msg):
        self.clientSocket.sendall(msg)
    
    def stopThread(self):
        self.stopThisThread = True
    
    def isConnected(self):
        return self.isConnected
    
    def run(self):
        # create client socket
        try:
            self.isConnected = True
            self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.clientSocket.connect((self.host, self.portNumber))
            self.myServerMessageHandler = ServerMessageHandler(self.clientSocket)
            self.stopThisThread = False
        except socket.error as SocketError:
            print("Unable to connect to server, because ", repr(SocketError))
        
        # handle server messages 
        msg = ''
        while self.stopThisThread == False:
            try:
                msg = self.clientSocket.recv(self.buffSize)
            except BlockingIOError:
                print("Unable to receive message, because ", repr(BlockingIOError))
            finally:
                self.myServerMessageHandler.handleServerMessage(msg)
            break
