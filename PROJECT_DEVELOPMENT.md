# 9CT2 - Assessment Task 1 - Robotics

## Aim
The aim is to navigate around obstacles, pick up two uniquely idenitified boxes (Coloured red and yellow) and bring them back to the starting area.

## Key Functions
Key functions for the robot are:
* Able to navigate around the obstacles without touching them.
* Does not leave the mat.
* Can pickup the two coloured boxes.
* Can navigate blocks back to the starting area.

# Functional and Non-functional requirements

## Functional Requirements:
* Move forward until an object is detected in front of the robot (within 10cm) using the ultrasonic sensor then turn if the target isn't red or yellow (using the colour sensor)
* Move forward until one of the boxes (Red and Yellow) are found, then pick the boxes up using pincers attachment (using the motors)
* Turn 180° when the edge of the mat is detected (using the colour sensor's reflection function to identify the difference between the floor and the mat)

## Non-functional requirements:
* High response time
* Should be accurate
* Also should be efficient


# Use Cases
### Scenario: The robot encounters an obstacle or the edge of the mat.
 Inputs: The robot's ultrasonic sensor detects an object 10cm or less in front of it. The colour sensor then senses that it is an unwanted block colour.

 Actions: The robot rotates clockwise by 10° until the ultrasonic sensor can't see the object anymore.

 Expected Outcome: The robot continues moving, but in a different direction to avoid colliding with the obstacle.

### Scenario: The robot finds a block that it wants to grab.
Inputs: The robot detects an object in front of it using the ultrasonic sensor and the colour sensor sees that it is the right colour.

Actions: The robot moves towards the object and uses a pincer attachment with a motor to clasp onto the object.

Expected Outcome: The robot grabs and collects the object.

### Scenario: The robot has gathered all the desired blocks, and must get back to the beginning.
Inputs: The robot detects the colours that it wants. After gathering them and storing the values in variables, a function is triggered to begin reverse.

Actions: The robot will move to the edge of the mat and begin to follow the map's perimeter until it gets back to the start. It will turn at corners.

Expected Outcome: The robot will travel back to the beginning area while also having both blocks in it's possession.
# Test Cases

# Flowchart and Pseudocode