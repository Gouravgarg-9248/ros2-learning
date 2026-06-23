#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCircleNode(Node):
    def __init__(self):
        super().__init__("draw_circle")

        # making a publisher
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        # here  twist == message type , "/turtle1/cmd_vel" == topic name , 10 == queue size
        # as we are going to interact with a build in nodes- these meassage type and name must be exactly same as it is.

        # creating a timer that will call the function every 0.5 seconds
        self.timer_ = self.create_timer(0.5, self.send_velocity_command)

        self.get_logger().info("Draw circle node has been started.")

    def send_velocity_command(self):

        #making a message
        msg = Twist()
        # filling some data in it
        msg.linear.x = 2.0
        msg.angular.z = 1.0

        # publishing the message with data
        self.cmd_vel_pub_.publish(msg)



def main(args = None):
    rclpy.init(args = args)

    node = DrawCircleNode()

    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()