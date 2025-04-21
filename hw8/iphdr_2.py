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

def unpack_Iphdr(buffer):
    unpacked = struct.unpack("!HHHH", buffer[:8])
    return unpacked

def getSrcPort(unpacked_ipheader):
    return unpacked_ipheader[0]

def getDstPort(unpacked_ipheader):
    return unpacked_ipheader[1]

def getLenght(unpacked_ipheader):
    return unpacked_ipheader[2]

def getChecksum(unpacked_ipheader):
    return unpacked_ipheader[3]

ip = Iphdr(5555, 80, 1000, 0xFFFF)
packed_iphdr = ip.pack_Iphdr()
print(binascii.b2a_hex(packed_iphdr))

unpack_Iphdr = unpack_Iphdr(packed_iphdr)
print(unpack_Iphdr)
print('Source port: {} Destination port:{} Length:{} Checksum:{}'
      .format(getSrcPort(unpack_Iphdr), getDstPort(unpack_Iphdr), getLenght(unpack_Iphdr), getChecksum(unpack_Iphdr),))