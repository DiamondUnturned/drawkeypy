
yaslon = 0

def setup():
    size(800,600)
    background(100)
    
def draw():
    global yaslon
    if keyPressed:
        if key == "e" or key == "E" or key == u"у" or key == u"У":
            fill(0,0,0)
            stroke(0,0,0)
            ellipse(mouseX,mouseY,40,40) 
            
        if key == "r" or key == "R" or key == u"к" or key == u"К":
            fill(200,56,0)
            stroke(200,56,0)
            ellipse(mouseX,mouseY,40,40)
            
        if key == "c" or key == "C" or key == u"с" or key == u"С":    
            background(100) 
            
