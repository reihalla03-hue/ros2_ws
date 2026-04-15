ROS2 TurtleBot3 Autonomous Navigation Project

Overview
This project demonstrates autonomous navigation using ROS 2 Humble, Gazebo, and Nav2 with the TurtleBot3 robot.
A SLAM-generated occupancy grid map from the previous task is used for localization, and a custom mission script allows the robot to navigate through four predefined goal positions automatically. The robot follows sequential waypoints inside a custom Gazebo world while avoiding obstacles using the Nav2 navigation stack.

Required packages:
sudo apt install ros-humble-turtlebot3
sudo apt install ros-humble-navigation2 
sudo apt install ros-humble-nav2-bringup 
sudo apt install ros-humble-gazebo-ros

Workspace Setup
Clone the repository: git clone https://github.com/reihalla03-hue/ros2_ws
Navigate to workspace: cd ros2_ws
Build workspace: build_ws.sh

Running the Navigation Simulation

Launch the mapping environment: ros2 launch my_robot_controller run_navigation.launch.py
This launches:
-Gazebo simulation 
-TurtleBot3 robot 
-AMCL localization 
-Nav2 navigation stack 
-RViz visualization 
-autonomous waypoint navigation controller

The robot will localize itself inside the SLAM-generated map and move sequentially through four predefined goal positions.

Navigation Behavior
-The robot receives an initial pose 
-AMCL estimates robot position in the map frame 
-The mission node publishes waypoint goals 
-Nav2 plans paths between goals 
-The robot avoids obstacles using costmaps 
-The robot reaches all four goal positions autonomously
