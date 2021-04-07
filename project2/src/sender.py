# ----- sender.py ------

#!/usr/bin/env python
from socket import *
import sys
import struct

s = socket(AF_INET,SOCK_DGRAM)
host =sys.argv[1]
port = sys.argv[2]
port = (int(port))
buf =1024
addr = (host,port)

number_of_lines = len(sys.stdin.readlines( ))
count = 0
ack = true

while(count < number_of_lines):
  f=sys.stdin.readlines(count)
  data = f
  f.pack(count)
  while (data && ack):
    (count)
      if(f.sendto(data,addr)):
          print("sending ...")
          data = f.read(buf) 
      if(s.recvfrom(buf)):
        ack = true
      else:
        ack = false
s.close()
f.close()
print("File sent, exiting.")