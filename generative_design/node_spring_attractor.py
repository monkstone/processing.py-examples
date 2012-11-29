import generativedesign.Node as Node
import generativedesign.Spring as Spring
import generativedesign.Attractor as Attractor

"""
part of the example files of the generativedesign library. 
shows how to use the classes Node, Spring and Attractor in 3d space.
"""

def setup():
    """
    Setup Sketch smooth should be called here
    """
    size(512, 512, P3D)
    lights()
    global nodeA, nodeB, attractor, spring
    smooth(8)
    fill(0)
    nodeA = Node(random(width), random(height), random(-200, 200))
    nodeB = Node(random(width), random(height), random(-200, 200))
    nodeA.setStrength(-2)
    nodeB.setStrength(-2)
    nodeA.setDamping(0.1)
    nodeB.setDamping(0.1)
    nodeA.setBoundary(0, 0, -300, width, height, 300)
    nodeB.setBoundary(0, 0, -300, width, height, 300)
    
    spring = Spring(nodeA, nodeB)
    spring.setStiffness(0.7)
    spring.setDamping(0.9)
    spring.setLength(100)
    
    attractor = Attractor(width/2, height/2, 0)
    attractor.setMode(Attractor.SMOOTH)
    attractor.setRadius(200)
    attractor.setStrength(5)


def draw():
    """
    The processing draw loop
    """
    background(50, 50, 200)
    lights()
    ambientLight(100, 100, 100)
    ambient(30)
    specular(30)
    if (mousePressed == True):
        nodeA.x = mouseX
        nodeA.y = mouseY
        nodeA.z = mouseY - 256
    # attraction between nodes
    nodeA.attract(nodeB)
    nodeB.attract(nodeA)
    # update spring
    spring.update()
    # attract
    attractor.attract(nodeA)
    attractor.attract(nodeB)
    # update node positions
    nodeA.update()
    nodeB.update()
    # draw attractor
    stroke(0, 50)
    strokeWeight(1)
    noFill()
    line(attractor.x-10, attractor.y, attractor.x+10, attractor.y)
    line(attractor.x, attractor.y-10, attractor.x, attractor.y+10)
    ellipse(attractor.x, attractor.y, attractor.radius*2, attractor.radius*2)
    # draw spring
    stroke(255, 0, 0, 255)
    strokeWeight(4)
    line(nodeA.x, nodeA.y, nodeA.z, nodeB.x, nodeB.y, nodeB.z)
    # draw nodes
    noStroke()
    fill(212)
    pushMatrix()
    translate(nodeA.x, nodeA.y, nodeA.z)
    sphere(20)
    popMatrix()
    pushMatrix()
    translate(nodeB.x, nodeB.y, nodeB.z)
    sphere(20)
    popMatrix()
