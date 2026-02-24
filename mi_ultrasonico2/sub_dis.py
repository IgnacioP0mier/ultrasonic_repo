import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class Mysubscriber(Node):

    def __init__(self):
        super().__init__('mi_subscriptor')

        self.subscription = self.create_subscription(
            Int32,
            'ignaciop',
            self.listener_callback,
            10)

    def listener_callback(self, msg):

        numero = msg.data

        self.get_logger().info(f'Me llegó este número: {numero}')

        if numero == 5:
            self.get_logger().warn('!!! ALERTA !!!')


def main(args=None):
    rclpy.init(args=args)

    nodo = Mysubscriber()

    rclpy.spin(nodo)

    nodo.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()