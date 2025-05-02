#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltraSonicSensor
from pybricks.parameters import Port
# from pybricks.tools import (wait, Stopwatch, DataLog)
from pybricks.robotics import DriveBase

ev3 = EV3Brick()
#Adds variables to motor
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

color_sensor = ColorSensor(Port.S3)
color_sensor_down = ColorSensor(Port.S1)
color = color_sensor.color()

obstacle_sensor = UltraSonicSensor(Port.S4)

#Combines variables/motors together
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
# class DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104):
    # robot = DriveBase() - doesnt work?
correct_colors = ["RED", "YELLOW"]

def goBack():

    while True: # Go back to the start

        robot.drive(100, 0)
        if color_sensor_down.reflection() <= 10:
            robot.stop()
            robot.turn(90)
        if color_sensor.color() == 'BLUE':
            robot.stop 
            # Drop object
            if len(correct_colors) == 0:
                    robot.stop
                    break

        if obstacle_sensor.distance() >= 100:
            robot.stop()
            robot.turn(90)
            




def main():

    while True:
        robot.drive(100, 0)
    
        if color_sensor_down.reflection() <= 10:
            robot.stop()
            robot.turn(100) # Value is 100 so that it does not loop around the mat
        if obstacle_sensor.distance() <= 100:
            robot.stop()
            robot.turn(90)

        if color_sensor.color() in correct_colors:
            correct_colors.remove(color) 
            # Pickup the correct object
            break
    
    goBack()
    
    
 
        



# main 
main()


#Thanks for all the fish