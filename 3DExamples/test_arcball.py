from arcball.arcball import ArcBall

"""
test_arcball.py by Martin Prout a processing.py sketch
Sketch features the use of ArcBall class, provides intuitive manipulation of sketch object
ArcBall class uses Quaternions class for efficient calculation of rotation, hold down x, y or z
keys to constrain rotation to that plane otherwise drag mouse for smooth rotation
"""
X = 0
Y= 1
Z = 2

def setup():
    size(600, 600, P3D)
    global arcball
    arcball = ArcBall(width/2.0, height/2.0, min(width - 20, height - 20) * 0.5)

def draw():
    background(0xff66c0ff)
    translate(width/2.0, height/2.0, -height/4.0)
    defineLights()
    update()
    lights()
    stroke(0)
    cube(arcball.radius)
    
def update():
    """
    wrap arcball update and rotation as a local function
    """
    theta, x, y, z = arcball.update()
    rotate(theta, x, y, z)    

def mousePressed():
    arcball.mousePressed(mouseX, mouseY)
  
def mouseDragged():
    arcball.mouseDragged(mouseX, mouseY) 

def defineLights():
    """
    Light up the cube
    """
    ambientLight(50, 50, 50)
    pointLight(150, 100, 0, 200, -150, 0)
    directionalLight(0, 102, 255, 1, 0, 0)
    spotLight(255, 255, 109, 0, 40, 200, 0, -0.5, -0.5, PI / 2, 2)

def keyPressed():
    """
    Important gotcha coming from regular processing
    key was not char, fixed in recent versions?
    Contstrain axis of rotation by holding down key 
    corresponding to axis
    """
    # print key # to test if fixed
    #if (key == 120):
    if (key == 'x'):  # if fixed
        arcball.selectAxis(X)
    #if (key == 121):
    if (key == 'y'):  # if fixed  
        arcball.selectAxis(Y)
    #if (key == 122):
    if (key == 'z'):  # if fixed 
        arcball.selectAxis(Z)

def keyReleased():
    """
    Release axis constraint
    """
    arcball.selectAxis(-1)

def cube(sz):
    sz *= 0.5  
    fill(200,  200,  200,  255) 
    beginShape(QUADS)
    vertex(-sz, -sz, -sz)
    vertex(+sz, -sz, -sz)
    vertex(+sz, +sz, -sz)
    vertex(-sz, +sz, -sz)
    vertex(-sz, -sz, +sz)
    vertex(+sz, -sz, +sz)
    vertex(+sz, +sz, +sz)
    vertex(-sz, +sz, +sz)
    vertex(-sz, -sz, -sz)
    vertex(-sz, -sz, +sz)
    vertex(-sz, +sz, +sz)
    vertex(-sz, +sz, -sz)
    vertex(+sz, -sz, -sz)
    vertex(+sz, -sz, +sz)
    vertex(+sz, +sz, +sz)
    vertex(+sz, +sz, -sz)
    vertex(-sz, -sz, -sz)
    vertex(+sz, -sz, -sz)
    vertex(+sz, -sz, +sz)
    vertex(-sz, -sz, +sz)
    vertex(-sz, +sz, -sz)
    vertex(+sz, +sz, -sz)
    vertex(+sz, +sz, +sz)
    vertex(-sz, +sz, +sz)
    endShape()


