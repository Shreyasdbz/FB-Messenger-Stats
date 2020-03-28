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
        self.stickersCount = 0
        self.photosCount = 0
        self.gifsCount = 0
        self.contentType = []
