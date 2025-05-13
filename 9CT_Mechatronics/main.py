#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port
# from pybricks.tools import (wait, Stopwatch, DataLog) - Not used
from pybricks.robotics import DriveBase

ev3 = EV3Brick()

#Adds variables to motor
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

color_sensor = ColorSensor(Port.S3)
color_sensor_down = ColorSensor(Port.S1)
color = color_sensor.color()

obstacle_sensor = UltrasonicSensor(Port.S4)


robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104) # Combines variables/motors together

correct_colors = ["RED", "YELLOW"] # Correct colours are removed when picked up later

def goBack():

    while True: # Go back to the start

        robot.drive(100, 0) # Drive forever until 
        if color_sensor_down.reflection() <= 10: # The reflection of the carpet is <10
            robot.stop()
            robot.turn(90) # Alternatively turns 90 degrees so that it can loop around the mat
        if color_sensor_down.color() == 'BLUE': # On the mat, there are blue lines that indicate the start area
            robot.stop 
            # Drop object
            if len(correct_colors) == 0: # If there are no more correct colour blocks, finish program
                    robot.stop
                    break

        if obstacle_sensor.distance() >= 100: # Avoids obstacles
            robot.stop()
            robot.turn(90)
            




def main(): # Beginning of the main program

    while True:
        robot.drive(100, 0) # Drive forever until
    
        if color_sensor_down.reflection() <= 10: # The reflection of the carpet is <10
            robot.stop()
            robot.turn(120) # Value is 120 so that it does not loop around the mat
        if obstacle_sensor.distance() <= 100: # Avoids obstacles
            robot.stop()
            robot.turn(90)

        if color_sensor.color() in correct_colors: # If the colour that it detects is in the correct_colors list, picks up the object
            correct_colors.remove(color) 
            # Pickup the correct object
            break 
    
    goBack() # Robot returns back to the start
    
    
 
        



# main 
main()


#Thanks for all the fish