"""Naam: Tyron Kemble

Leerlijn: Python
Datum: 18 juli
"""
import socket

class Socket(object):

    __client_socket = socket.socket()

    def __init__(self,HEADER_LENGTH, IP, PORT):
        self.__HEADER_LENGTH = HEADER_LENGTH
        self.__IP = IP
        self.__PORT = PORT

    def get__HEADER_LENGTH(self):
        return self.__HEADER_LENGTH

    def set__HEADER_LENGTH(self, HEADER_LENGTH):
        self.__HEADER_LENGTH = 10

    def get__IP(self):
        return self.__IP

    def set__IP(self, IP):
        self.__IP = "127.0.0.1"

    def get__PORT(self):
        return self.__PORT

    def set__PORT(self, PORT):
        self.__PORT = 1234

    def MaakSocketConnection(self, IP, PORT):
        try:
            # Maakt de socket
            self.__client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            self.__client_socket.connect((IP, PORT))

            # Zet de connectie op de state niet blokkeren, zo dat .recv() niet stops/ blokkeert maar de exception handeling uitvoert.
            self.__client_socket.setblocking(False)

            return self.__client_socket
        except:
            print("No Client Socket Connection ")
