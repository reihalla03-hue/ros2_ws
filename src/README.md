ROS2 TurtleBot3 Autonomous Mapping Project

Overview
This project demonstrates autonomous mapping using ROS 2 Humble, Gazebo, and Cartographer SLAM with the TurtleBot3 robot.
A custom Gazebo environment was created and explored using a simple obstacle-avoidance controller that allowed the robot to navigate the environment and generate a 2D occupancy grid map.
The final map was saved using the ROS2 map server and exported as `.pgm` and `.yaml` files.

Required packages:
sudo apt install ros-humble-turtlebot3
sudo apt install ros-humble-cartographer
sudo apt install ros-humble-cartographer-ros
sudo apt install ros-humble-nav2-map-server

Workspace Setup
Clone the repository: git clone <your_repository_link>
Navigate to workspace: cd ros2_ws
Build workspace: source /opt/ros/humble/setup.bash
colcon build --symlink-install
source install/setup.bash

Running the Mapping Simulation

Launch the mapping environment: ros2 launch my_robot_controller start_mapping.launch.py
This launches:
-Gazebo simulation
-TurtleBot3 robot
-Cartographer SLAM
-autonomous mapping controller
The robot will explore the custom world and generate a map in RViz.

Saving the Map

After mapping finishes:
ros2 run nav2_map_server map_saver_cli -f ~/ws/src/my_robot_controller/maps/my_map

This generates:
my_map.pgm
my_map.yaml

inside:
my_robot_controller/maps/