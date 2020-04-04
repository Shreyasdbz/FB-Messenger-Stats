import os
import json
from src import Parser
from src import Stats
from src import Conversation

path = "../"

#############################################################################################################
#
# Class Name:       Controller
# Arguments:        None
# Functionality:    Controls the parsind and statistics operations
#
############################################################################################################
class Controller:
    def __init__(self):
        self.parser = Parser.Parser("")
        self.participantList = []
        self.messageList = []
        self.conversationList = []
        self.dirPath = ""


    #------------------------------------------------------------------------------------------------------
    # Gets a list of all the available conversations
    #------------------------------------------------------------------------------------------------------
    def getConversationList(self):
        fileNames = []
        filePath = ""
        for convo in os.listdir('Data/messages/inbox'):
            if(convo[0] != "."):
                fileNames.append(convo)
        for convo in fileNames:
            filePath = "Data/messages/inbox/" + convo + "/message_1.json"
            with open(filePath) as f:
                data = json.load(f)
                for i in data:
                    if i == "title":
                        self.conversationList.append(Conversation.Conversation(data['title'], convo))
                        
    #------------------------------------------------------------------------------------------------------
    # Runs all the needed methods
    #------------------------------------------------------------------------------------------------------
    def setDirPath(self, filePath):
        self.dirPath = filePath

    #------------------------------------------------------------------------------------------------------
    # Runs all the needed methods
    #------------------------------------------------------------------------------------------------------
    def runStuff(self):
        self.getConversationList()
        self.parserOps()
        self.statOps()
        self.printStuff()


    #------------------------------------------------------------------------------------------------------
    # Takes care of all the pre processing and importing functions 
    #------------------------------------------------------------------------------------------------------
    def parserOps(self):
        self.parser.setDirPath(self.dirPath)
        self.parser.setFileNames()
        self.parser.importFileContent(self.conversationList)
        self.participantList = self.parser.chatParticipants
        self.messageList = self.parser.messages
        self.parser.printStuff()
    

    #------------------------------------------------------------------------------------------------------
    # Generates statsitics about a conversation
    #------------------------------------------------------------------------------------------------------
    def statOps(self):
        for convo in self.conversationList:
            if(convo.folderName == self.dirPath):
                stat = Stats.Stats(convo)
                stat.printStuff()


    #------------------------------------------------------------------------------------------------------
    # Print Stuff
    #------------------------------------------------------------------------------------------------------
    def printStuff(self):
        for convo in self.conversationList:
            if(convo.folderName == "FrehCurrency_U35V8y-xEA"):
                for p in convo.participantList:
                    # print(p.name)
                    pass



#Parkland Chat:
#test.setDirPath("Isweartogodwerenormalpeople_Rs3jzQUoVA")
#soccer chat:
#test.setDirPath("ohJ6e3Zymg")