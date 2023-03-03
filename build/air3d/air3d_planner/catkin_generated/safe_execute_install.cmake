execute_process(COMMAND "/home/vincent/catkin_ws2/build/air3d/air3d_planner/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/vincent/catkin_ws2/build/air3d/air3d_planner/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
