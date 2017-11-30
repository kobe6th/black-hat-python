#!/usr/bin/env python
#
# -*- coding:utf-8 -*-
#

import socket
import threading

target_host = "127.0.0.1"
target_port = 80

def handle_client(client, addr):
    print "accpect connect from %s:%s"%addr
    request = client.recv(4096)
    print "client request: %s"%(request)
    client.send("this is server response!")
    client.close()

def server_start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target_host, target_port))
    server.listen(5)
    print "listening on %s:%d"%(target_host, target_port)
    while True:
        client, addr = server.accept()
        t = threading.Thread(target=handle_client, args=(client,addr))
        t.start()

server_start()