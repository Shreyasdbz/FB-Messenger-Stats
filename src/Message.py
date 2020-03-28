#############################################################################################################
#
# Class Name:       Message
# Arguments:        sender(type:string), timestamp(type:int), content(type:string), photo(tyep:string)
#                   gif(type:string), sticker(type:string)                    
# Functionality:    Acts as a datatype for a chat participant
#
############################################################################################################c
class Message:
    def __init__(self, sender, timestamp, content, photo, gif, sticker):
        self.sender = sender
        self.timestamp = timestamp
        self.content = content
        self.photo = photo
        self.gif = gif
        self.sticker = sticker
