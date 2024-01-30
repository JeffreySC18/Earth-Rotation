from vpython import *
import math

R = 1
earth = sphere(pos=vector(0, 0, 0), radius=R, texture=textures.earth, shineness=0)

tilt = (23.5 * pi) / 180
earth.rotate(origin=vector(0, 0, 0), axis=vector(0, 0, 1), angle=tilt)

Npole=cylinder(pos=vector(0,0,0), axis =1.5*R*vector(-sin(tilt), cos(tilt), 0), radius=0.02*R)
Spole=cylinder(pos=vector(0,0,0), axis =-1.5*R*vector(-sin(tilt), cos(tilt), 0), radius=0.02*R)



lat = 30*pi/180
ball=sphere(pos=R*vector(-cos(lat), sin(lat), 0), radius=0.03,color=color.yellow, make_trail=False)

scene.lights = []
scene.lights = scene.lights + [distant_light(direction=vector(-1, 0, 0),color=vector(.9,.9,.9))]