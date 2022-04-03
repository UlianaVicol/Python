

import turtle as t
# time data
hours = 4
minutes = 55
seconds = 5

t.bgcolor("black")
t.speed(0.3)

#print the time
def printTime():
    print( f"{hours:4}:{minutes:55}:{seconds:05}" )

# draw clock with turtle 
#################  VARIANTA I  ###################
def drawClock():
    t.pensize(5)
    t.penup()
    t.goto(0, 210)
    t.setheading(180)
    t.color("DarkTurquoise")
    t.pendown()
    #t.circle(210)

# drow the lines for the hour    
def drowLinesHour(): 
    t.penup()
    t.goto(0,0)
    t.setheading(90)
    for i in range(12):
        t.forward(190)
        t.pendown()
        t.forward(20)
        t.penup()
        t.goto(0,0)
        t.right(30)
        t.pensize(5)
    
# center dot
    t.color("white")
    t.forward(6)
    t.left(90)
    t.pendown()
    t.circle(6)


# hours indicator  
    t.penup()
    t.goto(0,0)
    t.color("white")
    t.setheading(90)
    t.right(hours * 30)
    t.pendown()
    t.forward(100)
    t.pensize(5)

# minutes indicator  
    t.penup()
    t.goto(0,0)
    t.color("yellow")
    t.setheading(90)
    t.right(minutes * 6)
    t.pendown()
    t.forward(120)
    t.pensize(3)

# seconds  indicator
    t.penup()
    t.goto(0,0)
    t.color("dark red")
    t.setheading(90) 
    t.right(seconds * 6)
    t.pendown()
    t.forward(140)
    t.pensize(1)

    t.exitonclick()  
    
    
################# VARIANTA I ###################   


################# VARIANTA II ###################
# draw clock with turtle
#def drawClock():
#    t.pensize(5)
#    t.color("DarkTurquoise")
#    t.circle(100)
#    t.left(90)
#    t.penup()
#    t.forward(100)
    
    # clock center dot
#    t.color("white")
#    t.forward(3)
#    t.left(90)
#    t.pendown()
#    t.circle(3)
    
    # reset the pen
#    t.penup()
#    t.right(90)
    
    # hours indicator
#    t.color("white")
#    t.pendown()
#    t.right(hours * 30)
#    t.forward(70)
    
    # reset the pen
#    t.penup()
#    t.left(180)
#    t.forward(70)
#    t.right(180-hours * 30)
    
    # minutes indicator
#    t.color("yellow")
#   t.pensize(2)
#    t.pendown()
#    t.right(minutes * 6)
#    t.forward(80)

    # reset the pen
#    t.pensize(1)
#    t.penup()
#    t.left(180)
#    t.forward(80)
#    t.right(180-minutes * 6)
  
    # seconds indicator
#    t.color("dark red")
#    t.pendown()
#    t.right(seconds * 6)
#    t.forward(90)
    
#    t.exitonclick()
    
################# VARIANTA II ###################
    



    
    
    
    
    




    
    
    
    
    
    
    
    
    
    












    

