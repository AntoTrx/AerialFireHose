cmake_minimum_required(VERSION 3.0.2)
project(air3d_planner)

# add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  nav_msgs
  qrotor_gazebo_plugin
  roscpp
  rospy
  message_generation
  std_msgs
  )
catkin_python_setup()

add_message_files(
  FILES
  BoolStamped.msg
  ParamsStamped.msg
)


generate_messages(
        DEPENDENCIES geometry_msgs std_msgs
)


generate_dynamic_reconfigure_options(
  cfg/MissionControl.cfg
)

