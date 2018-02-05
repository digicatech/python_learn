import socket
import os

def radioPoller():
    msg1="GET / HTTP/1.1"+'\r'+'\n'+"Host: shoutcast.radyogrup.com"+'\r'+'\n'+"User-Agent: VLC/2.0.5 LibVLC/2.0.5"+'\r'+'\n'+"Range: bytes=0-"+'\r'+'\n'+"Connection: close"+'\r'+'\n'+"Icy-MetaData: 1"+'\r'+'\n'+'\r'+'\n'


    HOST = '46.20.7.103'                      # The remote host
    PORT = 8030                                # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    s.sendto(msg1.encode() , (HOST, PORT))                                 #sending http request
    data=""
    while len(data)<1024:
        data=s.recv(1024)               #recieving a few characters

    print(data)


radioPoller()