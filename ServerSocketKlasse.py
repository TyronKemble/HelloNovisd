"""Naam: Tyron Kemble

Leerlijn: Python
Datum: 18 juli
"""
import socket

class ServerSocketKlasse(object):
    __server_socket = socket.socket()

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

    def ServerConnection (self ,IP,PORT):
        try:
            # Maakt socket
            self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # SO_ - socket option
            # SOL_ - socket option level
            # zet Reusableaddress op 1 voor de socket

            self.__server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            # De server informeert operating system dat hij het opgegeven IP adres gaat gebruiken
            self.__server_socket.bind((IP, PORT))

            # De server checked/luistert naar nieuwe connecties
            self.__server_socket.listen()
            print(f'Listening for connections on {IP}:{PORT}...')
            return self.__server_socket

        except:
            print("No Server Socket Connection ")