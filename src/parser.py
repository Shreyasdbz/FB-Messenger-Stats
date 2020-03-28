import os
import json
from Participant import Participant
from Message import Message

path = "../"

#############################################################################################################
#
# Class Name:       Parser
# Arguments:        ""(string) OR "DEBUG" for debug statements
# Functionality:    Reads in the raw data and packs it into a Participant object array.
#
############################################################################################################
class Parser:
    def __init__(self, debug):
        self.debug = debug
        self.fileNames = []
        self.chatName = ""
        self.chatParticipants = []
        self.messages = []
        self.avoid_messages = ['You sent an atachment','']

    #------------------------------------------------------------------------------------------------------
    # Get all the conversation history files
    #------------------------------------------------------------------------------------------------------
    def setFileNames(self):
        if(self.debug == "DEBUG"):
            print("Parser:::Entered setFileNames()")
        for i in os.listdir("Data/messages/groupChat"):
            if i.endswith('.json'):
                self.fileNames.append(i)

    #------------------------------------------------------------------------------------------------------
    # Import Data from the files
    #------------------------------------------------------------------------------------------------------
    def importFileContent(self):
        if(self.debug == "DEBUG"):
            print("Parser:::Entered importFileContent()")
        for f in self.fileNames:
            filePath = "Data/messages/groupChat/" + f
            with open(filePath) as j:
                data = json.load(j)

                #Import Participants ------------------------------------------------
                for i in data['participants']:
                    for person in i:
                        exists = False
                        for participant_obj in self.chatParticipants:
                            if i[person] == participant_obj.name:
                                exists = True
                        if(exists == True):
                            exists = False
                        else:
                            self.chatParticipants.append(Participant(i[person]))
                            # if(self.debug == "DEBUG"):
                            #    print("Parser::: importFileContent() ::: Import Participants ::: " , i[person])

                #Import Messages ------------------------------------------------
                for m in data['messages']:
                    sender = ""
                    timeStamp = 0
                    content = ""
                    contentType = ""

                    for msgData in m:
                        if(msgData == "sender_name"):
                            sender = m[msgData]
                        if(msgData == "timestamp_ms"):
                            timeStamp = m[msgData]
                        if(msgData == "content"):
                            content = m[msgData]
                        if(msgData == "type"):
                            contentType = m[msgData]

                    #Append to overall Message object array
                    if(content != ""):
                        self.messages.append(Message(sender, timeStamp, content, "", "", ""))                    

                    #Append to each participant's Participant object
                    for participant_obj in self.chatParticipants:
                        if participant_obj.name == sender:
                            participant_obj.timeStamps.append(timeStamp)
                            participant_obj.contentType.append(contentType)                                
                            if(content not in self.avoid_messages):                                    
                                participant_obj.messages.append(content)

    #------------------------------------------------------------------------------------------------------
    # Return an array of Participant objects
    #------------------------------------------------------------------------------------------------------
    def getParticipantList(self):

        if(self.debug == "DEBUG"):
            print("Parser:::Entered getParticipantList()")

        return self.chatParticipants

    #------------------------------------------------------------------------------------------------------
    # Return an array of Message objects
    #------------------------------------------------------------------------------------------------------
    def getMessageList(self):

        if(self.debug == "DEBUG"):
            print("Parser:::Entered getMessageList()")

        return self.messages

    #------------------------------------------------------------------------------------------------------
    # Print data
    #------------------------------------------------------------------------------------------------------
    def printStuff(self):
        for msg in self.messages:
            # print(msg.sender, ", ", msg.timestamp)
            pass
