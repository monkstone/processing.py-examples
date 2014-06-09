from arcball import ArcBall

"""
test_arcball.py by Martin Prout a processing.py sketch
Sketch features the use of ArcBall class, provides intuitive manipulation of sketch object
ArcBall class uses Quaternions class for efficient calculation of rotation, hold down x, y or z
keys to constrain rotation to that plane otherwise drag mouse for smooth rotation
"""
X = 0
Y = 1
Z = 2

def setup():
    """
    processing.py setup
    """
    size(800, 600, P3D)
    smooth(16)
    global arcball, my_cube
    camera(width/2.0, height/2.0, (height/2.0) / tan(PI*30.0 / 180.0), 0, 0, 0, 0, 1, 0)
    arcball = ArcBall(0, 0, height * 0.7)
    my_cube = createShape(PShape.BOX, [arcball.radius]  * 3)

def draw():
    """
    processing.py draw loop
    """
    background(0xff66c0ff)
    defineLights()
    update()
    lights()
    my_cube.setAmbient(50)	
    my_cube.setSpecular(30)	
    shape(my_cube)
    
    
def update():
    """
    wrap arcball update and rotation as a local function
    """
    theta, x, y, z = arcball.update()
    rotate(theta, x, y, z)    

def mousePressed():
    """
    for arcball manipulation
    """
    arcball.mousePressed(mouseX, mouseY)
  
def mouseDragged():
    """
    for arcball manipulation
    """
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
    Constrain axis of rotation by holding down key 
    corresponding to axis
    """
    if (key == 'x'):  
        arcball.selectAxis(X)
    if (key == 'y'):  
        arcball.selectAxis(Y)
    if (key == 'z'):  
        arcball.selectAxis(Z)

def keyReleased():
    """
    Release axis constraint
    """
    arcball.selectAxis(-1)
