#!/usr/bin/env python3
import os
import rospy
from duckietown.dtros import DTROS, NodeType
from std_msgs.msg import String
from duckietown_msgs.msg import WheelsCmdStamped

class GestureMotorController(DTROS):

    def __init__(self):
        super(GestureMotorController, self).__init__(node_name='motor_controller_node', node_type=NodeType.GENERIC)
        self.vehicle_name = os.environ['VEHICLE_NAME']
        wheels_topic = f"/{self.vehicle_name}/wheels_driver_node/wheels_cmd"
        self.publisher = rospy.Publisher(wheels_topic, WheelsCmdStamped, queue_size=1)
        rospy.Subscriber('/gesture_command', String, self.callback)

    def callback(self, msg):
        command = msg.data.upper()
        cmd = WheelsCmdStamped()

        if command == "F":
            cmd.vel_left = 0.3
            cmd.vel_right = 0.3
        elif command == "L":
            cmd.vel_left = -0.2
            cmd.vel_right = 0.2
        elif command == "R":
            cmd.vel_left = 0.2
            cmd.vel_right = -0.2
        elif command == "S":
            cmd.vel_left = 0.0
            cmd.vel_right = 0.0
        else:
            rospy.logwarn(f"Unknown command: {command}")
            return

        rospy.loginfo(f"Executing movement: {command}")
        self.publisher.publish(cmd)

if __name__ == '__main__':
    node = GestureMotorController()
    rospy.spin()
