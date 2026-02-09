import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from std_msgs.msg import String

class DecisionNode(Node):
    def __init__(self):
        super().__init__('decision_node')
        self.subscription=self.create_subscription(Int32,'distance',self.distance_callback,10)
        self.publisher=self.create_publisher(String,'motion_command',10)
    def distance_callback(self,msg):
        distance=msg.data
        command=String()
        if distance<10:
            command.data="STOP"
        else:
            command.data="MOVE"
        self.publisher.publish(command)
        self.get_logger().info(f"Decision made for distance {distance}: {command.data}")

def main():
    rclpy.init()
    node = DecisionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
