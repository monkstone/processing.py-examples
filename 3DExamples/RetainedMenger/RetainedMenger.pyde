##########################
# RetainedMenger.py
# (processing-2.0)
# author Martin Prout
##########################

from arcball import ArcBall

MIN_SIZE = 20
X = 0
Y = 1
Z = 2

def setup():
    """
    processing.py setup
    """  
    size(640, 480, P3D)
    smooth(16)
    camera()
    global arcball, menger
    camera(width/2.0, height/2.0, (height/2.0) / tan(PI*30.0 / 180.0), 0, 0, 0, 0, 1, 0)
    arcball = ArcBall(0, 0, min(width - 20, height - 20) * 0.5)
    menger = createShape(PShape.GROUP)
    createMenger(0, 0, 0, height * 0.8)
    
def draw():
    """
    processing.py draw loop
    """	 
    background(20, 20, 200)
    noStroke()
    lights()
    update()
    defineLights()
    render()
    
    
def render():
    """
    Render encapsulated as a method
    """  
    menger.setAmbient(50)	
    menger.setSpecular(30)	
    shape(menger)
    
def createMenger(xx, yy, zz, sz):
    """
    Recursively create a smaller instance of menger (1/3 smaller)
    Only the terminal cubes are added to menger when size < min size
    If you are new to python note non inclusive range()
    """
    u = sz / 3.0
    if (sz < MIN_SIZE) : # recursion limited by minimum cube size
        noStroke()
        menger.addChild(createCube(xx, yy, zz, sz)) # create and add a cube	 
    else:
        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    if ((abs(i) + abs(j) + abs(k)) > 1) :
                        createMenger(xx + (i * u), yy + (j * u), zz + (k * u), u)
                        
def createCube(xx, yy, zz, sz):
    """
    Create and return a unit cube PShape instance
    """
    dim = sz / 2.0
    cube = createShape()
    cube.beginShape(QUADS)
    # Front face
    cube.fill(255)
    cube.normal(0, 0, 1)
    cube.vertex(-dim + xx, -dim + yy, -dim + zz)
    cube.vertex(+dim + xx, -dim + yy, -dim + zz)
    cube.vertex(+dim + xx, +dim + yy, -dim + zz)
    cube.vertex(-dim + xx, +dim + yy, -dim + zz)
    
    # Back face
    
    cube.normal(0, 0, -1)
    cube.vertex(-dim + xx, -dim + yy, +dim + zz)
    cube.vertex(+dim + xx, -dim + yy, +dim + zz)
    cube.vertex(+dim + xx, +dim + yy, +dim + zz)
    cube.vertex(-dim + xx, +dim + yy, +dim + zz)
    
    # Left face
    
    cube.normal(1, 0, 0)
    cube.vertex(-dim + xx, -dim + yy, -dim + zz)
    cube.vertex(-dim + xx, -dim + yy, +dim + zz)
    cube.vertex(-dim + xx, +dim + yy, +dim + zz)
    cube.vertex(-dim + xx, +dim + yy, -dim + zz)
    
    # Right face
    
    cube.normal(-1, 0, 0)
    cube.vertex(+dim + xx, -dim + yy, -dim + zz)
    cube.vertex(+dim + xx, -dim + yy, +dim + zz)
    cube.vertex(+dim + xx, +dim + yy, +dim + zz)
    cube.vertex(+dim + xx, +dim + yy, -dim + zz)
    
    # Top face
    
    cube.normal(0, 1, 0)
    cube.vertex(-dim + xx, -dim + yy, -dim + zz)
    cube.vertex(+dim + xx, -dim + yy, -dim + zz)
    cube.vertex(+dim + xx, -dim + yy, +dim + zz)
    cube.vertex(-dim + xx, -dim + yy, +dim + zz)
    
    # Bottom face
    
    cube.normal(0, -1, 0)
    cube.vertex(-dim + xx, +dim + yy, -dim + zz)
    cube.vertex(+dim + xx, +dim + yy, -dim + zz)
    cube.vertex(+dim + xx, +dim + yy, +dim + zz)
    cube.vertex(-dim + xx, +dim + yy, +dim + zz)
    cube.endShape()
    return cube
  
  
def defineLights():
    """
    Method sets up lights
    """
    pointLight(150, 100, 0, 200, -150, 0) 
    directionalLight(0, 102, 255, 1, 0, 0) 
    spotLight(255, 255, 109, 0, 40, 200, 0, -0.5, -0.5, PI / 2, 2)	

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
