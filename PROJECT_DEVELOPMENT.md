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
* Move forward until an object is detected in front of the robot (within 10cm) using the ultrasonic sensor then turn 10° everytime until it no longer sees it, if the target isn't red or yellow (using the colour sensor)
* Move forward until one of the boxes (Red and Yellow) are found, then pick the boxes up using pincers attachment (using the motors)
* Turn 90° when the edge of the mat is detected (using the colour sensor's reflection function to identify the difference between the floor and the mat)

## Non-functional requirements:
* The robot should stop immediately after detecting an obstacle
* The robot should not loop for a very long amount of time

# Use Cases
**Scenario: The robot encounters an obstacle**

>Inputs: The ultrasonic sensor detects an object within 10cm

>Actions: The robot stops and spins 10° every time until it can not longer see the object to avoid it and continues moving forward

>Expected Outcome: The robot avoids the obstacles and continues moving

**Scenario: The robot must pick up a specific coloured object**

>Inputs: The colour sensor detects the correct coloured object to pickup

>Actions: The motor moves the pincer attachment into the correct object and picks it up

>Expected Outcome: The robot pickups up the correct object

**Scenario: The robot needs to go back to its original postion after picking up the correct objects**

>Inputs: When the robot picks up the correct object

>Actions: The robot should continue doing revolutions around the mat until it reaches the centre, which then moves backwards until the start position

>Expected Outcome: The robot is at its original position

# Test Cases
| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
|Avoid Obstacle|Ultrasonic Sensor detects object within 10cm|The robot stops and spins 10° until it can no longer see the object and continues moving forward|
|Pickup specific coloured object|Colour sensor detects correct colour(s)|Using motors it grabs and picks up the correct object with the pincer attachment|
|Go back to original position|Motor picks up correct object|Robot continues moving forward x cm less every "revolution" until it is in the centre and moves back to the start position|

# Flowchart and Pseudocode
## Pseudocode Activities

### 1 a. 
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

### 1 b.
```
BEGIN Calculating Factorial

INPUT Number

FOR i = 1, i TO Number, STEP 1
    PROCESS Number = Number * i

OUTPUT Number

END
```     
### 2 a.  
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

### 2 b.
```
BEGIN Sum of numbers from 1 to N

INPUT N

FOR i = 0, i TO N, STEP 1

    PROCESS sum += N + i
    
    PROCESS N - 1

OUTPUT SUM

END
```

# Flowchart
## Flowchart Activities

### 1 a. 
![Flowchart](https://github.com/transaction-fraud/9CT2-Task1-Schmeegledeeps/blob/main/Images/1a.excalidraw.png "Flowchart 1 a.")
### 1 b.
![Flowchart](https://github.com/transaction-fraud/9CT2-Task1-Schmeegledeeps/blob/ANWESH/Images/1b.excalidraw.png "Flowchart 1 b.")
### 1 c.
![Flowchart](https://github.com/transaction-fraud/9CT2-Task1-Schmeegledeeps/blob/ANWESH/Images/1c.excalidraw.png "Flowchart 1 c.")
