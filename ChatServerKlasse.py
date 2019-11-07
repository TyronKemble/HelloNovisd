"""Naam: Tyron Kemble

Leerlijn: Python
Datum: 17 juli
"""

import socket
import pickle
import select
import time
import threading

from ChatApplicatieNovi import ServerSocketKlasse
from ChatApplicatieNovi import  ChatHistoryKlasse




class ChatServerKlasse(ServerSocketKlasse.ServerSocketKlasse):
    __client_socket = {}
    __chatHistoryFile = {}
    __sockets_list = []
    # Empty array voor de berichten geschiedenis
    __message_history = []
    # lijst van clients die geconnect zijn - socket is key, user header and name is als data.
    __clients = {}
    __notified_socket = []
    __user = {}
    __message = {}

    def __init__(self, HEADER_LENGTH, IP, PORT):
        super().__init__( HEADER_LENGTH, IP, PORT)
        self.__client_socket = self.socketConnection()
        self.__sockets_list = [self.__client_socket]
        self.__chatHistoryFile = ChatHistoryKlasse.ChatHistory.createChatHistoryFile()

    def socketConnection(self):
        return ServerSocketKlasse.ServerSocketKlasse.ServerConnection(ServerSocketKlasse, self.get__IP(), self.get__PORT())


    def broadCastMessage(self,clients):



        for client_socket in self.__clients:
            # Send het bericht niet naar de gebruiker die het bericht heeft verzonden.
            if client_socket != self.__notified_socket:
                client_socket.send(self.__user['header'] + self.__user['data'] + self.__message['header'] + self.__message['data'])


    # Functie Handelt de ontvangen berichten af.
    def receive_message(self,client_socket):
        try:
            # Ontvangt de "header" de inhoud is de message lengte
            message_header = client_socket.recv(self.get__HEADER_LENGTH())
            # Als er geen data wordt ontvangen word de connectie afgesloten.
            if not len(message_header):
                return False
            # Converteert header naar int
            message_length = int(message_header.decode('utf-8').strip())
            # Returned object van message_header en message data
            return {'header': message_header, 'data': client_socket.recv(message_length)}
        except:
            # zodra de gebruiker de connectie vrijwillig beeindigd
            return False

    # Functie 2 - CheckSocketsAndAddSockets - Keep listening for nieuw connection
    def CheckSocketsAndAddSockets(self):
        while True:
            # Dit zorgt voor een blokkering, de code executie wacht hier zodra er actie nodig is wordt dat uitgevoerd.
            read_sockets, _, exception_sockets = select.select(self.__sockets_list, [], self.__sockets_list)

            # Loopt door op de hoogte gestelde sockets heen.
            for self.__notified_socket in read_sockets:
                # Als de op de hoogte gestelde socket een server socket is.
                if self.__notified_socket == self.__client_socket :

                    # Accepteerd nieuwe connecties
                    # Elke client krijgt zijn eigen unique adress
                    client_socket, client_address = self.__client_socket.accept()
                    # De client stuurt zijn gebruikers naam mee.
                    self.__user = self.receive_message(client_socket)
                    # If false - wordt de gebruiker gedisconnect.
                    if self.__user is False:
                        continue

                    # geaccepteerde socket wordt aan de lijst toegevoegd.
                    self.__sockets_list.append(client_socket)

                    self.__clients[client_socket] = self.__user
                    print('Accepted new connection from {}:{}, username: {}'.format(*client_address,
                                                                                    self.__user['data'].decode('utf-8')))

                else:
                    # Ontvang het bericht
                    self.__message = self.receive_message(self.__notified_socket)
                    # If false - wordt de client gedisconnect met een bericht
                    if self.__message is False:

                        print('Closed connection from: {}'.format(self.__clients[self.__notified_socket]['data'].decode('utf-8')))

                        self.__sockets_list.remove(self.__notified_socket)

                        del self.__clients[self.__notified_socket]
                        continue

                    self.__user = self.__clients[self.__notified_socket]

                    print(f'Received message from {self.__user["data"].decode("utf-8")}: {self.__message["data"].decode("utf-8")}')
                    # voegt de berichten die naar de server zijn verzonden toe aan de arraylist.
                    self.__message_history.append(f'Received message from {self.__user["data"].decode("utf-8")}: {self.__message["data"].decode("utf-8")} : On {time.ctime()}')
                    # slaat het bericht op
                    ChatHistoryKlasse.ChatHistory.storeChatHistory(self.__message_history, self.__message_history,self.__chatHistoryFile)


                    # Loopt door alle aangesloten clients heen en broadcast het bericht
                    threading.Thread(target=self.broadCastMessage, args=[self.__clients]).start()




Chat = ChatServerKlasse(10,"127.0.0.1",1234)
Chat.CheckSocketsAndAddSockets()

