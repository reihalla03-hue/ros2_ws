from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    return LaunchDescription([
        # Launch your custom TurtleBot3 simulation
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                PathJoinSubstitution([
                    FindPackageShare('my_robot_controller'),
                    'launch',
                    'turtlebot3_world.launch.py'
                ])
            ),
        ),

        # Launch SLAM
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                PathJoinSubstitution([
                    FindPackageShare('turtlebot3_cartographer'),
                    'launch',
                    'cartographer.launch.py'
                ])
            ),
            launch_arguments={'use_sim_time': 'True'}.items(),
        ),

        # Launch autonomous mapping node
        Node(
            package='my_robot_controller',
            executable='mapping',
            name='control',
            output='screen'
        )
    ])