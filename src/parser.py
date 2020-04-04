import os
import json
from src import Participant
from src import Message

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
        self.dirPath = ""
        self.fileNames = []
        self.chatName = ""
        self.chatParticipants = []
        self.messages = []
        self.avoid_messages = ['asdf']

    #------------------------------------------------------------------------------------------------------
    # Sets the path of the conversation director to parse
    #------------------------------------------------------------------------------------------------------
    def setDirPath(self, dirPath):
        self.dirPath = dirPath

    #------------------------------------------------------------------------------------------------------
    # Get all the conversation history files
    #------------------------------------------------------------------------------------------------------
    def setFileNames(self):
        if(self.debug == "DEBUG"):
            print("Parser:::Entered setFileNames()")
        for i in os.listdir("Data/messages/inbox/" + self.dirPath):
            if i.endswith('.json'):
                self.fileNames.append(i)

    #------------------------------------------------------------------------------------------------------
    # Import Data from the files
    #------------------------------------------------------------------------------------------------------
    def importFileContent(self, conversationList):
        if(self.debug == "DEBUG"):
            print("Parser:::Entered importFileContent()")
            
        for convo in conversationList:
            if convo.folderName == self.dirPath:

                for f in self.fileNames:
                    filePath = "Data/messages/inbox/" + self.dirPath + "/" + f

                    with open(filePath) as j:
                        data = json.load(j)
                        if(self.debug == "DEBUG"):
                            print("Parser:::importfileContent():::readingFile: ", filePath)

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
                                    self.chatParticipants.append(Participant.Participant(i[person]))
                                    if(self.debug == "DEBUG"):
                                       print("Parser::: importFileContent() ::: Import Participants ::: " , i[person])
                        
                        #Import Messages ------------------------------------------------
                        for m in data['messages']:
                            sender = ""
                            timeStamp = 0
                            content = ""
                            contentType = ""
                            photo_uri = ""
                            gifs_uri = ""
                            sticker_uri = ""

                            for msgData in m:
                                if(msgData == "sender_name"):
                                    sender = m[msgData]
                                if(msgData == "timestamp_ms"):
                                    timeStamp = m[msgData]
                                if(msgData == "content"):
                                    content = m[msgData]
                                if(msgData == "photos"):
                                    for photoData in m['photos']:
                                        photo_uri = photoData['uri']
                                if(msgData == "gifs"):
                                    for photoData in m['gifs']:
                                        gifs_uri = photoData['uri']
                                if(msgData == "sticker"):
                                    for photoData in m['sticker']:
                                        pass
                                        # sticker_uri = photoData['uri']
                                if(msgData == "type"):
                                    contentType = m[msgData]

                            #Append to overall Message object array
                            self.messages.append(Message.Message(sender, timeStamp, content, photo_uri, gifs_uri, sticker_uri))                    

                            #Check if sender is in participants list
                            # Participants who have left the chat don't show up in the default participants
                            existingNames = []
                            for participant_obj in self.chatParticipants:
                                existingNames.append(participant_obj.name)
                            if sender not in existingNames:
                                self.chatParticipants.append(Participant.Participant(sender))

                            #Append to each participant's Participant object
                            for participant_obj in self.chatParticipants:
                                if participant_obj.name == sender:
                                    participant_obj.timeStamps.append(timeStamp)
                                    participant_obj.contentType.append(contentType)                                
                                    if(content not in self.avoid_messages):                                    
                                        participant_obj.messages.append(content)
                                    if(photo_uri != ""):
                                        participant_obj.photosCount += 1
                                    if(gifs_uri != ""):
                                        participant_obj.gifsCount += 1
                                    if(sticker_uri != ""):
                                        participant_obj.stickersCount += 1

                convo.participantList = self.chatParticipants
                convo.getMessageList = self.messages                    


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
