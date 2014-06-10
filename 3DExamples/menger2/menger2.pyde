'''
A more complicated example with potential of Povray
export using a custom mesh class
'''

from box import Box
from arcball import ArcBall


angle = 0.0
X = 0
Y = 1
Z = 2
menger = []


def setup():
    size(800, 600, P3D)
    smooth(8)
    global arcball
    arcball = ArcBall(
        width / 2.0, height / 2.0, min(width - 20, height - 20) * 0.5)
    create_menger(0, 0, 0, height / 2.0)


def draw():
    background(0, 0, 200)
    lights()
    defineLights()
    translate(width / 2.0, height / 2.0)
    global menger
    update()
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


def create_menger(xx, yy, zz, sz):
    """
    Create a recursive menger sponge using my Cube class
    """
    global menger
    u = sz / 3.0
    if (sz < 20):
        menger.append(Box.createAcube(xx, yy, zz, sz).toMesh())
    else:
        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    if ((abs(i) + abs(j) + abs(k)) > 1):
                        create_menger(
                            xx + (i * u), yy + (j * u), zz + (k * u), u)


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


def keyPressed():
    """
    Important gotcha coming from regular processing
    key.char not key to compare key characters, fix axis
    of rotation by holding down key corresponding to axis
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

