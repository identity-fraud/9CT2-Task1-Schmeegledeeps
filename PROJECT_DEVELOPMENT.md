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

## Peer Evaluation (From William)

### Anwesh - 4/5


When rating 1-5 with 1 being lacklustre effort and 5 being outstanding effort, how much effort do you feel this group member put into this project

5/5

I think Anwesh put all the effort required and more to achieve a functional robot, he worked on the physical robot and helped me debug problems within the code as well, and has spent a lot of time working on this project.

When rating 1-5 with 1 being not at all and 5 being an exceptional amount, how much did this team member contribute to the team's efforts throughout this project?

5/5

Anwesh contributed a lot in the making of the physical robot, and he helped Anwesh with his flowcharts and me with the debugging of the code.

When rating 1-5 with 1 being entirely non-functional and 5 being completely functional, how effective was this team member's final test case?

3/5

Though we all used the same code - meaning same test cases - our robots test case did not achieve some of our functional requirements due to the restricted time frame, though atleast some critical parts still work (parthfinding, obstacle avoidance).

When rating 1-5 with 1 being not well at all and 5 being exceptionally well, how well do you think this team member performed throughout all stages of the project?

4/5

I think that Anwesh performed very well and consistently throughout the stages in the project.


## Adrian - 4/5

When rating 1-5 with 1 being lacklustre effort and 5 being outstanding effort, how much effort do you feel this group member put into this project?

Adrian worked on the flowcharts and pseudocode regarding the robot, he made sure that they are accurate to the actual code and to the highest quality.

When rating 1-5 with 1 being not at all and 5 being an exceptional amount, how much did this team member contribute to the team's efforts throughout this project?

4/5

Adrian working on the pseudocode and flowcharts allowed us to focus more on debugging and the actual robot aspect of this project.

When rating 1-5 with 1 being entirely non-functional and 5 being completely functional, how effective was this team member's final test case?

3/5

Though we all used the same code - meaning same test cases - our robots test case did not achieve some of our functional requirements due to the restricted time frame, though atleast some critical parts still work (parthfinding, obstacle avoidance).

When rating 1-5 with 1 being not well at all and 5 being exceptionally well, how well do you think this team member performed throughout all stages of the project?

4/5

Adrian worked hard to create the flowcharts and pseudocode for us, and was very consistent at his work.

# Final Test and Evaluation

Anwesh worked on the physical robot, William worked on the code for the robot, and Adrian made the pseudocode and flowcharts.

