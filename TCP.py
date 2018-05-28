from ctypes import *
import sys
import socket
import struct
import os

class TCP_class(Structure):
    _fields_=[
        ("Src", c_ushort),         
        ("dst", c_ushort),      
        ("seqNo", c_long),       
        ("ackNo", c_long),
        ("Offset", c_ubyte, 4), 
        ("Reserved", c_ubyte, 4),
        ("Flag",  c_ubyte),
        ("Window", c_ushort),
        ("CheckSum", c_ushort),
        ("URG_point", c_ushort), 
        ]
