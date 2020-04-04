#!/usr/bin/python

import time
import tkinter as tk
from src import Controller

class main():

    #List conversations
    app = Controller.Controller()
    app.getConversationList()

    conversationList = app.conversationList
    convos = []
    for convo in conversationList:
        convos.append(convo.title)

    numList = []
    counter = 1
    for i in range(len(convos)):
        numList.append(counter)
        counter += 1
      
    print("###############################################################")
    print("#####            Facebook Messenger Statistics            #####")
    print("###############################################################")
    print("------               App by Shreyas Sane                -------")
    print("---------------------------------------------------------------")
#    time.sleep(1)
    print("Enter the number of the chat conversation you'd like to get statistics for.")
#    time.sleep(2)
    for i in range(len(convos)):
        print(numList[i], ". " , convos[i])
#        time.sleep(0.005)
    

    #Make a selection and pass
    convoNum = int(input("Enter your selection: ")) - 1
    app.setDirPath(conversationList[convoNum].folderName)
    app.runStuff()
    #Get Data



if __name__ == "__main__":
    main()    