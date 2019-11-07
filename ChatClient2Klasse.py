"""Naam: Tyron Kemble

Leerlijn: Python
Datum: 17 juli
"""

import select
import errno
import pickle
import sys
import threading

from ChatApplicatieNovi import  ClientSocketKlasse
from  ChatApplicatieNovi import  PermissionKlasse


class ChatClient2(ClientSocketKlasse.Socket):

    __client_socket = {}

    __my_username = ""

    __message = ""

    __exiting = True

    __checkPermission = False

    def __init__(self, HEADER_LENGTH,IP, PORT):
        ClientSocketKlasse.Socket.__init__(self, HEADER_LENGTH, IP, PORT)
        self.__client_socket = ClientSocketKlasse.Socket.MaakSocketConnection(ClientSocketKlasse,self.get__IP(), self.get__PORT())

        while self.__my_username != "Quit":
            self.__my_username  = input("Login Press 1, Register press 2: ")
            if self.__my_username  == '1':
                self.__my_username  = input("Username: ")
                self.__checkPermission = PermissionKlasse.Permission.checkUsername(self.__my_username , self.__my_username )
                break
            elif self.__my_username == '2':
                PermissionKlasse.Permission.RegisterAccountAndCheckPermission(PermissionKlasse)
                continue

        # Check uitvoeren of het account bestaat doormiddel van de naam te controleren.
        while self.__checkPermission  != True:
            if self.__checkPermission  == False:
                print("Jij hebt geen account")
                self.__my_username  = input("Username: ")
                self.__checkPermission  = PermissionKlasse.Permission.checkUsername(self.__my_username , self.__my_username )

    def sendUsernameToServer(self):
        # Username en Header voorbereiden om te verzenden.
        username = self.__my_username.encode('utf-8')
        username_header = f"{len(username):<{self.get__HEADER_LENGTH()}}".encode('utf-8')
        self.__client_socket.send(username_header + username)

    def ontvangberichten_loop(self,client_socket):
        while True:
            try:
                if self.__exiting:
                    # Loop door alle ontvangen berichten heen.
                    # Ontvang de header

                    username_header = self.__client_socket.recv(self.get__HEADER_LENGTH())
                    # Zodra wij geen data hebben ontvangen wordt de connectie met de server gesloten.
                    if not len(username_header):
                        print('Connection closed by the server')
                        sys.exit()

                    username_length = int(username_header.decode('utf-8').strip())

                    username = self.__client_socket.recv(username_length).decode('utf-8')

                    message_header = self.__client_socket.recv(self.get__HEADER_LENGTH())
                    message_length = int(message_header.decode('utf-8').strip())
                    self.__message = self.__client_socket.recv(message_length).decode('utf-8')

                    # Print het bericht
                    print(f'{username}> {self.__message}')
                else:
                    break


            except IOError as e:
                # Wanneer is geen data binnen komt wordt er een error gegenereerd en dat wordt in deze exception afgehandeld
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print('Reading error: ontvangen {}'.format(str(e)))
                    sys.exit()


                    continue
            except Exception as e:
                # Any other exception - something happened, exit
                print('Reading error: '.format(str(e)))
                sys.exit()



    # Zodra CheckPermission Ok is
    def checkPermissionSendMessage(self):
        if self.__checkPermission :

            while True:
                # Wacht op user input
                self.__message = input(f'{self.__my_username} > ')
                # Als er een bericht is verstuur het dan.
                # Als er een bericht is verstuur het dan.
                if self.__message == 'exit':
                    self.__exiting = False
                    break
                # druk op Q om de chat sessie te starten en andere berichten te zien.
                elif self.__message == "Q":
                        threading.Thread(target=self.ontvangberichten_loop, args=[self.__client_socket]).start()

                try:
                    if self.__message:
                        # Codeerd message to bytes, Bereid de header voor en convert het naar bytes zoals voor username hierboven, verzend alles naar de server
                        self.__message = self.__message.encode('utf-8')
                        message_header = f"{len(self.__message):<{self.get__HEADER_LENGTH()}}".encode('utf-8')
                        self.__client_socket.send(message_header + self.__message)

                except IOError as e:
                    # Wanneer is geen data binnen komt wordt er een error gegenereerd en dat wordt in deze exception afgehandeld
                    if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                        print('Reading error:  {}'.format(str(e)))
                        sys.exit()


                    continue

                except Exception as e:
                    # Any other exception - something happened, exit
                    print('Reading error: Permission '.format(str(e)))
                    sys.exit()

client2 = ChatClient2(10,"127.0.0.1",1234)
client2.sendUsernameToServer()
client2.checkPermissionSendMessage()