#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import *
from pybricks.parameters import Port
from pybricks.tools import *
from pybricks.robotics import DriveBase

ev3 = EV3Brick()
#Adds variables to motor
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

color_sensor = ColorSensor(Port.S3)
color = color_sensor.color()

obstacle_sensor = UltrasonicSensor(Port.S4)

#Combines variables/motors together
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

correct_colors = ["RED", "YELLOW"]

def main():

    while True:
        robot.drive()
        if color_sensor.reflection() <= 10:
            robot.stop()
            robot.turn(90)
        elif obstacle_sensor.distance() >= 100:
            robot.stop()
            robot.turn(90)
            
            

    