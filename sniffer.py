import socket, struct, os, sys, signal, select
from ctypes import * 

PROTOCOLS = {
        1 : "ICMP",
        6 : "TCP",
        17: "UDP",}

s = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

class IP(Structure):
    _fields_ = [("ip_hl" , c_ubyte, 4), 
                ("ip_ver"  , c_ubyte, 4), 
                ("ip_tos", c_ubyte),    
                ("ip_len", c_ushort),   
                ("ip_id" , c_ushort),   
                ("ip_off", c_ushort),   
                ("ip_ttl", c_ubyte),    
                ("ip_proto"  , c_ubyte),    
                ("ip_sum", c_ushort),   
                ("ip_src", c_uint32),
                ("ip_dst", c_uint32)]   

    def __new__(self, buf=None):
        return self.from_buffer_copy(buf)
    
    def __init__(self, buf=None):
        
        self.src_address=socket.inet_ntoa(struct.pack("@I",self.ip_src))
        self.dst_address=socket.inet_ntoa(struct.pack("@I",self.ip_dst))
        
        try:
            self.proto = PROTOCOLS[self.ip_proto]
        except KeyError:
            print("{}Protocol Defining error.".format(self.ip_proto))
            socket.close()
            
print("Listning to the packets...")


try:
    while True:
        buf = s.recvfrom(65535)[0]
        ip_header = IP(buf[:20])
        print("SRC : " +ip_header.dst_address + " \t\tDES : "+ ip_header.src_address + "\t\tPROTOCOL : " + ip_header.proto)
except KeyboardInterrupt:
    print("\nSniffing cancled by user.")
    s.close()
