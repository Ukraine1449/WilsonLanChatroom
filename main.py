import socket
import sys
from threading import Thread
import random
import winsound
import time

name = input("Username: ")
userId = random.randint(10000, 250000)
server_address = ('10.167.134.241', 10000) # if this dosn't work, type ipconfig into cmd and replace this ip with the one listed under ipv4
    
def AcceptMessage():
    print('Starting up on %s port %s' % server_address)
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.bind(server_address)
    sock1.listen(1)
    
    while 1:
        connection, client_address = sock1.accept()
        try:
            data = connection.recv(999)
            message = data.decode('utf-8')
            split_message = message.split("(**__&&&&__**)")
            if int(split_message[1]) != int(userId):
                print(split_message[0])
                #winsound.Beep(1000, 200)

        except:
            connection.close()



def SendMessage():
    while 1:
        sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock2.connect(server_address)
        message=bytes(name + ": " + input('Message: ') + "(**__&&&&__**)" + str(userId),"utf-8")

t1 = Thread(target=AcceptMessage)
t2 = Thread(target=SendMessage)

t1.start()
t2.start()
