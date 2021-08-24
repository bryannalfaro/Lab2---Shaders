import struct
from gl import color

class Texture(object):
    def __init__(self,path):
        self.path = path
        self.pixels = []
        self.read()

    def read(self):
        image = open(self.path,'br')
        image.seek(10)
        val = image.read(4)
        header_size = struct.unpack('=l',val)[0]
        image.seek(18)
        self.width = struct.unpack('=l',image.read(4))[0]
        self.height = struct.unpack('=l',image.read(4))[0]
        image.seek(header_size)

        for y in range(self.height):
            self.pixels.append([])
            for x in range(self.width):
                b= ord(image.read(1))
                g= ord(image.read(1))
                r= ord(image.read(1))
                self.pixels[y].append(color(r,g,b))
        image.close()

    def get_color(self,tx,ty):
        x = round(tx*self.width)-1
        y = round(ty*self.height)-1
        return self.pixels[y][x]

