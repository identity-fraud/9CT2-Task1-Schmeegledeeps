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
>### __Scenario: The robot encounters an obstacle or the edge of the mat.__
>Inputs: The robot's ultrasonic sensor detects an object 10cm or less in front of it. The colour sensor then senses that it is an unwanted block colour.
>
>Actions: The robot rotates clockwise by 10° until the ultrasonic sensor can't see the object anymore.
>
>Expected Outcome: The robot continues moving, but in a different direction to avoid colliding with the obstacle.

>### **Scenario: The robot finds a block that it wants to grab.**
>Inputs: The robot detects an object in front of it using the ultrasonic sensor And the colour sensor sees that it is the right colour.
>
>Actions: The robot moves towards the object and uses a pincer attachment with a motor to clasp onto the object.
>
>Expected Outcome: The robot grabs and collects the object.

>### **Scenario: The robot has gathered a desired block, and must get back to the beginning.**
>Inputs: The robot uses the ultrasonic and colour sensor  detects an object with the colour it wants, and will gather it.
>
>Actions: The robot will move to the edge of the mat and begin to follow the mat's perimeter and slowly close in to the center in a spiral pattern. It will turn at corners.
>
>Expected Outcome: The robot will travel back to the beginning area while also having a block in it's possession. It will then restart the program to find the second object.
# Test Cases
| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
|Avoid Obstacle|The ultrasonic sensor detects an object within 10cm or less.|The robot stops moving, and spins 10° clockwise constantly until the unwanted object is out of its path.|
|Grab Block|The ultrasonic sensor detects an object within 10cm or less and the colour sensor detects that it is not an obstacle based on colour.|The robot will close the distance between it and the object. Once close enough, it will lower and close a motor-powered pincer/grabber arm and take the object.| 
|Go Back To Start|The robot uses the ultrasonic and colour sensors to find a desired object, and grabs it.|The robot will drive to the perimeter of the mat and will slowly follow it, moving smaller amounts for every "revolution" to bring it closer to the middle. Once in the middle, the robot will drive to the beginning easier.|
# Flowchart and Pseudocode
yeah
