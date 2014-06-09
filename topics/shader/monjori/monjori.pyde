monjori = None


def setup():
    size(640, 360, P2D)
    noStroke()
    global monjori
    monjori = loadShader("monjori.glsl")
    monjori.set("resolution", float(width), float(height))


def draw():
    monjori.set("time", millis() / 1000.0)
    shader(monjori)
    # The rect is needed to make the fragment shader go through every pixel of
    # the screen, but is not used for anything else since the rendering is entirely
    # generated by the shader.
    fill(0)
    rect(0, 0, width, height)
