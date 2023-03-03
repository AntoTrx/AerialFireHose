
(cl:in-package :asdf)

(defsystem "air3d_planner-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "BoolStamped" :depends-on ("_package_BoolStamped"))
    (:file "_package_BoolStamped" :depends-on ("_package"))
    (:file "ParamsStamped" :depends-on ("_package_ParamsStamped"))
    (:file "_package_ParamsStamped" :depends-on ("_package"))
  ))