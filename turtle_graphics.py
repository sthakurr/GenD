import math
import random
import numpy as np
from turtle import *
import turtle
from math import sin, pi, e
import cairo
import matplotlib.pyplot as plt
from PIL import Image
import cv2
from tkinter import *


S = ["rainbow benzene","spiral helix","turtle circles","spiral","scribbled_rays","waves","harmonograph","spirograph"]
shape = "scribbled_rays"
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

def hueGen(hue = 0,val = 1, sat=1):
    """Generates a 360 degree range of hues
    sat of 1 is full saturation, 0 is B & W.
    val of 1 is full color, 0 is black"""
    if 0 <= hue < 60:
        r = 1
        g = (hue/59) + (1-sat)*(59-hue)/59
        b = 1 - sat
        hueOut = (r*val,g*val,b*val)
    elif 60 <= hue < 120:
        r = ((1-(hue-60)/59) + (1-sat)*(1-(119-hue)/59))
        g = 1
        b = 1 - sat
        hueOut = (r*val,g*val,b*val)
    elif 120 <= hue < 180:
        r = 1 - sat
        g = 1
        b = ((hue-120)/59) + (1-sat)*(179-hue)/59
        hueOut = (r*val,g*val,b*val)
    elif 180 <= hue < 240:
        r = 1 - sat
        g = (1-(hue-180)/59) + (1-sat)*(1-(239-hue)/59)
        b = 1
        hueOut = (r*val,g*val,b*val)
    elif 240 <= hue < 300:
        r = ((hue-240)/59) + (1-sat)*(299-hue)/59
        g = 1 - sat
        b = 1
        hueOut = (r*val,g*val,b*val)
    elif 300 <= hue < 360:
        r = 1
        g = 1 - sat
        b = (1-(hue-300)/59) + (1-sat)*(1-(359-hue)/59)
        hueOut = (r*val,g*val,b*val)
    elif hue >= 360:
        hueOut = hueGen(hue % 360, val, sat)
    return hueOut
if shape == "spirograph":
	WIDTH = 30
	HEIGHT = 30
	PIXEL_SCALE = 20

	surface = cairo.ImageSurface(cairo.FORMAT_RGB24, WIDTH*PIXEL_SCALE, HEIGHT*PIXEL_SCALE)
	ctx = cairo.Context(surface)
	ctx.scale(PIXEL_SCALE, PIXEL_SCALE)

	ctx.set_source_rgb(1, 1, 1)
	ctx.rectangle(0, 0, WIDTH, HEIGHT)
	ctx.fill()

	ctx.translate(WIDTH/2, HEIGHT/2)

	# Create the spirograph points
	def create_spiro(a, b, d):
		dt = 0.01
		t = 0
		pts = []
		while t < 2*math.pi*b/math.gcd(a, b):
			t += dt
			x = (a - b) * math.sin(t) + d * math.sin((a - b)/b * t)
			y = (a - b) * math.cos(t) - d * math.cos((a - b)/b * t)
			pts.append((x, y))
		return pts

	def draw_spiro(ctx, a, b, d, color):
		ctx.set_line_width(.1)
		ctx.set_source_rgb(*color)
		pts = create_spiro(a, b, d)
		ctx.move_to(pts[0][0], pts[0][1])
		for x, y in pts[1:]:
			ctx.line_to(x, y)
			ctx.stroke()
	for d in range(50, 80, 5):
		draw_spiro(ctx, 11, 20, d/10, (0, 0.5, 0.5))
		ctx.rotate(0.1)

	surface.write_to_png('spirograph.png')

	spiro = Image.open('spirograph.png')
	spiro

if shape == "rainbow benzene":
	t = turtle.Pen() 
	t.speed(0)
	turtle.bgcolor('black') 
	for x in range(360): 
    		t.pencolor(colors[x%6]) 
    		t.width(x/100 + 1) 
    		t.forward(x) 
    		t.left(59)
	turtle.done() 

if shape == "spiral helix":
	loadWindow = turtle.Screen() 
	turtle.bgcolor('black')
	turtle.speed(1) 
	turtle.pencolor('white')
  
	for i in range(100): 
		turtle.circle(5*i) 
		turtle.circle(-5*i) 
		turtle.left(i) 
  
	turtle.done()

if shape == "turtle circles":
	setup()
	t1 = Turtle()
	t1.speed(0)
	t1.up()
	colors = [#reddish colors
	(1.00, 0.00, 0.00),(1.00, 0.03, 0.00),(1.00, 0.05, 0.00),(1.00, 0.07, 0.00),(1.00, 0.10, 0.00),(1.00, 0.12, 0.00),(1.00, 0.15, 0.00),(1.00, 0.17, 0.00),(1.00, 0.20, 0.00),(1.00, 0.23, 0.00),(1.00, 0.25, 0.00),(1.00, 0.28, 0.00),(1.00, 0.30, 0.00),(1.00, 0.33, 0.00),(1.00, 0.35, 0.00),(1.00, 0.38, 0.00),(1.00, 0.40, 0.00),(1.00, 0.42, 0.00),(1.00, 0.45, 0.00),(1.00, 0.47, 0.00),
#orangey colors
(1.00, 0.50, 0.00),(1.00, 0.53, 0.00),(1.00, 0.55, 0.00),(1.00, 0.57, 0.00),(1.00, 0.60, 0.00),(1.00, 0.62, 0.00),(1.00, 0.65, 0.00),(1.00, 0.68, 0.00),(1.00, 0.70, 0.00),(1.00, 0.72, 0.00),(1.00, 0.75, 0.00),(1.00, 0.78, 0.00),(1.00, 0.80, 0.00),(1.00, 0.82, 0.00),(1.00, 0.85, 0.00),(1.00, 0.88, 0.00),(1.00, 0.90, 0.00),(1.00, 0.93, 0.00),(1.00, 0.95, 0.00),(1.00, 0.97, 0.00),
#yellowy colors
(1.00, 1.00, 0.00),(0.95, 1.00, 0.00),(0.90, 1.00, 0.00),(0.85, 1.00, 0.00),(0.80, 1.00, 0.00),(0.75, 1.00, 0.00),(0.70, 1.00, 0.00),(0.65, 1.00, 0.00),(0.60, 1.00, 0.00),(0.55, 1.00, 0.00),(0.50, 1.00, 0.00),(0.45, 1.00, 0.00),(0.40, 1.00, 0.00),(0.35, 1.00, 0.00),(0.30, 1.00, 0.00),(0.25, 1.00, 0.00),(0.20, 1.00, 0.00),(0.15, 1.00, 0.00),(0.10, 1.00, 0.00),(0.05, 1.00, 0.00),
#greenish colors
(0.00, 1.00, 0.00),(0.00, 0.95, 0.05),(0.00, 0.90, 0.10),(0.00, 0.85, 0.15),(0.00, 0.80, 0.20),(0.00, 0.75, 0.25),(0.00, 0.70, 0.30),(0.00, 0.65, 0.35),(0.00, 0.60, 0.40),(0.00, 0.55, 0.45),(0.00, 0.50, 0.50),(0.00, 0.45, 0.55),(0.00, 0.40, 0.60),(0.00, 0.35, 0.65),(0.00, 0.30, 0.70),(0.00, 0.25, 0.75),(0.00, 0.20, 0.80),(0.00, 0.15, 0.85),(0.00, 0.10, 0.90),(0.00, 0.05, 0.95),
#blueish colors
(0.00, 0.00, 1.00),(0.05, 0.00, 1.00),(0.10, 0.00, 1.00),(0.15, 0.00, 1.00),(0.20, 0.00, 1.00),(0.25, 0.00, 1.00),(0.30, 0.00, 1.00),(0.35, 0.00, 1.00),(0.40, 0.00, 1.00),(0.45, 0.00, 1.00),(0.50, 0.00, 1.00),(0.55, 0.00, 1.00),(0.60, 0.00, 1.00),(0.65, 0.00, 1.00),(0.70, 0.00, 1.00),(0.75, 0.00, 1.00),(0.80, 0.00, 1.00),(0.85, 0.00, 1.00),(0.90, 0.00, 1.00),(0.95, 0.00, 1.00)]
	n=100
	def dist(k,i):
		return math.sqrt(((coords[k][0]-coords[i][0])**2) + ((coords[k][1]-coords[i][1])**2))

	coords = np.zeros(shape = (n,2))
	radius = np.zeros(shape = (n,1))
	i=0
	while i<n:
		x = random.randint(-300, 300)
		y = random.randint(-300, 300)
		circle_size = random.randint(20,30)
		coords[i][0] = x
		coords[i][1] = y
		radius[i] = circle_size
		k=0
		is_Overlap = False
		while k < i:
			distance = radius[i]+radius[k]
			if dist(k,i)<distance:
				is_Overlap = True
			k+=1
		if is_Overlap==False:
			t1.goto(x,y)
			color = random.choice(colors)
			t1.down()
			t1.color(color)
			t1.begin_fill()
			t1.circle(circle_size)
			t1.end_fill()
			t1.up()
		i+=1
	turtle.done()

if shape == "spiral":
	turtle.setup(width=600, height=500)
	turtle.reset()
	turtle.hideturtle()
	turtle.speed(0)

	turtle.bgcolor('black')

	c = 0
	x = 0

	colors = [
	#reddish colors
	(1.00, 0.00, 0.00),(1.00, 0.03, 0.00),(1.00, 0.05, 0.00),(1.00, 0.07, 0.00),(1.00, 0.10, 0.00),(1.00, 0.12, 0.00),(1.00, 0.15, 0.00),(1.00, 0.17, 0.00),(1.00, 0.20, 0.00),(1.00, 0.23, 0.00),(1.00, 0.25, 0.00),(1.00, 0.28, 0.00),(1.00, 0.30, 0.00),(1.00, 0.33, 0.00),(1.00, 0.35, 0.00),(1.00, 0.38, 0.00),(1.00, 0.40, 0.00),(1.00, 0.42, 0.00),(1.00, 0.45, 0.00),(1.00, 0.47, 0.00),
#orangey colors
(1.00, 0.50, 0.00),(1.00, 0.53, 0.00),(1.00, 0.55, 0.00),(1.00, 0.57, 0.00),(1.00, 0.60, 0.00),(1.00, 0.62, 0.00),(1.00, 0.65, 0.00),(1.00, 0.68, 0.00),(1.00, 0.70, 0.00),(1.00, 0.72, 0.00),(1.00, 0.75, 0.00),(1.00, 0.78, 0.00),(1.00, 0.80, 0.00),(1.00, 0.82, 0.00),(1.00, 0.85, 0.00),(1.00, 0.88, 0.00),(1.00, 0.90, 0.00),(1.00, 0.93, 0.00),(1.00, 0.95, 0.00),(1.00, 0.97, 0.00),
#yellowy colors
(1.00, 1.00, 0.00),(0.95, 1.00, 0.00),(0.90, 1.00, 0.00),(0.85, 1.00, 0.00),(0.80, 1.00, 0.00),(0.75, 1.00, 0.00),(0.70, 1.00, 0.00),(0.65, 1.00, 0.00),(0.60, 1.00, 0.00),(0.55, 1.00, 0.00),(0.50, 1.00, 0.00),(0.45, 1.00, 0.00),(0.40, 1.00, 0.00),(0.35, 1.00, 0.00),(0.30, 1.00, 0.00),(0.25, 1.00, 0.00),(0.20, 1.00, 0.00),(0.15, 1.00, 0.00),(0.10, 1.00, 0.00),(0.05, 1.00, 0.00),
#greenish colors
(0.00, 1.00, 0.00),(0.00, 0.95, 0.05),(0.00, 0.90, 0.10),(0.00, 0.85, 0.15),(0.00, 0.80, 0.20),(0.00, 0.75, 0.25),(0.00, 0.70, 0.30),(0.00, 0.65, 0.35),(0.00, 0.60, 0.40),(0.00, 0.55, 0.45),(0.00, 0.50, 0.50),(0.00, 0.45, 0.55),(0.00, 0.40, 0.60),(0.00, 0.35, 0.65),(0.00, 0.30, 0.70),(0.00, 0.25, 0.75),(0.00, 0.20, 0.80),(0.00, 0.15, 0.85),(0.00, 0.10, 0.90),(0.00, 0.05, 0.95),
#blueish colors
(0.00, 0.00, 1.00),(0.05, 0.00, 1.00),(0.10, 0.00, 1.00),(0.15, 0.00, 1.00),(0.20, 0.00, 1.00),(0.25, 0.00, 1.00),(0.30, 0.00, 1.00),(0.35, 0.00, 1.00),(0.40, 0.00, 1.00),(0.45, 0.00, 1.00),(0.50, 0.00, 1.00),(0.55, 0.00, 1.00),(0.60, 0.00, 1.00),(0.65, 0.00, 1.00),(0.70, 0.00, 1.00),(0.75, 0.00, 1.00),(0.80, 0.00, 1.00),(0.85, 0.00, 1.00),(0.90, 0.00, 1.00),(0.95, 0.00, 1.00)
]

	while x < 1000:
		idx = int(c)
		color = colors[idx]
		turtle.color(color)
		turtle.forward(x)
		turtle.right(98)
		x = x + 1
		c = c + 0.1

	turtle.done()

if shape == "scribbled_rays":
	turtle.tracer(0, 0)
	wn = turtle.Screen()
	wn.colormode(255)
	turtle.bgcolor("black")
	alex = turtle.Turtle()
	alex.speed(10)
	alex.goto(0,0)
	alex.pensize(0)
	alex.ht()
	for i in range(400):
		alex.color(random.randrange(256),random.randrange(256),random.randrange(256))
		alex.goto(round(random.gauss(0,100),0),round(random.gauss(0,100),0))
		x = alex.xcor()
		y = alex.ycor()
		for j in range(25):
			s = round(random.gauss(0,5), 0)
			t = round(random.gauss(0,5), 0)
			alex.color(random.randrange(256),random.randrange(256),random.randrange(256))
			alex.pensize(0)
			alex.goto(x + s, y + t)
		alex.goto(s,t)
	turtle.update()
	turtle.done()

if shape == "waves":
	def waves(repeats = 1):
		for i in range(repeats):
			alex.up()
			alex.color(hueGen(i, 1*i/repeats, 1))
			alex.goto(-315,315 - i)
			alex.seth(45) # set heading
			x = alex.xcor()
			y = alex.ycor()
			f = i + 1
			for j in range(630):
				x = alex.xcor()
				alex.goto(x + 1, y + 25*sin(8*j/f + i/25)) # plot sines
				alex.down()
				x = alex.xcor()
	turtle.tracer(0, 0)
	wn = turtle.Screen()
	wn.colormode(1)
	turtle.bgcolor("black")
	alex = turtle.Turtle()
	alex.speed(10)
	alex.pensize(2)
	alex.ht()
	waves(700)
	turtle.update()
	wn.exitonclick()

if shape == "harmonograph":

	decay1, decay2, decay3, decay4 = 0.02, 0.5, 0.2, 0.005  #The oscillation decay coefficients
	phase1, phase2, phase3, phase4 = pi/6, pi/2, pi/6, pi/2  #Phase shifts
	freq1, freq2, freq3, freq4 = 3, 2, 6, 4 #Frequencies
	turtle.speed(0)

	t = 0 #Initial time
	dt = 0.05 #Time shift between each points of the graph

	while t < 10:
    		x = 100 * pow(e, -decay1 * t) * sin(t * freq1 + phase1) + 100 * pow(e, -decay2 * t) * sin(t * freq2 + phase2) #x axis position
    		y = 100 * pow(e, -decay3 * t) * sin(t * freq3 + phase3) + 100 * pow(e, -decay4 * t) * sin(t * freq4 + phase4) #y axis position
    		turtle.setposition(x, y) #Setting the position of the pen
    		t += dt #Next (new) value of time
