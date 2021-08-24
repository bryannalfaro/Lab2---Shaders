'''
Universidad del Valle de Guatemala
Graficas por computadora - Bryann Alfaro
SR4 - Flat Shading
'''
from gl import Renderer
from textures import Texture

r =  Renderer()
r.glInit()
r.glCreateWindow(800,600)
r.glClear()
r.customBackground()

r.load('./modelos/spherelab.obj',(1.5,1,0),(300,300,400))
r.glFinish("./salidas/textura.bmp")
