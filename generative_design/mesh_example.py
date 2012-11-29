import generativedesign.Mesh as Mesh


"""
part of the example files of the generativedesign library.
Modified to run with processing.py
"""

def setup():
	"""
	Setup the drawing style
	"""
	size(1000,1000,P3D)	
	# setup drawing style 
	background(255)
	noStroke()
	fill(0)	
	# setup lights
	lightSpecular(230, 230, 230) 
	directionalLight(200, 200, 200, 0.5, 0.5, -1) 
	specular(color(220)) 
	shininess(5.0) 
	# setup view
	translate(width*0.5, height*0.5)
	rotateX(-0.2) 
	rotateY(-0.5) 
	scale(100)	
	# setup Mesh, set colors and draw  
	myMesh = Mesh(this, Mesh.STEINBACHSCREW, 200, 200, -3.0, 3.0, -PI, PI)
	myMesh.setColorRange(200, 200, 50, 50, 40, 40, 100)
	myMesh.draw()


def draw():
	"""
	The processing draw loop
	"""
	pass
