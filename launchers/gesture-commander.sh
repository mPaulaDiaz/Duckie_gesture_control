#!/bin/bash

source /environment.sh

# initialize launch file
dt-launchfile-init

# launch the TCP→ROS bridge node
rosrun gesture_control tcp_server.py &

# launch the gesture → motor controller node
rosrun gesture_control motor_controller_node.py &

# wait for app to end
dt-launchfile-join
