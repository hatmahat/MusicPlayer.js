from graphics import *
import math

win = GraphWin("Pemetaan PIR (Passive Infra Red)", 800, 800)
win.setCoords(-800,-800,800,800)
win.setBackground("black")

# Sudut
sudut = Text(Point(-700, 750), "Sudut")
sudut.setTextColor("white")
sudut.draw(win)

# Jarak
jarak = Text(Point(-500, 750), "Jarak(m)")
jarak.setTextColor("white")
jarak.draw(win)

# Derajat2
count0 = 0
for i in range(750-60, (750-660), -60):
    derajat = ["6", "10", "20", "30", "40", "50", "60", "70", "80", "90"]
    warna = [
        #6 
        color_rgb(168, 50, 50),
        #10 
        color_rgb(168, 97, 50),
        #20
        color_rgb(168, 139, 50),
        #30
        color_rgb(168, 166, 50),
        #40
        color_rgb(39, 168, 50),
        #50
        color_rgb(85, 168, 50),
        #60
        color_rgb(50, 168, 158),
        #70
        color_rgb(50, 119, 168),
        #80
        color_rgb(0, 52, 168),
        #90
        color_rgb(140, 50, 168)
    ]
    sudutSudut = Text(Point(-700, i), derajat[count0] + " derajat")
    sudutSudut.setTextColor(warna[count0])
    sudutSudut.draw(win)
    count0 += 1

# Entry Jarak 6 derajat
der6 = Entry(Point(-500,750-60), 5)
der6.setText("0.0")
der6.draw(win)

# Entry Jarak 10 derajat 
der10 = Entry(Point(-500,750-60*2),5)
der10.setText("0.0")
der10.draw(win)

# Entry Jarak 20 derajat
der20 = Entry(Point(-500,750-60*3),5)
der20.setText("0.0")
der20.draw(win)

# Entry Jarak 30 derajat
der30 = Entry(Point(-500,750-60*4),5)
der30.setText("0.0")
der30.draw(win)

# Entry Jarak 40 derajat
der40 = Entry(Point(-500,750-60*5),5)
der40.setText("0.0")
der40.draw(win)

# Entry Jarak 50 derajat
der50 = Entry(Point(-500,750-60*6),5)
der50.setText("0.0")
der50.draw(win)

# Entry Jarak 60 derajat
der60 = Entry(Point(-500,750-60*7),5)
der60.setText("0.0")
der60.draw(win)

# Entry Jarak 70 derajat
der70 = Entry(Point(-500,750-60*8),5)
der70.setText("0.0")
der70.draw(win)

# Entry Jarak 80 derajat
der80 = Entry(Point(-500,750-60*9),5)
der80.setText("0.0")
der80.draw(win)

# Entry Jarak 90 derajat
der90 = Entry(Point(-500,750-60*10),5)
der90.setText("0.0")
der90.draw(win)

# Garis Sumbu
yAxis = Line(Point(0,780),Point(0,-780))
yAxis.setOutline("white")
yAxis.draw(win)
xAxis = Line(Point(-780,0), Point(780,0))
xAxis.setOutline("white")
xAxis.draw(win)

# Circle background
for i in range(780, 0, -130):
    aCicle = Circle(Point(0,0), i)
    aCicle.setOutline("white")
    aCicle.draw(win)

# Draw Button
drawButton = Rectangle(Point(-700,750-60*11), Point(-500,750-60*12))
drawButton.setOutline("green")
drawButton.draw(win)
drawButtonText = Text(Point(-600,((750-60*11)+(750-60*12))/2), "DRAW")
drawButtonText.setTextColor("GREEN")
drawButtonText.draw(win)

# Mouse Click
posisi = win.getMouse()
print("X :" + str(posisi.getX()))
print("Y :" + str(posisi.getY()))
print("-------------------")
while (posisi.getX()<-700 or posisi.getX()>-500) or (posisi.getY()>90 or posisi.getY()<30):
    posisi = win.getMouse()
    print("X :" + str(posisi.getX()))
    print("Y :" + str(posisi.getY()))
    print("-------------------")
    
# Variables Jarak
floatDe6 = float(der6.getText())
floatDe10 = float(der10.getText())
floatDe20 = float(der20.getText())
floatDe30 = float(der30.getText())
floatDe40 = float(der40.getText())
floatDe50 = float(der50.getText())
floatDe60 = float(der60.getText())
floatDe70 = float(der70.getText())
floatDe80 = float(der80.getText())
floatDe90 = float(der90.getText())

# Lines
def pytaX(jarak, sudut):
    x = math.cos(math.pi*sudut/180)*jarak
    return x*100
def pytaY(jarak, sudut):
    y = math.sin(math.pi*sudut/180)*jarak
    return y*100

# Derajat 6
derajat6 = Line(Point(0,0), Point(pytaX(floatDe6,6),pytaY(floatDe6,6)))
derajat6.setFill(color_rgb(168, 50, 50))
derajat6.setWidth(2)
derajat6.draw(win)
derajat6_2 = Line(Point(0,0), Point(pytaX(floatDe6,6), -pytaY(floatDe6,6)))
derajat6_2.setWidth(2)
derajat6_2.setFill(color_rgb(168, 50, 50))
derajat6_2.draw(win)

ver2 = Line(Point(pytaX(floatDe6,6),pytaY(floatDe6,6)), Point(pytaX(floatDe6,6), -pytaY(floatDe6,6)))
ver2.setWidth(2)
ver2.setFill(color_rgb(168, 50, 50))
ver2.draw(win)

# Field
count1 = 0
for i in range(10, 10*9+1, 10):
    rows = [
        floatDe10,
        floatDe20,
        floatDe30,
        floatDe40,
        floatDe50,
        floatDe60,
        floatDe70,
        floatDe80,
        floatDe90
    ]
    warna = [
        #6 
        color_rgb(168, 50, 50),
        #10 
        color_rgb(168, 97, 50),
        #20
        color_rgb(168, 139, 50),
        #30
        color_rgb(168, 166, 50),
        #40
        color_rgb(39, 168, 50),
        #50
        color_rgb(85, 168, 50),
        #60
        color_rgb(50, 168, 158),
        #70
        color_rgb(50, 119, 168),
        #80
        color_rgb(0, 52, 168),
        #90
        color_rgb(140, 50, 168)
    ]
    derajat = Line(Point(0,0), Point(pytaX(rows[count1],i),pytaY(rows[count1],i)))
    derajat.setWidth(2)
    derajat.setFill(warna[count1+1])
    derajat.draw(win)
    
    derajat_2 = Line(Point(0,0), Point(pytaX(rows[count1],i),-pytaY(rows[count1],i)))
    derajat_2.setWidth(2)
    derajat_2.setFill(warna[count1+1])
    derajat_2.draw(win)
    
    ver = Line(Point(pytaX(rows[count1],i),pytaY(rows[count1],i)), Point(pytaX(rows[count1],i),-pytaY(rows[count1],i)))
    ver.setWidth(2)
    ver.setFill(warna[count1+1])
    ver.draw(win)
    count1 += 1

# Polygon    
count2 = 0
for i in range(9):   
    # Polygon
    derajat = ["6", "10", "20", "30", "40", "50", "60", "70", "80", "90"]
    rows = [
        floatDe6,
        floatDe10,
        floatDe20,
        floatDe30,
        floatDe40,
        floatDe50,
        floatDe60,
        floatDe70,
        floatDe80,
        floatDe90
    ]
    
    # Poly normal
    poly = Line(Point(
        pytaX(rows[8-count2], float(derajat[8-count2])),
        pytaY(rows[8-count2], float(derajat[8-count2]))
    ), 
                Point(
                    pytaX(rows[7-count2], float(derajat[7-count2])),
                    pytaY(rows[7-count2], float(derajat[7-count2]))
                )
               )
    poly.setFill("white")
    poly.draw(win)
    
    # Poly inverse
    poly2 = Line(Point(
        pytaX(rows[8-count2], float(derajat[8-count2])),
        -pytaY(rows[8-count2], float(derajat[8-count2]))
    ), 
                Point(
                    pytaX(rows[7-count2], float(derajat[7-count2])),
                    -pytaY(rows[7-count2], float(derajat[7-count2]))
                )
               )
    poly2.setFill("white")
    poly2.draw(win)
    count2 += 1
    
# Exit Button
exButton = Rectangle(Point(600, 650), Point(750, 750))
exButton.setOutline("red")
exButton.draw(win)
exText = Text(Point((600+750)/2, (650+750)/2), "EXIT")
exText.setTextColor("red")
exText.draw(win)

# Mouse Click
posisi = win.getMouse()
print("X :" + str(posisi.getX()))
print("Y :" + str(posisi.getY()))
print("-------------------")
while (posisi.getX()<600 or posisi.getX()>750) or (posisi.getY()<650 or posisi.getY()>750):
    posisi = win.getMouse()
    print("X :" + str(posisi.getX()))
    print("Y :" + str(posisi.getY()))
    print("-------------------")

print("user exit")
print("Bye bye!")
win.close()