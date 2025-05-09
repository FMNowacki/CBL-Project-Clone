from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # SLAM Toolbox Node
        Node(
            package='slam_toolbox',
            executable='sync_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[{
                'use_sim_time': True
            }]
        ),
        # TurtleBot3 Navigation Node
        Node(
            package='turtlebot3_navigation2',
            executable='navigate_to_pose',
            name='turtlebot3_navigation',
            output='screen'
        ),
        # Frontier Exploration Node
        Node(
            package='my_ros2_package',
            executable='frontier_exploration',
            name='frontier_exploration',
            output='screen'
        ),
        # RViz Visualization
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', 'rviz/slam_visualization.rviz']
        )
    ])