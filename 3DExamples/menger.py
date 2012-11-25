from arcball.arcball import ArcBall
from arcball.box import Box

FOV = PI/3.0
angle = 0.0
ANGLE_STEP = PI / 180.0
menger = []
 

def setup():
    size(800,600, P3D)
    global arcball
    camera(width/2.0, height/2.0, (height/2.0) / tan(PI*30.0 / 180.0), 0, 0, 0, 0, 1, 0)
    arcball = ArcBall(0, 0, height * 0.6)
    
    
def draw():
    background(0,  0,  200)
    lights()
    defineLights()    
    update()
    create_menger(0, 0, 0, arcball.radius)

def create_menger(xx, yy, zz, sz):
    """
    Create a recursive menger sponge using my Cube class
    """
    global menger	
    u = sz / 3.0
    if (sz < 50):
        my_cube(xx, yy, zz, sz)
    else:
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                for k in range(-1, 2, 1):
                    if ((abs(i) + abs(j) + abs(k)) > 1):
                        create_menger(xx + (i * u), yy + (j * u), zz + (k * u), u)
                        
def my_cube(xx,  yy,  zz,  sz):
    """
    Draw a cube with centre xx, yy, zz and size sz
    """
    beginShape(QUADS)
    normal(0, 0, 1)
    vertex(-sz / 2.0 + xx, -sz / 2.0 + yy, -sz / 2.0 + zz)
    vertex(+sz / 2.0 + xx, -sz / 2.0 + yy, -sz / 2.0 + zz)
    vertex(+sz / 2.0 + xx, +sz / 2.0 + yy, -sz / 2.0 + zz)
    vertex(-sz / 2.0 + xx, +sz / 2.0 + yy, -sz / 2.0 + zz)
    
    #Back face    
    normal(0, 0, -1)
    vertex(-sz / 2.0 + xx, -sz / 2.0 + yy, +sz / 2.0 + zz)
    vertex(+sz / 2.0 + xx, -sz / 2.0 + yy, +sz / 2.0 + zz)
    vertex(+sz / 2.0 + xx, +sz / 2.0 + yy, +sz / 2.0 + zz)
    vertex(-sz / 2.0 + xx, +sz / 2.0 + yy, +sz / 2.0 + zz)
    
    #Left face    
    normal(1, 0, 0)
    vertex(-sz / 2.0 + xx, -sz / 2.0 + yy, -sz / 2.0 + zz)
    vertex(-sz / 2.0 + xx, -sz / 2.0 + yy, +sz / 2.0 + zz)
    vertex(-sz / 2.0 + xx, +sz / 2.0 + yy, +sz / 2.0 + zz)
    vertex(-sz / 2.0 + xx, +sz / 2.0 + yy, -sz / 2.0 + zz)
    
    #Right face    
    normal(-1, 0, 0)
    vertex(+sz / 2.0 + xx, -sz / 2.0 + yy, -sz / 2.0 + zz)
    vertex(+sz / 2.0 + xx, -sz / 2.0 + yy, +sz / 2.0 + zz)
    vertex(+sz / 2.0 + xx, +sz / 2.0 + yy, +sz / 2.0 + zz)
    vertex(+sz / 2.0 + xx, +sz / 2.0 + yy, -sz / 2.0 + zz)
    
    #Top face    
    normal(0, 1, 0)
    vertex(-sz / 2.0 + xx, -sz / 2.0 + yy, -sz / 2.0 + zz)
    vertex(+sz / 2.0 + xx, -sz / 2.0 + yy, -sz / 2.0 + zz)
    vertex(+sz / 2.0 + xx, -sz / 2.0 + yy, +sz / 2.0 + zz)
    vertex(-sz / 2.0 + xx, -sz / 2.0 + yy, +sz / 2.0 + zz)
    
    #Bottom face    
    normal(0, -1, 0)
    vertex(-sz / 2.0 + xx, +sz / 2.0 + yy, -sz / 2.0 + zz)
    vertex(+sz / 2.0 + xx, +sz / 2.0 + yy, -sz / 2.0 + zz)
    vertex(+sz / 2.0 + xx, +sz / 2.0 + yy, +sz / 2.0 + zz)
    vertex(-sz / 2.0 + xx, +sz / 2.0 + yy, +sz / 2.0 + zz)
    endShape()                        
                    
def defineLights():
    """
    Without lights you wouldn't see the menger
    """
    ambient(20, 20, 20)
    ambientLight(50, 50, 50)
    pointLight(30, 30, 30, 200, -150, 0)
    directionalLight(0, 30, 50, 1, 0, 0)
    spotLight(30, 30, 30, 0, 40, 200, 0, -0.5, -0.5, PI / 2, 2)     
 
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

    




