# RT1_assignment1

### How to run the code
We should open three different prompts, beside the one where we run "roscore". In the first one we lunch the simulator by executing the command:
```
rosrun stage_ros stageros $(rospack find assignment1)/world/exercise.world."
```
In the third and in the fourth window we can run the two nodes by executing:
```
rosrun assignment1 ProcessOne.py
```
 and
``` 
rosrun assignment1 ProcessTwo.py
```
### Description of the content

The package contains two ros nodes (randomTarget_server and robot_controller) and one server (values).

The service server is implemented in ProcessOne. Among the libraries imported we have assignment1.srv, that allows us to use the service "values". By doing this we can also use valuesRequest() and valuesResponse().
In the main we created the node, with the name "randomTarget_server", and initialized a server, "random_target", which is of type values. When The callback function myrandom is invoked every time a new service request is received. 
When a request is made by the client, as output, it returns two random coordinates as response, which are generated from the function "randMtoN".
The coordinates are generated whitin a certain interval given by a fixed minimum and maximum value.

In ProcessTwo we have the client which makes the request and wait for the response from the server, the subscriber which provides the position of the robot throught the topic Odom and the publisher.
In the main we created the node, with the name "robot_controller" and initialized the service, publisher and subscriber.
The client issues service requests to the service random_target which is of srv values type.
The callback function of the subscriber is called each time a new message is pubblshed to the topyc Odom and is saved in msg. In this way we can have the current position of the robot.
Then, we defined the distance, with respect to x and y, as the difference between the position of the target and the current position and set the condition to determine if the target is reached. In our case, the values were provided by the assignment.
If the range is respected, we can ask the client to make another request for a new target. Otherwise, we define a lineare velocity proportional to the distance. 
