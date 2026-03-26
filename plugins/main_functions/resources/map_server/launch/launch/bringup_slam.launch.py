import os
from ament_index_python.packages import get_package_share_directory

import launch
from launch.substitutions import LaunchConfiguration
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node

    
def slam_toolbox(description):
    slam_params_file = LaunchConfiguration(
        'slam_params_file',
        default = os.path.join(
            get_package_share_directory("typeg"),
           'config',
           'navigation',
           'slam_toolbox.yaml')
        )

    slam_toolbox_node = Node(
    parameters=[
        {'slam_params_file':'./slam_toolbox.yaml'}
    ],
    package='slam_toolbox',
    executable='async_slam_toolbox_node',
    name='slam_toolbox',
    remappings=[('map', '/map_slam')],
    output='screen')
    
    description.add_action(slam_toolbox_node)


def generate_launch_description():
    launch_description = launch.LaunchDescription()
    slam_toolbox(launch_description)
    return launch_description
