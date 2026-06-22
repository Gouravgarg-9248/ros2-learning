#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

#===============================================================

class MyNode(Node):
    def __init__(self):
        super().__init__("first_node")
        # here "first_node" is the name of the node


        self.counter_ = 0   # it is just numbering that will be printed with each repeated message.

        # below line is used to repeat the message written in time_callback function after every 1.0 second gap
        self.create_timer(1.0, self.timer_callback)


    def timer_callback(self):

        # this is the message to be displayed:
        self.get_logger().info("Hello " + str(self.counter_))

        self.counter_ += 1  # just increasing the count after each message print
        
        
        # print("hello world")
          
        # we can also simply print a message like this, but ROS2 logging gives extra information like:
        # [INFO] - message type
        # 178211... - timestamp
        # furst_node - node name
        # Hello 1 - our message

#===============================================================

def main(args=None):
    
    rclpy.init(args=args)   #first line (first we have to initialize ros2 communications)
    node = MyNode()     # created node inside main()
    rclpy.spin(node)    # it keeps the node alive until we press { ctrl + c }

    rclpy.shutdown() #last line (shuting down ros2 communications)

#===============================================================

if __name__ == '__main__':
    main()