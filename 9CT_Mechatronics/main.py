#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Note that this code cannot be run in this directory (you must create a seperate one through the VSC Lego Mindstorm extension)
ev3 = EV3Brick()

#Adds variables to each sensor
grab_motor = Motor(Port.A)
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)


color_sensor_down = ColorSensor(Port.S1)
color_sensor = ColorSensor(Port.S3)

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
            robot.run(-100) # Negative integer so that it unclamps on the correct block
            if len(correct_colors) == 0: # If there are no more correct colour blocks, finish program
                    robot.stop
                    break

        if obstacle_sensor.distance() >= 100: # Avoids obstacles
            robot.stop()
            robot.turn(90)
            




def main(): # Beginning of the main program

    while True:
        robot.drive(100, 0) # Drive forever until

        if color_sensor.color() in correct_colors: # If the colour that it detects is in the correct_colors list, picks up the object
            robot.stop()
            grab_motor.run(-100)
            grab_motor.run(100) # Moves the motor into the correct block
            wait(1000)
            
            grab_motor.brake()
            correct_colors.remove(color) 

            # Pickup the correct object
            break 
    
        if color_sensor_down.reflection() <= 10: # The reflection of the carpet is <10
            robot.stop()
            robot.turn(120) # Value is 120 so that it does not loop around the mat
        if obstacle_sensor.distance() <= 100: # Avoids obstacles
            robot.stop()
            robot.turn(90)

        
    
    goBack() # Robot returns back to the start
    
    
 
        



# main 
main()

#So long and thanks for all the fish
