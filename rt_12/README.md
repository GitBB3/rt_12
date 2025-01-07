# rt_12
Assignment 2 (part 2) RT1

As the part 2 of the assignment was compared to the first exercise made in ROS2, here is the Step 1 of Assignment2 - Part 2, with the required behaviours in turtlesim environment.

## Exercise 1
The code implemented should:
- Call the service kill to remove turtle1 and spawn to add a new turtle
- Create a publisher/subscriber to the new turtle (topics cmd_vel and pose):
	- Check the types of messages and add the needed dependencies
	- Add a publisher and a subscriber
	- Publish a certain velocity in the callback
	
## Run it

source \opt\ros\foxy\local_setup.bash
ros2 launch rt_12 launch_part2_turtle.py

## Implementation

Implemented in rt_12/rt_12/turtle_move.py :
- client to kill turtle1
- client to spawn turtle2 in (5,5)
- publisher to publish speed of turtle2 once spawned
- subscriber with callback function to command the speed of turtle2

## Modify the speed
The command speed of turtle2 can be modified in the callback function "listener_callback", by giving values of linear speed Vx and angular speed Wz (line 42-43).

## Expected behaviour
Here, when launching the launchfile, the turtlesim environment is supposed to appear, then turtle1 is killed, turtle2 is spawned in (5,5) and then it moves in circles in the environment.
