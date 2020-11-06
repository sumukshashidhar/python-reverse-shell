import socket
import threading
import os


BIND_IP = "127.0.0.1"
BIND_PORT = 23
SERV_ADD = BIND_IP, BIND_PORT

def send_commands(con):
    while True:
        cmd = input()
        if cmd == 'quit':
            con.close()
            server.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((SERV_ADD))
server.listen(5)
print ("[*] listening on {}:{}".format(BIND_IP, BIND_PORT))
#4
conn,addr = server.accept()
print('accepted connection from {} and port {}'.format(addr[0],addr[1]))
print("enter the commands below")
#5
send_commands(conn)
conn.close()
