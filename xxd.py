import os.path
import string
import sys
import textwrap
if (len(sys.argv)<2):
    print ("Please enter file name")        #chech arguments

filename = ''.join(sys.argv[1:])    
#print (filename)
fileEx = os.path.isfile(filename)           #check file name

if (fileEx==False):
    print ("File not found!")

f = open(filename,"r")
content = f.read()
#print(content)                             #open file

reContent = ".".join( content.split())      #remove space and add dot
hexcount=0

length=len(reContent)                       #get string length
i=0
i=length/16+1                               #count needed nbr of rows   

#print(i)
c=0
d = int(c)
j = int(i)                                  #define counter and number of rows

#print(d,j)

def split_every(n, s):
    xrange=0
    return [ s[i:i+n] for i in xrange(0, len(s), n) ]

while(d<j):                                 #print result
    string=(reContent[hexcount:hexcount+16])
    #print(string)
    hexcount=hexcount+16
    asci=""
    for i in str(string):
        asci+=str(hex(ord(i)))[4::]
    asci+="0a"
    hexnumber=hex(hexcount)
    hexcode=" ".join("{:0x}".format(ord(c)) for c in string)
    fullhex=hexcode.replace(" ", "")
    print(hexnumber,"\t",fullhex[0:4],fullhex[4:8],fullhex[8:12],fullhex[12:16],"\t", string)
    d=d+1

# 29 code lines (without blank lines and comment lines) :-) 
