#############################################################################################################
#
# Class Name:       Participant
# Arguments:        name(type:string)
# Functionality:    Acts as a datatype for a chat participant
#
############################################################################################################c
class Participant:
    def __init__(self, name):
        self.name = name
        self.timeStamps = []
        self.messages = []
        self.sticker = 0
        self.photos = 0
        self.gifs = 0
        self.contentType = []
