"""Naam: Tyron Kemble

Leerlijn: Python
Datum: 19 juli
"""

import select
import errno
import pickle
import sys
import threading

from ChatApplicatieNovi import  ClientSocketKlasse
from ChatApplicatieNovi import  Admin
from  ChatApplicatieNovi import ChatHistoryKlasse
from  ChatApplicatieNovi import  PermissionKlasse


class Administrator(ClientSocketKlasse.Socket, Admin.Admin):

    __admin_socket = {}

    __exiting = True

    __message = ""

    def __init__(self, HEADER_LENGTH,IP, PORT, id, name,email):
        ClientSocketKlasse.Socket.__init__( self, HEADER_LENGTH, IP, PORT)
        Admin.Admin.__init__(self, id, name,email)
        self.__admin_socket = self.socketConnection()


    def socketConnection(self):
            return ClientSocketKlasse.Socket.MaakSocketConnection(ClientSocketKlasse, self.get__IP(), self.get__PORT())

    def checkPermission(self):
        return PermissionKlasse.Permission.checkUsername(self.get__naam(), self.get__naam())


    def ontvangberichten_loop(self, admin_socket):
        print("Monitoringsbeheer is gestart -  ")
        while True:
            try:
                if self.__exiting:
                    # Loop door alle ontvangen berichten heen.
                    # Ontvang de header
                    self.__message
                    username_header = self.__admin_socket.recv(self.get__HEADER_LENGTH())
                    # Zodra wij geen data hebben ontvangen wordt de connectie met de server gesloten.
                    if not len(username_header):
                        print('Connection closed by the server')
                        sys.exit()

                    username_length = int(username_header.decode('utf-8').strip())

                    username = self.__admin_socket.recv(username_length).decode('utf-8')

                    message_header = self.__admin_socket.recv(self.get__HEADER_LENGTH())
                    message_length = int(message_header.decode('utf-8').strip())
                    self.__message = self.__admin_socket.recv(message_length).decode('utf-8')

                    # Print het bericht
                    print(f'{username}> {self.__message}')
                else:
                    break


            except IOError as e:
                # Wanneer is geen data binnen komt wordt er een error gegenereerd en dat wordt in deze exception afgehandeld
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print('Reading error: ontvangen {}'.format(str(e)))
                    sys.exit()

                # # Wij hebben niks ontvangen
                    continue
            except Exception as e:
                # Any other exception - something happened, exit
                print('Reading error: '.format(str(e)))
                sys.exit()

    def sendUsernameToServer(self):
        # Prepare username and header and send them
        # We need to encode username to bytes, then count number of bytes and prepare header of fixed size, that we encode to bytes as well
        username = self.get__naam().encode('utf-8')
        username_header = f"{len(username):<{self.get__HEADER_LENGTH()}}".encode('utf-8')
        self.__admin_socket.send(username_header + username)


    def checkPermissionAndMenu(self):
        # if self.checkPermission:
        while True:
            self.__message = input("Kies 1 om de ChatHistory in te zien , Kies 2 voor de Monitoring: ")
            if self.__message == '1':
                    self.__message = print(ChatHistoryKlasse.ChatHistory.openChatHistory())
            elif self.__message == '2':
                threading.Thread(target=self.ontvangberichten_loop, args=[self.__admin_socket]).start()

Admin = Administrator(10,"127.0.0.1", 1234, 100,"Henk","Henk.Vrieswijk@gmail.com")
Admin.sendUsernameToServer()
Admin.checkPermissionAndMenu()