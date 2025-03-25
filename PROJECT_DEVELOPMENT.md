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
* Move forward until an object is detected in front of the robot (within 10cm) using the ultrasonic sensor then turn 90° if the target isn't red or yellow (using the colour sensor)
* Move forward until one of the boxes (Red and Yellow) are found, then pick the boxes up using pincers attachment (using the motors)
* Turn 180° when the edge of the mat is detected (using the colour sensor's reflection function to identify the difference between the floor and the mat)

## Non-functional requirements:
* High response time
* Should be accurate
* Also should be efficient


# Use Cases
Scenario: Robot must navigate through a maze
Inputs: The robot moves forever until it detects an object within 10cm in front of it
Actions: The robot spins 90° and continues moving forever
Outcome: The robot continues moving forever and turning away from obstacles until it escapes the maze

Scenario: Robot much pick up an object and move it to a destination
Inputs: The robot moves towards the object until it reached the object within 10cm in front
Actions: The robot uses a pincer attachment with the motor in the attachment to grab the object and moves to the destination

# Flowchat and Pseudocode