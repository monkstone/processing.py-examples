from arcball.arcball import ArcBall
from arcball.box import Box

FOV = PI/3.0
angle = 0.0
ANGLE_STEP = PI / 180.0
menger = []
 

def setup():
    size(800,600, P3D)
    global arcball
    arcball = ArcBall(width/2.0, height/2.0, min(width - 20, height - 20) * 0.5)
    create_menger(0, 0, 0, height/2.0)
    
def draw():
    background(0,  0,  200)
    lights()
    defineLights()    
    translate(width/2.0, height/2.0)
    update()
#    export(menger)
    for cub in menger:
        draw_cube(cub)
    print(frameRate)

def draw_cube(cube):
    """
    Draw a cube with centre xx, yy, zz and size sz
    """
    noStroke()
    beginShape(TRIANGLES)
    for vec in cube.mesh_array():
        vertex(vec.x, vec.y, vec.z)
    endShape()
    
def export(menger):
    f = open("menger.inc", 'w')
    f.write("#declare mesh_objects = union{\n")
    for cub in menger: 
        f.write(cub.mesh2())
    f.write("}\n")        
    f.close()
    exit(0)
    

def create_menger(xx, yy, zz, sz):
    """
    Create a recursive menger sponge using my Cube class
    """
    global menger	
    u = sz / 3.0
    if (sz < 50):
        menger.append(Box.createAcube(xx, yy, zz, sz).toMesh())
    else:
        for i in xrange(-1, 2, 1):
            for j in xrange(-1, 2, 1):
                for k in xrange(-1, 2, 1):
                    if ((abs(i) + abs(j) + abs(k)) > 1):
                        create_menger(xx + (i * u), yy + (j * u), zz + (k * u), u)
                    
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

    




