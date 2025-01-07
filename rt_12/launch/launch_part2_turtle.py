from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='turtlesim', executable='turtlesim_node', name='turtlesim_node'
        ),
        Node(package='rt_12', executable='ex1_turtles', name='ex1_turtles'
        ),
    ])

