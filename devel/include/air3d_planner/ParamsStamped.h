// Generated by gencpp from file air3d_planner/ParamsStamped.msg
// DO NOT EDIT!


#ifndef AIR3D_PLANNER_MESSAGE_PARAMSSTAMPED_H
#define AIR3D_PLANNER_MESSAGE_PARAMSSTAMPED_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace air3d_planner
{
template <class ContainerAllocator>
struct ParamsStamped_
{
  typedef ParamsStamped_<ContainerAllocator> Type;

  ParamsStamped_()
    : header()
    , height(0.0)
    , width(0.0)
    , inner_radius(0.0)  {
    }
  ParamsStamped_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , height(0.0)
    , width(0.0)
    , inner_radius(0.0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef float _height_type;
  _height_type height;

   typedef float _width_type;
  _width_type width;

   typedef float _inner_radius_type;
  _inner_radius_type inner_radius;





  typedef boost::shared_ptr< ::air3d_planner::ParamsStamped_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::air3d_planner::ParamsStamped_<ContainerAllocator> const> ConstPtr;

}; // struct ParamsStamped_

typedef ::air3d_planner::ParamsStamped_<std::allocator<void> > ParamsStamped;

typedef boost::shared_ptr< ::air3d_planner::ParamsStamped > ParamsStampedPtr;
typedef boost::shared_ptr< ::air3d_planner::ParamsStamped const> ParamsStampedConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::air3d_planner::ParamsStamped_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::air3d_planner::ParamsStamped_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::air3d_planner::ParamsStamped_<ContainerAllocator1> & lhs, const ::air3d_planner::ParamsStamped_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.height == rhs.height &&
    lhs.width == rhs.width &&
    lhs.inner_radius == rhs.inner_radius;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::air3d_planner::ParamsStamped_<ContainerAllocator1> & lhs, const ::air3d_planner::ParamsStamped_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace air3d_planner

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::air3d_planner::ParamsStamped_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::air3d_planner::ParamsStamped_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::air3d_planner::ParamsStamped_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::air3d_planner::ParamsStamped_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::air3d_planner::ParamsStamped_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::air3d_planner::ParamsStamped_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::air3d_planner::ParamsStamped_<ContainerAllocator> >
{
  static const char* value()
  {
    return "edeadafd57bc2f53e01759641dd723f9";
  }

  static const char* value(const ::air3d_planner::ParamsStamped_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xedeadafd57bc2f53ULL;
  static const uint64_t static_value2 = 0xe01759641dd723f9ULL;
};

template<class ContainerAllocator>
struct DataType< ::air3d_planner::ParamsStamped_<ContainerAllocator> >
{
  static const char* value()
  {
    return "air3d_planner/ParamsStamped";
  }

  static const char* value(const ::air3d_planner::ParamsStamped_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::air3d_planner::ParamsStamped_<ContainerAllocator> >
{
  static const char* value()
  {
    return "std_msgs/Header header\n"
"float32 height\n"
"float32 width\n"
"float32 inner_radius\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
;
  }

  static const char* value(const ::air3d_planner::ParamsStamped_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::air3d_planner::ParamsStamped_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.height);
      stream.next(m.width);
      stream.next(m.inner_radius);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ParamsStamped_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::air3d_planner::ParamsStamped_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::air3d_planner::ParamsStamped_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "height: ";
    Printer<float>::stream(s, indent + "  ", v.height);
    s << indent << "width: ";
    Printer<float>::stream(s, indent + "  ", v.width);
    s << indent << "inner_radius: ";
    Printer<float>::stream(s, indent + "  ", v.inner_radius);
  }
};

} // namespace message_operations
} // namespace ros

#endif // AIR3D_PLANNER_MESSAGE_PARAMSSTAMPED_H
