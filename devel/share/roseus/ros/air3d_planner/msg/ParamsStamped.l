;; Auto-generated. Do not edit!


(when (boundp 'air3d_planner::ParamsStamped)
  (if (not (find-package "AIR3D_PLANNER"))
    (make-package "AIR3D_PLANNER"))
  (shadow 'ParamsStamped (find-package "AIR3D_PLANNER")))
(unless (find-package "AIR3D_PLANNER::PARAMSSTAMPED")
  (make-package "AIR3D_PLANNER::PARAMSSTAMPED"))

(in-package "ROS")
;;//! \htmlinclude ParamsStamped.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass air3d_planner::ParamsStamped
  :super ros::object
  :slots (_header _height _width _inner_radius ))

(defmethod air3d_planner::ParamsStamped
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:height __height) 0.0)
    ((:width __width) 0.0)
    ((:inner_radius __inner_radius) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _height (float __height))
   (setq _width (float __width))
   (setq _inner_radius (float __inner_radius))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:height
   (&optional __height)
   (if __height (setq _height __height)) _height)
  (:width
   (&optional __width)
   (if __width (setq _width __width)) _width)
  (:inner_radius
   (&optional __inner_radius)
   (if __inner_radius (setq _inner_radius __inner_radius)) _inner_radius)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32 _height
    4
    ;; float32 _width
    4
    ;; float32 _inner_radius
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float32 _height
       (sys::poke _height (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _width
       (sys::poke _width (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _inner_radius
       (sys::poke _inner_radius (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32 _height
     (setq _height (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _width
     (setq _width (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _inner_radius
     (setq _inner_radius (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get air3d_planner::ParamsStamped :md5sum-) "edeadafd57bc2f53e01759641dd723f9")
(setf (get air3d_planner::ParamsStamped :datatype-) "air3d_planner/ParamsStamped")
(setf (get air3d_planner::ParamsStamped :definition-)
      "std_msgs/Header header
float32 height
float32 width
float32 inner_radius
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

")



(provide :air3d_planner/ParamsStamped "edeadafd57bc2f53e01759641dd723f9")


