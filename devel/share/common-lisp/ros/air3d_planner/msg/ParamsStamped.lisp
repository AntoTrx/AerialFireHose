; Auto-generated. Do not edit!


(cl:in-package air3d_planner-msg)


;//! \htmlinclude ParamsStamped.msg.html

(cl:defclass <ParamsStamped> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (height
    :reader height
    :initarg :height
    :type cl:float
    :initform 0.0)
   (width
    :reader width
    :initarg :width
    :type cl:float
    :initform 0.0)
   (inner_radius
    :reader inner_radius
    :initarg :inner_radius
    :type cl:float
    :initform 0.0))
)

(cl:defclass ParamsStamped (<ParamsStamped>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ParamsStamped>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ParamsStamped)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name air3d_planner-msg:<ParamsStamped> is deprecated: use air3d_planner-msg:ParamsStamped instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <ParamsStamped>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader air3d_planner-msg:header-val is deprecated.  Use air3d_planner-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'height-val :lambda-list '(m))
(cl:defmethod height-val ((m <ParamsStamped>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader air3d_planner-msg:height-val is deprecated.  Use air3d_planner-msg:height instead.")
  (height m))

(cl:ensure-generic-function 'width-val :lambda-list '(m))
(cl:defmethod width-val ((m <ParamsStamped>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader air3d_planner-msg:width-val is deprecated.  Use air3d_planner-msg:width instead.")
  (width m))

(cl:ensure-generic-function 'inner_radius-val :lambda-list '(m))
(cl:defmethod inner_radius-val ((m <ParamsStamped>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader air3d_planner-msg:inner_radius-val is deprecated.  Use air3d_planner-msg:inner_radius instead.")
  (inner_radius m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ParamsStamped>) ostream)
  "Serializes a message object of type '<ParamsStamped>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'height))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'width))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'inner_radius))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ParamsStamped>) istream)
  "Deserializes a message object of type '<ParamsStamped>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'height) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'width) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'inner_radius) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ParamsStamped>)))
  "Returns string type for a message object of type '<ParamsStamped>"
  "air3d_planner/ParamsStamped")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ParamsStamped)))
  "Returns string type for a message object of type 'ParamsStamped"
  "air3d_planner/ParamsStamped")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ParamsStamped>)))
  "Returns md5sum for a message object of type '<ParamsStamped>"
  "edeadafd57bc2f53e01759641dd723f9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ParamsStamped)))
  "Returns md5sum for a message object of type 'ParamsStamped"
  "edeadafd57bc2f53e01759641dd723f9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ParamsStamped>)))
  "Returns full string definition for message of type '<ParamsStamped>"
  (cl:format cl:nil "std_msgs/Header header~%float32 height~%float32 width~%float32 inner_radius~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ParamsStamped)))
  "Returns full string definition for message of type 'ParamsStamped"
  (cl:format cl:nil "std_msgs/Header header~%float32 height~%float32 width~%float32 inner_radius~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ParamsStamped>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ParamsStamped>))
  "Converts a ROS message object to a list"
  (cl:list 'ParamsStamped
    (cl:cons ':header (header msg))
    (cl:cons ':height (height msg))
    (cl:cons ':width (width msg))
    (cl:cons ':inner_radius (inner_radius msg))
))
