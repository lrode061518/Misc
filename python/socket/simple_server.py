#!/usr/bin/env python
import sys
import os, pwd, grp
import random, string
import threading
import time
import ntpath
import json
import requests
import socket
import re


# funcs
def get_socket_on_random_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",0))
    return s

# Support GET/POST
def listen(s):
    try:
        header = ''
        body = ''
        buff = ''
        length = 1

        s.listen(1) # connection counts
        print("listen on port: {}".format(s.getsockname()[1]))
        client, addr = s.accept()
        while not header or length > len(body):
            r = client.recv(4096)
            if not header:
                buff = buff + r
                # try to get header
                splt = buff.split("\r\n\r\n")
                if len(splt) == 2:
                    header = splt[0]
                    body = splt[1]
                    if header.startswith('POST'):
                        length = int(re.match("(?i).*Content\-Length\:\ ([0-9]+)", header, re.DOTALL).group(1))
                    else:
                        length = 0
                    buff = ''
                continue

            # get body
            body = body + r

        client.send("HTTP/1.1 200 OK\r\n")
        client.send("Server: PyListener/0.0.1\r\n")
        client.send("Content-Type: text/plain\r\n")
        client.send("\r\n")
        client.send("OK\n")
        client.close()

        print("<<Receive>>\n{}\n\n{}\n".format(header, body))
    except Exception as  err:
        print(err)

def main():
    s = get_socket_on_random_port()
    listen(s)
    s.close()
    return


if __name__ == "__main__":
    main()
