from launch_ros.actions import Node
from moveit_configs_utils import MoveItConfigsBuilder

from launch import LaunchDescription


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("moveit_resources_panda").to_dict()

    # MTC Demo node
    pick_place_demo = Node(
        package="mtc_tutorial",
        executable="mtc_tutorial",
        output="screen",
        parameters=[
            moveit_config,
        ],
    )

    return LaunchDescription([pick_place_demo])