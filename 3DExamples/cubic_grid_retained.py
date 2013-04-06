# CubicGridRetained
#
# You may need to increase the maximum available memory in the
# by passing -mx1000m to jvm (in run script if you use that)
#
BOX_SIZE = 20
MARGIN = BOX_SIZE * 2
DEPTH = 400
boxFill = None
grid = None
fcount = 0
lastm = 0
frate =  0
FINT = 3

def setup(): 
  size(640, 360, P3D)
  frameRate(60)
  noSmooth()
  noStroke()
  global grid
  grid = createShape(GROUP)

  # Build grid using multiple 
  for i in range(-DEPTH / 2 + MARGIN, DEPTH / 2 - MARGIN, BOX_SIZE):
    for j in range(-height + MARGIN, height - MARGIN, BOX_SIZE):
      for k in range(-width + MARGIN,  width - MARGIN, BOX_SIZE):
        # Base fill color on counter values, abs function
        # ensures values stay within legal range
        boxFill = color(abs(i), abs(j), abs(k), 50) 
        cube = createShape(BOX, [BOX_SIZE] * 3)
        cube.setFill(boxFill)
        cube.translate(k, j, i)
        grid.addChild(cube)

def draw(): 
  background(255)

  hint(DISABLE_DEPTH_TEST)

  # Center and spin grid
  pushMatrix()
  translate(width / 2, height / 2, -DEPTH)
  rotateY(frameCount * 0.01)
  rotateX(frameCount * 0.01)
  global grid
  shape(grid)
  popMatrix()

  hint(ENABLE_DEPTH_TEST)
  global fcount, lastm, frate
  fcount += 1
  m = millis()
  if (m - lastm > 1000 * FINT): 
    frate = float(fcount) / FINT
    fcount = 0
    lastm = m
    print("fps: %d" %  frate)
  
  fill(0)
  text("fps: %d" %  frate, 10, 20)

