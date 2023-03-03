cmake_minimum_required(VERSION 3.0.2)
project(air3d_viz)

# add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  rospy
  std_msgs
  nav_msgs
)

catkin_python_setup()

catkin_package(
 INCLUDE_DIRS 
#  LIBRARIES air3d_viz
 CATKIN_DEPENDS geometry_msgs rospy std_msgs nav_msgs
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)
