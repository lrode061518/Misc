#!/usr/bin/env python
import random, string
import ntpath
import json
import socket

def get_socket_on_random_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",0))
    return s

def get_random_string(count):
    return ''.join(random.choice(string.ascii_lowercase+string.digits) for i in range(count))

def pretty(o):
    if type(o) is dict:
        return json.dumps(o, indent=2)
    return o

def write_to_file(msg, file_path):
    with open(file_path, 'w+') as f:
        f.write(msg)
        print("output result to '{}'\n".format(file_path))

def get_path_basename(path):
    return ntpath.basename(path)
