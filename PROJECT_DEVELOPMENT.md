# 9CT2-Task1-Schmeegledeeps

# Aim
The Aim is to pick up two differently coloured cubes and put them in the starting box without hitting obsticles along their path.

# Key Functions
Key functions for the robot are:
* To be able to navigate around obsticles without colliding with them
* Not leave the mat
* Pickup the two coloured boxes
* Navigate back to the starting box
# Functional and Non-functional requirements

## Functional Requirements:
* Travel around the map, while getting a smaller distance each revolution until it reaches the centre, it will aslways be looking for coloured blocks and obsticles in the way.
* Move forward until one of the boxes (Red and Yellow) are found, then pick the boxes up using pincers attachment (using the motors)
* Turn 180° when the edge of the mat is detected (using the colour sensor's reflection function to identify the difference between the floor and the mat)
* Follows the edge of the map back to the starting box.

## Non-functional requirements:
* High response time
* Should be accurate
* Also should be efficient


# Use Cases
Scenario: Robot much pick up an object and move it to a destination
Inputs: The robot will circulate the map, getting a smaller area each revolution until it detects something 10cm is front of it.
Actions: The robot spins 10° until the object is not seen then turns back to go along the map.
Outcome: The robot continues moving forever and turning away from obstacles until it finds a correctly coloured box and brings it back to the start.

# Test Cases
| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
|Avoid Obstacle|Ultrasonic Sensor detects object within 10cm|The robot stops and spins 10° until it can no longer see the object and continues moving forward|
|Pickup specific coloured object|Colour sensor detects correct colour(s)|Using motors it grabs and picks up the correct object with the pincer attachment|
|Go back to original position|Motor picks up correct object|Robot continues moving forward x cm less every "revolution" until it is in the centre and moves back to the start position|
  
# Flowchart and Pseudocode

# Flowchart Activity A

![Flowchart](https://github.com/transaction-fraud/9CT2-Task1-Schmeegledeeps/blob/ANWESH/Images/Untitled-2025-04-01-1147.excalidraw.png "Flowchart")

# Flowchart Activity B

![Flowchart](https://github.com/transaction-fraud/9CT2-Task1-Schmeegledeeps/blob/ANWESH/Images/Rawr2025-04-01-1147.excalidraw.png "Flowchart")

# Flowchart Activity C

![Flowchart](https://github.com/transaction-fraud/9CT2-Task1-Schmeegledeeps/blob/ANWESH/Images/Untitled-2025-04-h01-1147.excalidraw%20-%20Copy.png "Flowchart")

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