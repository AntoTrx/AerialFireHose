;; Auto-generated. Do not edit!


(when (boundp 'qrotor_gazebo_plugin::Command)
  (if (not (find-package "QROTOR_GAZEBO_PLUGIN"))
    (make-package "QROTOR_GAZEBO_PLUGIN"))
  (shadow 'Command (find-package "QROTOR_GAZEBO_PLUGIN")))
(unless (find-package "QROTOR_GAZEBO_PLUGIN::COMMAND")
  (make-package "QROTOR_GAZEBO_PLUGIN::COMMAND"))

(in-package "ROS")
;;//! \htmlinclude Command.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(intern "*MODE_PASS_THROUGH*" (find-package "QROTOR_GAZEBO_PLUGIN::COMMAND"))
(shadow '*MODE_PASS_THROUGH* (find-package "QROTOR_GAZEBO_PLUGIN::COMMAND"))
(defconstant qrotor_gazebo_plugin::Command::*MODE_PASS_THROUGH* 0)
(intern "*MODE_ATTITUDE*" (find-package "QROTOR_GAZEBO_PLUGIN::COMMAND"))
(shadow '*MODE_ATTITUDE* (find-package "QROTOR_GAZEBO_PLUGIN::COMMAND"))
(defconstant qrotor_gazebo_plugin::Command::*MODE_ATTITUDE* 1)
(intern "*MODE_ATTITUDE_RATE*" (find-package "QROTOR_GAZEBO_PLUGIN::COMMAND"))
(shadow '*MODE_ATTITUDE_RATE* (find-package "QROTOR_GAZEBO_PLUGIN::COMMAND"))
(defconstant qrotor_gazebo_plugin::Command::*MODE_ATTITUDE_RATE* 2)
(intern "*MODE_THRUST_YAW*" (find-package "QROTOR_GAZEBO_PLUGIN::COMMAND"))
(shadow '*MODE_THRUST_YAW* (find-package "QROTOR_GAZEBO_PLUGIN::COMMAND"))
(defconstant qrotor_gazebo_plugin::Command::*MODE_THRUST_YAW* 3)
(intern "*MODE_THRUST_YAW_RATE*" (find-package "QROTOR_GAZEBO_PLUGIN::COMMAND"))
(shadow '*MODE_THRUST_YAW_RATE* (find-package "QROTOR_GAZEBO_PLUGIN::COMMAND"))
(defconstant qrotor_gazebo_plugin::Command::*MODE_THRUST_YAW_RATE* 4)
(intern "*MODE_POSITION*" (find-package "QROTOR_GAZEBO_PLUGIN::COMMAND"))
(shadow '*MODE_POSITION* (find-package "QROTOR_GAZEBO_PLUGIN::COMMAND"))
(defconstant qrotor_gazebo_plugin::Command::*MODE_POSITION* 5)
(intern "*MODE_POSITION_SPLINE*" (find-package "QROTOR_GAZEBO_PLUGIN::COMMAND"))
(shadow '*MODE_POSITION_SPLINE* (find-package "QROTOR_GAZEBO_PLUGIN::COMMAND"))
(defconstant qrotor_gazebo_plugin::Command::*MODE_POSITION_SPLINE* 6)

(defun qrotor_gazebo_plugin::Command-to-symbol (const)
  (cond
        ((= const 0) 'qrotor_gazebo_plugin::Command::*MODE_PASS_THROUGH*)
        ((= const 1) 'qrotor_gazebo_plugin::Command::*MODE_ATTITUDE*)
        ((= const 2) 'qrotor_gazebo_plugin::Command::*MODE_ATTITUDE_RATE*)
        ((= const 3) 'qrotor_gazebo_plugin::Command::*MODE_THRUST_YAW*)
        ((= const 4) 'qrotor_gazebo_plugin::Command::*MODE_THRUST_YAW_RATE*)
        ((= const 5) 'qrotor_gazebo_plugin::Command::*MODE_POSITION*)
        ((= const 6) 'qrotor_gazebo_plugin::Command::*MODE_POSITION_SPLINE*)
        (t nil)))

(defclass qrotor_gazebo_plugin::Command
  :super ros::object
  :slots (_header _mode _thrust _yaw _command _spline ))

(defmethod qrotor_gazebo_plugin::Command
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:mode __mode) 0)
    ((:thrust __thrust) 0.0)
    ((:yaw __yaw) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:command __command) ())
    ((:spline __spline) (instance qrotor_gazebo_plugin::Spline :init))
    )
   (send-super :init)
   (setq _header __header)
   (setq _mode (round __mode))
   (setq _thrust (float __thrust))
   (setq _yaw __yaw)
   (setq _command __command)
   (setq _spline __spline)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:mode
   (&optional __mode)
   (if __mode (setq _mode __mode)) _mode)
  (:thrust
   (&optional __thrust)
   (if __thrust (setq _thrust __thrust)) _thrust)
  (:yaw
   (&optional __yaw)
   (if __yaw (setq _yaw __yaw)) _yaw)
  (:command
   (&rest __command)
   (if (keywordp (car __command))
       (send* _command __command)
     (progn
       (if __command (setq _command (car __command)))
       _command)))
  (:spline
   (&rest __spline)
   (if (keywordp (car __spline))
       (send* _spline __spline)
     (progn
       (if __spline (setq _spline (car __spline)))
       _spline)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; uint8 _mode
    1
    ;; float64 _thrust
    8
    ;; float64[] _yaw
    (* 8    (length _yaw)) 4
    ;; geometry_msgs/Vector3[] _command
    (apply #'+ (send-all _command :serialization-length)) 4
    ;; qrotor_gazebo_plugin/Spline _spline
    (send _spline :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; uint8 _mode
       (write-byte _mode s)
     ;; float64 _thrust
       (sys::poke _thrust (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64[] _yaw
     (write-long (length _yaw) s)
     (dotimes (i (length _yaw))
       (sys::poke (elt _yaw i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; geometry_msgs/Vector3[] _command
     (write-long (length _command) s)
     (dolist (elem _command)
       (send elem :serialize s)
       )
     ;; qrotor_gazebo_plugin/Spline _spline
       (send _spline :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; uint8 _mode
     (setq _mode (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; float64 _thrust
     (setq _thrust (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64[] _yaw
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _yaw (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _yaw i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; geometry_msgs/Vector3[] _command
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _command (let (r) (dotimes (i n) (push (instance geometry_msgs::Vector3 :init) r)) r))
     (dolist (elem- _command)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; qrotor_gazebo_plugin/Spline _spline
     (send _spline :deserialize buf ptr-) (incf ptr- (send _spline :serialization-length))
   ;;
   self)
  )

(setf (get qrotor_gazebo_plugin::Command :md5sum-) "0675820010bfd865d593e5dde5d5a059")
(setf (get qrotor_gazebo_plugin::Command :datatype-) "qrotor_gazebo_plugin/Command")
(setf (get qrotor_gazebo_plugin::Command :definition-)
      "# Command msg 

# control mode flags
uint8 MODE_PASS_THROUGH = 0
uint8 MODE_ATTITUDE = 1
uint8 MODE_ATTITUDE_RATE = 2
uint8 MODE_THRUST_YAW = 3
uint8 MODE_THRUST_YAW_RATE = 4
uint8 MODE_POSITION = 5
uint8 MODE_POSITION_SPLINE = 6

# message
Header header
uint8 mode
float64 thrust
float64[] yaw
geometry_msgs/Vector3[] command
qrotor_gazebo_plugin/Spline spline
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
================================================================================
MSG: qrotor_gazebo_plugin/Spline
float64[] x
float64[] y
float64[] z
")



(provide :qrotor_gazebo_plugin/Command "0675820010bfd865d593e5dde5d5a059")


