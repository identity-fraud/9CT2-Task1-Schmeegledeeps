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
* Move forward until an object is detected in front of the robot (within 10cm) using the ultrasonic sensor then turn 90° if the target isn't red or yellow (using the colour sensor)
* Move forward until one of the boxes (Red and Yellow) are found, then pick the boxes up using pincers attachment (using the motors)
* Turn 180° when the edge of the mat is detected (using the colour sensor's reflection function to identify the difference between the floor and the mat)

## Non-functional requirements:
* High response time
* Should be accurate
* Also should be efficient


# Use Cases
Scenario: The robot encounters an obstacle or the edge of the mat.
Inputs: The robot's ultrasonic sensor detects an unwanted object or area 10cm in front of it.
Actions: The robot rotates clockwise by 10° until the ultrasonic sensor can't see the object anymore.
Outcome: The robot continues moving, but in a different direction to avoid colliding with the obstacle.

Scenario: The robot finds a block that it wants to grab.
Inputs: The robot moves towards the object until it reached the object within 10cm in front
Actions: The robot uses a pincer attachment with the motor in the attachment to grab the object and moves to the destination

# Test Cases

# Flowchart and Pseudocode