# ----- receiver.py -----

#!/usr/bin/env python

from socket import *
import sys
import select
import struct

host="0.0.0.0"
port = int(sys.argv[1])
s = socket(AF_INET,SOCK_DGRAM)
s.bind((host,port))

addr = (host,port)
buf=1024
windowbuf=10
header = 0

data,addr = s.recvfrom(buf)
try:
    while(data):
        print(type(sys.stdout))
        sys.stdout.write(str(data))
        s.settimeout(2)
        data,addr = s.recvfrom(buf)
        header = struct.unpack(data)
        if(header)
          f.sendto(True,addr)
          data = f.read(windowbuf)
        
except timeout:
    f.close()
    s.close()
    print("File received, exiting.")
