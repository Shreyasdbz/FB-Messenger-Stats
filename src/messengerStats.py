import os
from Parser import Parser
from Stats import Stats

class messengerStats:
    def __init__(self):
        self.parser = Parser("")
        self.stat = Stats()
        self.participantList = []
        self.messageList = []

    def runStuff(self):
        self.parserOps()
        self.statOps()
        self.printStuff()

    def parserOps(self):
        self.parser.setFileNames()
        self.parser.importFileContent()
        self.participantList = self.parser.chatParticipants
        self.messageList = self.parser.messages
        self.parser.printStuff()
    
    def statOps(self):
        self.stat.setData(self.participantList, self.messageList)
        self.stat.printStuff()

    def printStuff(self):
        pass



test = messengerStats()
test.runStuff()