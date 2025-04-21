import socket
import struct
import binascii

class Iphdr:
    def __init__(self, srcport, dstport, tot_len, checksum):
        self.tot_len = tot_len
        self.checksum = checksum
        self.srcport = srcport
        self.dstport = dstport
        
    def pack_Iphdr(self):
        packed = b''
        packed += struct.pack('!H', self.srcport)
        packed += struct.pack('!H', self.dstport)
        packed += struct.pack('!H', self.tot_len)
        packed += struct.pack('!H', self.checksum)
        return packed

ip = Iphdr(5555, 80, 1000, 0xFFFF)
packed_iphdr = ip.pack_Iphdr()
print(binascii.b2a_hex(packed_iphdr))
        