#! /usr/bin/env python3
import rclpy # Import the rclpy library the rclpy library is essential for creating ROS 2 nodes in Python
from rclpy.node import Node # Import the Node class from rclpy.node, which is the base class for all ROS 2 nodes

class MyNode(Node):

    def __init__(self):
        super().__init__("node_name_is_this")
        self.get_logger().info("Hello from ROS!")

def main(args = None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':# for python3 executable entry point not for ROS 2
    main() 