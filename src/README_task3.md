ROS2 Autoware Autonomous Navigation Task

Overview
This task demonstrates autonomous navigation using ROS 2 Humble and Autoware. A prebuilt map is used for localization, and the vehicle navigates to goal positions using Autoware’s planning and control stack. A custom controller (aw_navigation.py) is used to interact with the system.

Required packages
sudo apt install ros-humble-autoware

Workspace Setup
Clone the repository: git clone https://github.com/YOUR_USERNAME/ros2_ws.git

Navigate to workspace: cd ~/ros2_ws
. /autoware_terminal.sh
Build workspace: . /build_ws.sh


Running Custom Navigation with the custom launch file:
ros2 launch my_robot_controller car_nav.launch.py

Important Change (Terminal Usage)

In this task,we use: . /autoware_terminal.sh
instead of: ./docker_terminal.sh
This opens a terminal with Autoware environment already sourced.

Also important!
In the file explorer home library there has to be the map file (for example home/autoware_map/sample_map_planning/). It can be found in my github repository 


Navigation Behavior
* The vehicle waits for an initial pose
* Localization is handled by Autoware
* A goal is set in RViz
* Autoware plans and executes the path
* The vehicle reaches the goal while avoiding obstacles
