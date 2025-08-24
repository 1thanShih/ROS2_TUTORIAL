#! /usr/bin/env python
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class Pose_sub(Node):

    def __init__(self):
        super().__init__('pose_sub')
        self.pose_suber = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
    
    def pose_callback(self, msg: Pose):
        self.get_logger().info(str(msg))

def main(args=None):
    rclpy.init(args=args)
    node = Pose_sub()
    rclpy.spin(node)
    rclpy.shutdown()
