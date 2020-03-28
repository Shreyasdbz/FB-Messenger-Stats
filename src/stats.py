import os
import math
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from Participant import Participant

path = "../"

#############################################################################################################
#
# Class Name:       Stats
# Arguments:        ""(string) OR "DEBUG" for debug statements
# Functionality:    Generates statistics based on data fed from a parsed Participant List.
#
############################################################################################################
class Stats:
    def __init__(self):
        self.participantList = []
        self.messageList = []

    #------------------------------------------------------------------------------------------------------
    # Set parsed data to appropriate lists
    #------------------------------------------------------------------------------------------------------
    def setData(self, participantList, messageList):
        self.participantList = participantList
        self.messageList = messageList


    #------------------------------------------------------------------------------------------------------
    # Generates a plot of messages sent by each user in a chat
    #------------------------------------------------------------------------------------------------------
    def  messagesPerUser(self):
        names = []
        messages = []

        for participant in self.participantList:
            name_words = str.split(participant.name)
            names.append(name_words[0])      
            messages.append(len(participant.messages))    

        fig, ax = plt.subplots()
        y_pos = np.arange(len(names))
        plt.bar(y_pos, messages) 
        plt.xticks(y_pos, names)
        rect = plt.bar(y_pos, messages)

        for idx,rect in enumerate(rect):
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,
                    messages[idx],
                    ha='center', va='bottom', rotation=0)

        plt.title('Number of messages sent by each user')
        plt.show()


    #------------------------------------------------------------------------------------------------------
    # Generates a word cloud of the most used words in a chat
    #------------------------------------------------------------------------------------------------------
    def wordCloud(self):
        messageText = ""
        
        for msg in self.messageList:
            if(msg.content != ""):
                messageText = messageText + " " + msg.content
        
        wordcloud = WordCloud(width=1080, height=1080, margin=0).generate(messageText)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.margins(x=0, y=0)
        plt.title('Word cloud of most sent words in the chat')
        plt.show()
        
        
    #------------------------------------------------------------------------------------------------------
    # print stuff
    #------------------------------------------------------------------------------------------------------
    def printStuff(self):
#        self.messagesPerUser()
        self.wordCloud()
        pass
