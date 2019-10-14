from capstoneg08_client import Client

class UserCommandHandler:
    def _init_(self, myClient):
        self.myClient = myClient;
    
    def handleUserCommand(self, myCommand):
        self.myCommand = myCommand
        myCommandThread = UserCommandHandler(self.myClient)
        myCommandThread.start()
        
    def run(self):
        if self.myCommand == "Hello World":
            self.myClient.sendMessageToServer('Hello World')
        return
            