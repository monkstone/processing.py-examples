add_library('GenerativeDesign')

import generativedesign.Mesh as Mesh

"""
part of the example files of the generativedesign library.
shows how to use the mesh class, if you want to define your own forms.
Modified to run in python mode in processing ide
"""

def setup():
    """
    Setup the drawing style
    """
    size(1000, 1000, P3D)    
    colorMode(HSB, 360, 100, 100, 100)
    noStroke()
    global myMesh
    myMesh = MyOwnMesh(this)
    myMesh.setUCount(100)
    myMesh.setVCount(100)
    myMesh.setColorRange(193, 193, 30, 30, 85, 85, 100)
    myMesh.update()

def draw():
    """
    The processing draw loop
    """
    background(255)    
    # setup lights
    colorMode(RGB, 255, 255, 255, 100)
    lightSpecular(255, 255, 255) 
    directionalLight(255, 255, 255, 1, 1, -1) 
    shininess(5.0)
    # setup view    
    translate(width/2, height/2)
    scale(180)
    myMesh.draw()    


class MyOwnMesh(Mesh):
    """
    A custom python class that extend the original Mesh class
    """
    
    def __init__(self, theParent):
        Mesh.__init__(self, theParent)
        
        
    # just override this function and put your own formulas inside
    def calculatePoints(self, u,  v):
        A = 2/3.0
        B = sqrt(2)      
        x = A *  (cos(u) * cos(2 * v) + B * sin(u) * cos(v)) * cos(u) / (B - sin(2 * u) * sin(3 * v))
        y = A * (cos(u) * sin(2 * v) - B * sin(u) * sin(v)) * cos(u) / (B - sin(2 * u) * sin(3 * v))
        z = B * cos(u) * cos(u) / (B - sin(2 * u) * sin(3 * v))
        return PVector(x, y, z)
