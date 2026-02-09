import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class DistanceSensor(Node):
    def __init__(self):
        super().__init__('distance_sensor')
        self.publisher=self.create_publisher(Int32,'distance',10)
        self.timer=self.create_timer(1.0,self.publish_distance)

    def publish_distance(self):
        msg=Int32()
        msg.data=random.randint(1,50)
        self.publisher.publish(msg)
        self.get_logger().info(f"Distance:{msg.data}")

def main():
    rclpy.init()
    node = DistanceSensor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()