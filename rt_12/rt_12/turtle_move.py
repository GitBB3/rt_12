import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import Kill, Spawn
from turtlesim.msg import Pose

class TurtleMover(Node):
    def __init__(self):
        super().__init__('turtle_mover')
        self.publisher_ = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)
        
        self.cli1 = self.create_client(Kill, 'kill')  # Kill service
        while not self.cli1.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service kill not available, waiting again...')
        self.cli2 = self.create_client(Spawn, 'spawn')  # Spawn service
        while not self.cli2.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service spawn not available, waiting again...')
        
    def send_kill_request(self):
        self.kill_request = Kill.Request()
        self.kill_request.name = 'turtle1'

        future = self.cli1.call_async(self.kill_request)
        future.add_done_callback(self.kill_response_callback)
    def kill_response_callback(self, future):
    	self.get_logger().info("Turtle1 killed")
    
    def send_spawn_request(self):
        self.spawn_request = Spawn.Request()
        self.spawn_request.x = 5.0  # Position X
        self.spawn_request.y = 5.0  # Position Y
        self.spawn_request.theta = 0.0  # Orientation
        self.spawn_request.name = 'turtle2'

        future = self.cli2.call_async(self.spawn_request)
        future.add_done_callback(self.spawn_response_callback)
    def spawn_response_callback(self, future):
    	self.get_logger().info("Turtle2 spawned")
    
    def listener_callback(self, msg):
        move_cmd = Twist() # Create Twist message to send the speed command
        move_cmd.linear.x = 2.0  # Linear speed
        move_cmd.angular.z = 1.0  # Angular speed

        self.publisher_.publish(move_cmd)
        self.get_logger().info(f"Command: Vx={move_cmd.linear.x}, Wz={move_cmd.angular.z}")

def main(args=None):
    rclpy.init(args=args)
    node = TurtleMover()
    node.send_kill_request()
    node.send_spawn_request()
    node.create_subscription(
        Pose,
        'turtle2/pose',
        node.listener_callback,
        10)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

