# ----- sender.py ------

#!/usr/bin/env python
from socket import *
import sys

s = socket(AF_INET,SOCK_DGRAM)
host =sys.argv[1]
port = sys.argv[2]
port = (int(port))
buf =1024
addr = (host,port)

number_of_lines = len(sys.stdin.readlines( ))
count = 0

#!f=open("a.txt","rb")
while(count < number_of_lines):
  f=sys.stdin.readlines(count)
  data = f
  while (data):
      if(s.sendto(data,addr)):
          print("sending ...")
          data = f.read(buf)
s.close()
f.close()