from collections import namedtuple

V3 = namedtuple("Point3D",['x','y','z'])

def cross(v0,v1):
        cx = v0.y*v1.z-v0.z*v1.y
        cy = v0.z*v1.x-v0.x*v1.z
        cz = v0.x*v1.y-v0.y*v1.x

        return V3(cx,cy,cz)

def sub(v0,v1):
    return V3(v0.x-v1.x,v0.y-v1.y,v0.z-v1.z)

def length(v0):
    return (v0.x**2+v0.y**2+v0.z**2)**0.5

def norm(v0):
    l = length(v0)
    if l == 0:
        return V3(0,0,0)
    return V3(v0.x/l, v0.y/l, v0.z/l)

def dot(v0,v1):
    return(v0.x*v1.x + v0.y*v1.y + v0.z*v1.z)