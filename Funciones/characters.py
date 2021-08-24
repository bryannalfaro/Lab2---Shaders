import struct

def char(c):
    return struct.pack('=c',c.encode('ascii'))

def word(w):
    #short
    return struct.pack('=h',w)

def dword(d):
    #long
    return struct.pack('=l',d)