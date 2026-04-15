#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped
from action_msgs.msg import GoalStatusArray
import tf_transformations
import math
import time


class TurtleNavigationNode(Node):
    def __init__(self):
        super().__init__("navigation")
        self.get_logger().info("Navigation Node started")

        self.goal_poses = [
            {'x': -2.0, 'y': -1.5, 'yaw': -90},
            {'x': 0.0, 'y': -3.0, 'yaw': 180},
            {'x': -4.4, 'y': 7.0, 'yaw': -90},
            {'x': 2.0, 'y': 3.0, 'yaw': -90}
        ]

        self.current_goal_index = 0
        self.goal_reached = False

        self.initial_pose_publisher = self.create_publisher(
            PoseWithCovarianceStamped, "/initialpose", 10
        )
        self.goal_pose_publisher = self.create_publisher(
            PoseStamped, "/goal_pose", 10
        )

        self.nav_status_listener = self.create_subscription(
            GoalStatusArray,
            '/navigate_to_pose/_action/status',
            self.status_callback,
            10
        
)

        time.sleep(5)
        self.publish_initial_pose()
        time.sleep(5)
        self.publish_goal()

    def publish_initial_pose(self):
        initial_pose = PoseWithCovarianceStamped()
        initial_pose.header.frame_id = 'map'
        initial_pose.header.stamp = self.get_clock().now().to_msg()

        initial_pose.pose.pose.position.x = 1.8
        initial_pose.pose.pose.position.y = 0.5

        quaternion = tf_transformations.quaternion_from_euler(0, 0, 0)
        initial_pose.pose.pose.orientation.x = quaternion[0]
        initial_pose.pose.pose.orientation.y = quaternion[1]
        initial_pose.pose.pose.orientation.z = quaternion[2]
        initial_pose.pose.pose.orientation.w = quaternion[3]

        initial_pose.pose.covariance[0] = 0.25
        initial_pose.pose.covariance[7] = 0.25
        initial_pose.pose.covariance[35] = 0.0685

        self.initial_pose_publisher.publish(initial_pose)
        self.get_logger().info("Initial pose published")

    def pose_callback(self, msg: PoseWithCovarianceStamped):
        current_pose = msg.pose.pose
        goal_pose = self.goal_poses[self.current_goal_index]

        distance_to_goal = math.sqrt(
            (current_pose.position.x - goal_pose['x']) ** 2 +
            (current_pose.position.y - goal_pose['y']) ** 2
        )

        if distance_to_goal < 0.1 and not self.goal_reached:
            self.goal_reached = True
            self.get_logger().info(f"Reached goal {self.current_goal_index + 1}")
            self.publish_next_goal()

    def status_callback(self, msg: GoalStatusArray):

        if len(msg.status_list) == 0:
            return

        latest_status = msg.status_list[-1].status

        # STATUS_SUCCEEDED = 4
        if latest_status == 4:
            self.get_logger().info(
                f"Goal {self.current_goal_index + 1} completed by Nav2"
            )
            self.publish_next_goal()

    def publish_next_goal(self):
        if self.current_goal_index < len(self.goal_poses) - 1:
            self.current_goal_index += 1
            self.publish_goal()
        else:
            self.get_logger().info("All goals reached!")
            rclpy.shutdown()

    def publish_goal(self):
        self.goal_reached = False

        goal = self.goal_poses[self.current_goal_index]
        pose_msg = PoseStamped()
        pose_msg.header.frame_id = 'map'
        pose_msg.header.stamp = self.get_clock().now().to_msg()

        pose_msg.pose.position.x = goal['x']
        pose_msg.pose.position.y = goal['y']

        quaternion = tf_transformations.quaternion_from_euler(
            0, 0, math.radians(goal['yaw'])
        )
        pose_msg.pose.orientation.x = quaternion[0]
        pose_msg.pose.orientation.y = quaternion[1]
        pose_msg.pose.orientation.z = quaternion[2]
        pose_msg.pose.orientation.w = quaternion[3]

        time.sleep(0.5)
        self.goal_pose_publisher.publish(pose_msg)
        self.get_logger().info(
            f"Published goal {self.current_goal_index + 1}: "
            f"x={goal['x']}, y={goal['y']}, yaw={goal['yaw']}"
        )


def main(args=None):
    rclpy.init(args=args)
    node = TurtleNavigationNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Navigation Node stopped")
    finally:
        rclpy.shutdown()