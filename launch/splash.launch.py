from launch import LaunchDescription
from launch_ros.actions import Node
def generate_launch_description():
    return LaunchDescription([
        Node(package='Torcs_5', executable='splash_server'),
        Node(package='Torcs_5', executable='default_build_unit'),
    ])
