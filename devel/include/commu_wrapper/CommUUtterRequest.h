// Generated by gencpp from file commu_wrapper/CommUUtterRequest.msg
// DO NOT EDIT!


#ifndef COMMU_WRAPPER_MESSAGE_COMMUUTTERREQUEST_H
#define COMMU_WRAPPER_MESSAGE_COMMUUTTERREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace commu_wrapper
{
template <class ContainerAllocator>
struct CommUUtterRequest_
{
  typedef CommUUtterRequest_<ContainerAllocator> Type;

  CommUUtterRequest_()
    : utterance()
    , blocking(false)
    , english(false)  {
    }
  CommUUtterRequest_(const ContainerAllocator& _alloc)
    : utterance(_alloc)
    , blocking(false)
    , english(false)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _utterance_type;
  _utterance_type utterance;

   typedef uint8_t _blocking_type;
  _blocking_type blocking;

   typedef uint8_t _english_type;
  _english_type english;




  typedef boost::shared_ptr< ::commu_wrapper::CommUUtterRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::commu_wrapper::CommUUtterRequest_<ContainerAllocator> const> ConstPtr;

}; // struct CommUUtterRequest_

typedef ::commu_wrapper::CommUUtterRequest_<std::allocator<void> > CommUUtterRequest;

typedef boost::shared_ptr< ::commu_wrapper::CommUUtterRequest > CommUUtterRequestPtr;
typedef boost::shared_ptr< ::commu_wrapper::CommUUtterRequest const> CommUUtterRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::commu_wrapper::CommUUtterRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::commu_wrapper::CommUUtterRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace commu_wrapper

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'sensor_msgs': ['/opt/ros/kinetic/share/sensor_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::commu_wrapper::CommUUtterRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::commu_wrapper::CommUUtterRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::commu_wrapper::CommUUtterRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::commu_wrapper::CommUUtterRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::commu_wrapper::CommUUtterRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::commu_wrapper::CommUUtterRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::commu_wrapper::CommUUtterRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "2afd6b4bdd4b8c861ea7fc877665051d";
  }

  static const char* value(const ::commu_wrapper::CommUUtterRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x2afd6b4bdd4b8c86ULL;
  static const uint64_t static_value2 = 0x1ea7fc877665051dULL;
};

template<class ContainerAllocator>
struct DataType< ::commu_wrapper::CommUUtterRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "commu_wrapper/CommUUtterRequest";
  }

  static const char* value(const ::commu_wrapper::CommUUtterRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::commu_wrapper::CommUUtterRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
string utterance\n\
\n\
\n\
\n\
bool blocking\n\
\n\
\n\
\n\
bool english\n\
";
  }

  static const char* value(const ::commu_wrapper::CommUUtterRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::commu_wrapper::CommUUtterRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.utterance);
      stream.next(m.blocking);
      stream.next(m.english);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct CommUUtterRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::commu_wrapper::CommUUtterRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::commu_wrapper::CommUUtterRequest_<ContainerAllocator>& v)
  {
    s << indent << "utterance: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.utterance);
    s << indent << "blocking: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.blocking);
    s << indent << "english: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.english);
  }
};

} // namespace message_operations
} // namespace ros

#endif // COMMU_WRAPPER_MESSAGE_COMMUUTTERREQUEST_H