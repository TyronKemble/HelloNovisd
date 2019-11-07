"""Naam: Tyron Kemble

Leerlijn: Python
Datum: 22 juli
"""

import pickle
import re

class ChatHistory(object):

    def __init__(self, open):
        self.__open = self.openChatHistory()

    def createChatHistoryFile():
        try:
            f = open("ChatHistory.txt", 'w')
        except:
            print("Kan het bestand ChatHistory.txt niet aanmaken ")
        return f

    def openChatHistory():
        try:
            inFile = open('ChatHistory.txt', 'rb')
        except:
            print("Kan het bestand ChatHistory.txt niet uitlezen. Het bestand ChatHistory.txt is niet opgeslagen")

        newlist = pickle.load(inFile)
        fullChatHistory = []
        for l in newlist:
            fullChatHistory.append(l)

        return fullChatHistory


    def storeChatHistory(self, message_history, f):
        try:
            with open("ChatHistory.txt", 'wb') as f:
                 return pickle.dump(message_history, f)
        except:
            print("Kan niet schrijven naar Chathistory.txt ")



