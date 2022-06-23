import turtle
from turtle import *


title("Pyramid Project")
speed(50)

bgcolor("#1C97D6")
screensize(canvwidth=1366, canvheight=968)

#screen area
penup()
goto(-783,10)
pendown()
begin_fill()
color("limegreen")
for i in range(4):
    fd(1566)
    rt(90)
end_fill()

#first pyramid
penup()
goto(600,10)
pendown()
color("#692810")
begin_fill()
for i in range(3):
    lt(120)
    fd(350)
end_fill()

#second part
penup()
goto(600,10)
pendown()
begin_fill()

color("#915F0D")
lt(120)
fd(350)
lt(130)
fd(323)
lt(110)
fd(290)
end_fill()




#2nd pyramid
penup()
goto(400,10)
pendown()
color("#692810")
begin_fill()
for i in range(3):
    lt(120)
    fd(450)
end_fill()

#2nd part
penup()
goto(400,10)
pendown()
begin_fill()

color("#B26D10")
lt(120)
fd(450)
lt(130)
fd(415)
lt(110)
fd(375)
end_fill()

#3rd pyramid
penup()
goto(100,10)
pendown()
color("#692810")
begin_fill()
for i in range(3):
    lt(120)
    fd(350)
end_fill()

#3rd part
penup()
goto(100,10)
pendown()
begin_fill()

color("#995D0E")
lt(120)
fd(350)
lt(130)
fd(323)
lt(110)
fd(290)
end_fill()
#end------------/////////////////////////////////////////////////////////-pyramid


#star
begin_fill()
color("#55DAF5")
penup()
goto(-583,450)
pendown()
begin_fill()
for i in range(4):
    rt(144)
    fd(50)
end_fill()

penup()
goto(-483,430)
pendown()
begin_fill()
for i in range(4):
    rt(144)
    fd(50)
end_fill()

penup()
goto(-180,450)
pendown()
begin_fill()
for i in range(4):
    rt(144)
    fd(50)
end_fill()

penup()
goto(-90,440)
pendown()
begin_fill()
for i in range(4):
    rt(144)
    fd(50)
end_fill()

penup()
goto(-643,420)
pendown()
begin_fill()
for i in range(4):
    rt(144)
    fd(50)
end_fill()

penup()
goto(-303,460)
pendown()
begin_fill()
for i in range(4):
    rt(144)
    fd(50)
end_fill()

penup()
goto(-383,440)
pendown()
begin_fill()
for i in range(4):
    rt(144)
    fd(50)
end_fill()

penup()
goto(-300,460)
pendown()
begin_fill()
for i in range(4):
    rt(144)
    fd(50)
end_fill()

penup()
goto(-200,470)
pendown()
begin_fill()
for i in range(4):
    rt(144)
    fd(50)
end_fill()

penup()
goto(-103,430)
pendown()
begin_fill()
for i in range(4):
    rt(144)
    fd(50)
end_fill()

penup()
goto(-50,450)
pendown()
begin_fill()
for i in range(4):
    rt(144)
    fd(50)
end_fill()

penup()
goto(0,450)
pendown()
begin_fill()
for i in range(4):
    rt(144)
    fd(50)
end_fill()

penup()
goto(50,460)
pendown()
begin_fill()
for i in range(4):
    rt(144)
    fd(50)
end_fill()

penup()
goto(270,430)
pendown()
begin_fill()
for i in range(4):
    rt(144)
    fd(50)
end_fill()

penup()
goto(353,440)
pendown()
begin_fill()
for i in range(4):
    rt(144)
    fd(50)
end_fill()

penup()
goto(690,460)
pendown()
begin_fill()
for i in range(4):
    rt(144)
    fd(50)
end_fill()

penup()
goto(540,470)
pendown()
begin_fill()
for i in range(4):
    rt(144)
    fd(50)
end_fill()

penup()
goto(403,430)
pendown()
begin_fill()
for i in range(4):
    rt(144)
    fd(50)
end_fill()


penup()
goto(598,450)
pendown()
begin_fill()
for i in range(4):
    rt(144)
    fd(50)
end_fill()

penup()
goto(483,430)
pendown()
begin_fill()
for i in range(4):
    rt(144)
    fd(50)
end_fill()

penup()
goto(643,400)
pendown()
begin_fill()
for i in range(4):
    rt(144)
    fd(50)
end_fill()

end_fill()


#circle
penup()
goto(405,360)
pendown()
color("#FFF2F6")
begin_fill()
for i in range(4):
    rt(144)
    fd(60)
end_fill()

penup()
goto(190,420)
pendown()
color("#FFF")
begin_fill()
for i in range(4):
    rt(144)
    fd(65)
end_fill()

penup()
goto(-75,380)
pendown()
color("#FFF2F6")
begin_fill()
for i in range(4):
    rt(144)
    fd(60)
end_fill()

#tree

penup()
goto(-583,10)
pendown()
color("#177205")
begin_fill()
pensize(5)
lt(-126)

def tree(size):
    if size < 10:
        return
    fd(size)
    lt(30)
    tree(size * 0.6)
    rt(60)
    tree(size * 0.6)
    lt(30)
    bk(size)
tree(120)
end_fill()



turtle.done()