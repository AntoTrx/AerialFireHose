// Auto-generated. Do not edit!

// (in-package qrotor_gazebo_plugin.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let Spline = require('./Spline.js');
let geometry_msgs = _finder('geometry_msgs');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class Command {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.mode = null;
      this.thrust = null;
      this.yaw = null;
      this.command = null;
      this.spline = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('mode')) {
        this.mode = initObj.mode
      }
      else {
        this.mode = 0;
      }
      if (initObj.hasOwnProperty('thrust')) {
        this.thrust = initObj.thrust
      }
      else {
        this.thrust = 0.0;
      }
      if (initObj.hasOwnProperty('yaw')) {
        this.yaw = initObj.yaw
      }
      else {
        this.yaw = [];
      }
      if (initObj.hasOwnProperty('command')) {
        this.command = initObj.command
      }
      else {
        this.command = [];
      }
      if (initObj.hasOwnProperty('spline')) {
        this.spline = initObj.spline
      }
      else {
        this.spline = new Spline();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Command
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [mode]
    bufferOffset = _serializer.uint8(obj.mode, buffer, bufferOffset);
    // Serialize message field [thrust]
    bufferOffset = _serializer.float64(obj.thrust, buffer, bufferOffset);
    // Serialize message field [yaw]
    bufferOffset = _arraySerializer.float64(obj.yaw, buffer, bufferOffset, null);
    // Serialize message field [command]
    // Serialize the length for message field [command]
    bufferOffset = _serializer.uint32(obj.command.length, buffer, bufferOffset);
    obj.command.forEach((val) => {
      bufferOffset = geometry_msgs.msg.Vector3.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [spline]
    bufferOffset = Spline.serialize(obj.spline, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Command
    let len;
    let data = new Command(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [mode]
    data.mode = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [thrust]
    data.thrust = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [yaw]
    data.yaw = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [command]
    // Deserialize array length for message field [command]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.command = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.command[i] = geometry_msgs.msg.Vector3.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [spline]
    data.spline = Spline.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    length += 8 * object.yaw.length;
    length += 24 * object.command.length;
    length += Spline.getMessageSize(object.spline);
    return length + 17;
  }

  static datatype() {
    // Returns string type for a message object
    return 'qrotor_gazebo_plugin/Command';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '0675820010bfd865d593e5dde5d5a059';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # Command msg 
    
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
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Command(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.mode !== undefined) {
      resolved.mode = msg.mode;
    }
    else {
      resolved.mode = 0
    }

    if (msg.thrust !== undefined) {
      resolved.thrust = msg.thrust;
    }
    else {
      resolved.thrust = 0.0
    }

    if (msg.yaw !== undefined) {
      resolved.yaw = msg.yaw;
    }
    else {
      resolved.yaw = []
    }

    if (msg.command !== undefined) {
      resolved.command = new Array(msg.command.length);
      for (let i = 0; i < resolved.command.length; ++i) {
        resolved.command[i] = geometry_msgs.msg.Vector3.Resolve(msg.command[i]);
      }
    }
    else {
      resolved.command = []
    }

    if (msg.spline !== undefined) {
      resolved.spline = Spline.Resolve(msg.spline)
    }
    else {
      resolved.spline = new Spline()
    }

    return resolved;
    }
};

// Constants for message
Command.Constants = {
  MODE_PASS_THROUGH: 0,
  MODE_ATTITUDE: 1,
  MODE_ATTITUDE_RATE: 2,
  MODE_THRUST_YAW: 3,
  MODE_THRUST_YAW_RATE: 4,
  MODE_POSITION: 5,
  MODE_POSITION_SPLINE: 6,
}

module.exports = Command;
