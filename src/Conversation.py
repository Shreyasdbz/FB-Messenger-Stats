#############################################################################################################
#
# Class Name:       Conversation
# Arguments:        title(type:string), folderName(type:string)                    
# Functionality:    Data type for a chat conversation
#
############################################################################################################c
class Conversation:
    def __init__(self, title, folderName):
        self.title = title
        self.participantList = []
        self.messageList = []
        self.folderName = folderName
