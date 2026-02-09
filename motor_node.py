import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MotorNode(Node):
    def __init__(self):
        super().__init__('motor_node')
        self.subscription=self.create_subscription(String,'motion_command',self.command_callback,10)
    def command_callback(self,msg):
        self.get_logger().info(f"Moto command:{msg.data}")
def main():
    rclpy.init()
    node = MotorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()