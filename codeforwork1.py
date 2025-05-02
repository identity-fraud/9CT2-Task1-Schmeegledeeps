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
color_sensor_down = ColorSensor(Port.S1)
color = color_sensor.color()

obstacle_sensor = UltrasonicSensor(Port.S4)

#Combines variables/motors together
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

correct_colors = ["RED", "YELLOW"]

def goBack():
    
    while True:

        robot.drive()
        if color_sensor_down.reflection() <= 10:
            robot.stop()
            robot.turn(90)
        
        if obstacle_sensor.distance() >= 100:
            robot.stop()
            robot.turn(90)

        if color_sensor_down.color() == 'BLUE':
            robot.stop()
            # Drop correct object
            if len(correct_colors) == 0:
                break
            else:
                main()
    
 
              



def main(): 

    while True:

        robot.drive()

        if color_sensor_down.reflection() <= 10:
            robot.stop()
            robot.turn(100) # Value is 100 so it does not loop around the mat

        if obstacle_sensor.distance() >= 100:
            robot.stop()
            robot.turn(90)
        
        if color in correct_colors:
            correct_colors.remove(color)
            robot.stop()
            # Pickup the correct object
            goBack()

            
main() 
# Thanks for all the fish           

    