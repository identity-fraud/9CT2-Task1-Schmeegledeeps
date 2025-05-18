# Aim
The aim is to navigate around obstacles, pick up two uniquely idenitified boxes (Coloured red and yellow) and bring them back to the starting area.

# Key Functions
Key functions for the robot are:
* Able to navigate around the obstacles without touching them
* Not leave the mat
* Pickup the two coloured boxes
* Navigate back to the starting area

# Functional and Non-functional requirements

## Functional Requirements:
* Move forward until an object is detected in front of the robot (within 10cm) using the ultrasonic sensor then turn 90° to avoid the obstacle
* Move forward until one of the boxes (Red and Yellow) are found, then pick the boxes up using pincers attachment (using the motors)
* Turn 90° when the edge of the mat is detected (using the colour sensor's reflection function to identify the difference between the floor and the mat)

## Non-functional requirements:
* The robot should stop immediately after detecting an obstacle
* The robot should be quick at its speed and obstacle detection
* The robot should loop around the mat correctly

# Use Cases
**Scenario: The robot encounters an obstacle**

>Inputs: The ultrasonic sensor detects an object within 10cm

>Actions: The robot stops and spins 90° and then continues moving forward

>Expected Outcome: The robot avoids the obstacles and continues moving

**Scenario: The robot must pick up a specific coloured object**

>Inputs: The colour sensor detects the correct coloured object to pickup

>Actions: The motor moves the pincer attachment into the correct object and picks it up

>Expected Outcome: The robot pickups up the correct object

**Scenario: The robot needs to go back to its original postion after picking up the correct objects**

>Inputs: When the robot picks up the correct object

>Actions: The robot should move until it finds the edge of the mat, then loops around the mat until it finds the blue line indicator at the start
>Expected Outcome: The robot is at its original position 

# Test Cases
| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
|Avoid Obstacle|Ultrasonic Sensor detects object within 10cm|The robot stops and spins 90° and then continues moving forward|
|Pickup specific coloured object|Colour sensor detects correct colour(s)|Using motors it grabs and picks up the correct object with the pincer attachment|
|Go back to original position|Motor picks up correct object|Robot moves until it reaches the end of the mat, then loops around the mat until it finds the blue line indicator for the start |

# Flowchart and Pseudocode
## Pseudocode Activities
<details>
<summary>1 a. </summary>
<br>

Question 1 a. Pseudocode
```
BEGIN Even or Odd

INPUT Number

IF Number % 2 == 0 THEN

    OUTPUT "Even"

ELSE

    OUTPUT "Odd"

ENDIF

END
```
</details>

<details>
<summary> 1 b.</summary>
<br>

Question 1 b. Pseudocode
```
BEGIN Calculating Factorial

INPUT Number

FOR i = 1, i TO Number, STEP 1
    PROCESS Number = Number * i

OUTPUT Number

END
```    
</details> 

<details>
<summary> 2 a. </summary> 
<br>

Question 2 a. Pseudocode
```
BEGIN Cost of total books

INPUT AMOUNT

FOR i = 0, i TO AMOUNT, STEP 1

    INPUT PRICE

    PROCESS PRICES += PRICE
    
IF PRICES > 100

    PROCESS = PRICES % 1.1

ENDIF

OUTPUT PRICES

END
```

</details>

<details> 
<summary>2 b.</summary>
<br>
Question 2 b. Pseudocode

```
BEGIN Sum of numbers from 1 to N

INPUT N

FOR i = 0, i TO N, STEP 1

    PROCESS sum += N + i
    
    PROCESS N - 1

OUTPUT SUM

END
```

</details>

## Flowchart Activities

<details>
<summary> 1 a. </summary>
<br>
Question 1 a. Flowchart

![Flowchart](https://github.com/transaction-fraud/9CT2-Task1-Schmeegledeeps/blob/main/Images/1a.excalidraw.png "Flowchart 1 a.")

</details>

<details>
<summary> 1 b.</summary>
<br>
Question 1 b. Flowchart

![Flowchart](https://github.com/identity-fraud/9CT2-Task1-Schmeegledeeps/blob/main/Images/1b.excalidraw.png "Flowchart 1 b.")

</details>

<details>
<summary> 1 c.</summary>
<br>
Question 1 c. Flowchart

![Flowchart](https://github.com/identity-fraud/9CT2-Task1-Schmeegledeeps/blob/main/Images/1c.excalidraw.png "Flowchart 1 c.")

</details>

## Main Flowcharts
</details>

<details>
<summary> Processes Flowchart</summary>
<br>

![Flowchart](https://github.com/identity-fraud/9CT2-Task1-Schmeegledeeps/blob/d2650d47f341ee47c8cdf90174b5ce9876271051/Images/processes.png "Processes Flowchart")

</details>

<details>
<summary> Individual Sub-processes Flowchart</summary>
<br>
 
![Flowchart](https://github.com/identity-fraud/9CT2-Task1-Schmeegledeeps/blob/be90797ef4b39e03a28ceff8c450e923cd175ee9/Images/subprocess.png "Sub-processes Flowchart")

</details>

## Main Pseudocode


<details>
<summary> Proccess Pseudocode</summary>
<br>

```
BEGIN

    read (avoid_obstacles)

    read (pickup_colour)

    read (avoid_border)

    read (find_start)

    read (drop_colour)

END
```

</details>


<details>
<summary> Individual Sub-processes Pseudocode</summary>

<br>

<h3> Avoid Obstacles</h3>
<br>

```
BEGIN avoid_obstacles

    Get obsticle_sensor.distance()

    IF distance >= 100mm

        Turn 90

    ENDIF 

    Drive Forward

END avoid_obstacles
        
```



<h3> Pickup Colour</h3>
<br>

```
BEGIN pickup_colour
    Get colour_sensor.colour()

    IF colour = RED or YELLOW

        Pickup Object

    ENDIF 

    Drive Forward

END pickup_colour
```


<h3> Avoid Border</h3>
<br>

```
BEGIN avoid_border
    Get colour_sensor_down.reflection()

    IF reflection <= 10

        Turn 120

    ENDIF 

    Drive Forward

END avoid_border
```



<h3> Find Start<</h3>
<br>

```
BEGIN find_start
    Get colour_sensor_down.reflection()

    IF reflection <= 10

        Turn 90

    ENDIF 

    Drive Forward

END find_start
```


<h3> Drop Colour</h3>
<br>

```
BEGIN drop_colour
    Get colour_sensor_down.colour()

    IF colour_sensor_down.colour = BLUE

        Drop Object
        
    ENDIF 

    Drive Forward

END drop_colour
```


</details>

# Test Cases
<details>

```
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

        
    
    goBack() # Robot returns back to the start
    
    
 
        



# main 
main()

#So long and thanks for all the fish
```
 Avoids both correct coloured blocks and not correct coloured blocks - testing movement code

 ```
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

        if obstacle_sensor.distance() <= 100 and color_sensor.color() not in correct_colors: # Avoids obstacles
            robot.stop()
            robot.turn(90)

        
    
    goBack() # Robot returns back to the start
    
    
 
        



# main 
main()

#So long and thanks for all the fish

 ```

Implemented Grab code - Changed the lego stucture to make the arm mroe compact but the grabber doesnt work - need to fix.

```
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

        if obstacle_sensor.distance() <= 100 and color_sensor.color() not in correct_colors: # Avoids obstacles
            robot.stop()
            robot.turn(90)

        
    
    goBack() # Robot returns back to the start
    
    
 
        



# main 
main()

#So long and thanks for all the fish

```
Made the robot stop pathfinding when a block of the correct colour is found, changed the grabber but still haven't tested, made the grabber hypothetically drop the block in the starting box and if all the boxes have been collected stops the code.

</details>

# Peer Evaluation from Anwesh

### William - 4/5
<summary> 
When rating 1-5 with 1 being lacklustre effort and 5 being outstanding effort, how much effort do you feel this group member put into this project?

5/5

Explain the reason for this score in detail: William provided most of the code and the structure of the programm, with the of the debugging and implementation done by Anwesh, spending a lot of time working on the project.



When rating 1-5 with 1 being not at all and 5 being an exceptional amount, how much did this team member contribute to the team's efforts throughout this project?

5/5

Explain the reason for this score in detail: He contributed a lot with the code and the Design and requirements outline. And he helped other group members to finish their contributions too.



When rating 1-5 with 1 being entirely non-functional and 5 being completely functional, how effective was this team member's final test case?

3/5

Explain the reason for this score in detail: Since we all converged on one main point we all had the same final test case, although this test was not very functional due to the time frame of the code butwith some features such as pathfinding and movement working properly.



When rating 1-5 with 1 being not well at all and 5 being exceptionally well, how well do you think this team member performed throughout all stages of the project?

4/5

Explain the reason for this score in detail: The team member preformed well and across ht etime frame contributing a steady flow of work between the time frame. </summary>


### Adrian - 4/5
<summary> 

When rating 1-5 with 1 being lacklustre effort and 5 being outstanding effort, how much effort do you feel this group member put into this project?

5/5

Explain the reason for this score in detail: Adrian worked on the flowcharts and pseudocode and had a lot of frustrations with the website but still managed to get both of them out. He put a lot of effort into making them accurate.



When rating 1-5 with 1 being not at all and 5 being an exceptional amount, how much did this team member contribute to the team's efforts throughout this project?

5/5

Explain the reason for this score in detail: With doing all the flowcharts and the psuedocode Adrian managed to take a huge chunk off of the work from everyone else.



When rating 1-5 with 1 being entirely non-functional and 5 being completely functional, how effective was this team member's final test case?

3/5

Explain the reason for this score in detail: Since we all converged on one main point we all had the same final test case, although this test was not very functional due to the time frame of the code butwith some features such as pathfinding and movement working properly.



When rating 1-5 with 1 being not well at all and 5 being exceptionally well, how well do you think this team member performed throughout all stages of the project?

5/5

Explain the reason for this score in detail: Adrian provided a constant flow of progression through the entire project though at the end we couldn't get the final and finish the project.
</summary>

# FINAL TEST EVALUATION:

<summary>
Since we all converged on the same Test early on we all had different jobs to do across the same test. I was debugging and working on the physical properties of the EV3 , William was working on the code and the main structure of the programm and Adrian worked on the Theory and pseudocode.
</summary>

<br>

## Functional Requirements

1. The Robot does turn 90° when a incorrect coloured block is found.
2. The Robot moves randomly until the correct colour box is found but the pincer attachments do not get used instead it avoids it like every other block.
3. The Robot does go back to start using the black line and the blue marked line.

The Robot meets most of the functional requirements but doesnt grab the block.

<br>

## Non-Functional Requirements

1. The Robot does immedietly stops when a block is detected.
2. The Robot was not quick, going randomly around the map didnt let the robot to find a box quickly but the line back to the start was efficient.
3. The Robot looped around the Map randomly, allowing it to cover more space and find the blocks easier.

The Robot met all the Non-funtional requirements but couldve been a bit faster when going to the blocks.

## Group Final Preformance & Project Management

Our group preformed well in the start getting many aspects of the design under control but the code we stuggled on. We made the first movement scripts pretty quickly but we struggled on the functions to drive the robot or make the motors spin. We got the Robot to pathfind but we didnt have enough time to fix the motors and debug the entire grab and detect block scripts. We didnt reach the objective of the identified need.

## Team Collaboration
I think all the members of my team worked well together and imporved on each others works while lightening the load of the total work for the final project.

## Future Changes
I would take more time working on the code and testing it to finalise all the requirements and touch up the flowcharts and pseudocode to make them more accurate. I would fix the code for the grabber arm to make it finally work and I could increase the range for the Ultrasonic Sensor so the sides of the robot don't bump into the blocks.
