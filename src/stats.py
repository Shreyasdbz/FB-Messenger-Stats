import os
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
from wordcloud import WordCloud

#############################################################################################################
#
# Class Name:       Stats
# Arguments:        ""(string) OR "DEBUG" for debug statements
# Functionality:    Generates statistics based on data fed from a parsed Participant List.
#
############################################################################################################
class Stats:
    def __init__(self, conversation):
        self.debug = ""
        self.conversation = conversation
        self.participantList = conversation.participantList
        self.messageList = conversation.messageList
        self.title = conversation.title
        
    ####
    # Stats ideas:
    #   Messages per user bar graph / pie chart
    #   Word cloud for most used words
    #   Stacked bar graphs for messages, pics, gifs and stickers per user
    #   Time chat is most active
    #   Time user is most active
    #   Most reacts
    #   Most emojis
    ####

    #------------------------------------------------------------------------------------------------------
    # Generates a plot of messages sent by each user in a chat
    #------------------------------------------------------------------------------------------------------
    def  messagesPerUser(self):
        names = []
        messages = []
        photos = []
        gifs = []
        total = []

        for participant in self.participantList:
            name_words = str.split(participant.name)
            names.append(name_words[0])      
            # names.append(participant.name)      
            messages.append(len(participant.messages))    
            photos.append(participant.photosCount)  
            gifs.append(participant.gifsCount) 
            temp_num = len(participant.messages) + participant.photosCount + participant.gifsCount + participant.stickersCount
            total.append(temp_num)

        fig, ax = plt.subplots()
        y_pos = np.arange(len(names))
        plt.bar(y_pos, total, align='edge', width=0) 
        plt.xticks(y_pos, names, wrap=True, fontsize=8)
        rect = plt.bar(y_pos, total)

        for idx,rect in enumerate(rect):
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1.01*height, total[idx], ha='center', va='bottom', rotation=0)

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
    # Shows overall chat statsitics like messages & photos sent, time most active, Date Created
    #------------------------------------------------------------------------------------------------------
    def chatStats(self):

        if(self.debug == "DEBUG"):
            print("Stats:::Entered chatStats()")

        pass


    #------------------------------------------------------------------------------------------------------
    # print stuff
    #------------------------------------------------------------------------------------------------------
    def printStuff(self):
        self.messagesPerUser()
        self.wordCloud()
        pass
