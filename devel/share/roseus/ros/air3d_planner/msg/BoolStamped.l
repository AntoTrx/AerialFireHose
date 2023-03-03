;; Auto-generated. Do not edit!


(when (boundp 'air3d_planner::BoolStamped)
  (if (not (find-package "AIR3D_PLANNER"))
    (make-package "AIR3D_PLANNER"))
  (shadow 'BoolStamped (find-package "AIR3D_PLANNER")))
(unless (find-package "AIR3D_PLANNER::BOOLSTAMPED")
  (make-package "AIR3D_PLANNER::BOOLSTAMPED"))

(in-package "ROS")
;;//! \htmlinclude BoolStamped.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass air3d_planner::BoolStamped
  :super ros::object
  :slots (_header _data ))

(defmethod air3d_planner::BoolStamped
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:data __data) nil)
    )
   (send-super :init)
   (setq _header __header)
   (setq _data __data)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:data
   (&optional (__data :null))
   (if (not (eq __data :null)) (setq _data __data)) _data)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; bool _data
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; bool _data
       (if _data (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; bool _data
     (setq _data (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get air3d_planner::BoolStamped :md5sum-) "542e22b190dc8e6eb476d50dda88feb7")
(setf (get air3d_planner::BoolStamped :datatype-) "air3d_planner/BoolStamped")
(setf (get air3d_planner::BoolStamped :definition-)
      "std_msgs/Header header
bool data
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



(provide :air3d_planner/BoolStamped "542e22b190dc8e6eb476d50dda88feb7")


