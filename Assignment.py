def draw_rectangle(x, y, length, height):
    if -400 <= x <= 400 and -400 <= y <= 400 and -400 <= length <= 400 and -400 <= height <= 400:
        return 1
    else:
        return 2


def main():
    xcor=int(input("x-axis"))
    ycor=int(input("y-axis"))
    length=int(input("Enter Length"))
    height=int(input("Enter Height"))
    
    print(draw_rectangle(xcor,ycor,length,height))

if _name_=="_main_":
    main()





import turtle
turtle.bgcolor("purple")

def draw_shape(shape, color_code, x, y, length, height=0):
    if shape=="r":
        if x+length <=400 and y+height <=400:
            turtle.up()
            turtle.goto(x,y)
            turtle.fillcolor(color_code)
            turtle.begin_fill()
            turtle.down()

            for i in range(1, 3):
                turtle.forward(100)
                turtle.left(90)
            
            turtle.up()
            turtle.goto(0, 400)
            return color_code
        
        else:
            return 0 
    elif shape=="c":
            if height <=400:
                turtle.up()
                turtle.goto(x, y)
                turtle.left(180)
                turtle.fillcolor(color_code)
                turtle.begin_fill()
                turtle.forward(height)
                turlte.circle(height)
                turtle.end_fill()
                turtle.up()
                turtle.goto(0,400)
                turtle.left(180)
            else:
                return 0 
    elif shape=="t":
        turtle.up()
        turtle.fillcolor(color_code)
        turtle.goto(x, y)
        turtle.begin_fill()
        turtle.down()
        if height <=400:
            i=0
            while i<3:
                turtle.forward(height)
                turtle.left(120)
                i=i+1
        else:
            return 0
            turle.end_fill()

        draw_shape("r","yellow",250,200,300,180)
        draw_shape("c","blue", -10,0,300,95)
        draw_shape("t","cyan",-100,300,300,100)






         turtle.done()







    
