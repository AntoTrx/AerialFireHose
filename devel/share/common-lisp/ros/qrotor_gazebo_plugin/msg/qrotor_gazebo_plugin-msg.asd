
(cl:in-package :asdf)

(defsystem "qrotor_gazebo_plugin-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "Command" :depends-on ("_package_Command"))
    (:file "_package_Command" :depends-on ("_package"))
    (:file "Spline" :depends-on ("_package_Spline"))
    (:file "_package_Spline" :depends-on ("_package"))
  ))