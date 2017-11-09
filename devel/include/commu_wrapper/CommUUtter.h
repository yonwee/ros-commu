// Generated by gencpp from file commu_wrapper/CommUUtter.msg
// DO NOT EDIT!


#ifndef COMMU_WRAPPER_MESSAGE_COMMUUTTER_H
#define COMMU_WRAPPER_MESSAGE_COMMUUTTER_H

#include <ros/service_traits.h>


#include <commu_wrapper/CommUUtterRequest.h>
#include <commu_wrapper/CommUUtterResponse.h>


namespace commu_wrapper
{

struct CommUUtter
{

typedef CommUUtterRequest Request;
typedef CommUUtterResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct CommUUtter
} // namespace commu_wrapper


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::commu_wrapper::CommUUtter > {
  static const char* value()
  {
    return "fc4efb8806f0415eaa9b069b92459024";
  }

  static const char* value(const ::commu_wrapper::CommUUtter&) { return value(); }
};

template<>
struct DataType< ::commu_wrapper::CommUUtter > {
  static const char* value()
  {
    return "commu_wrapper/CommUUtter";
  }

  static const char* value(const ::commu_wrapper::CommUUtter&) { return value(); }
};


// service_traits::MD5Sum< ::commu_wrapper::CommUUtterRequest> should match 
// service_traits::MD5Sum< ::commu_wrapper::CommUUtter > 
template<>
struct MD5Sum< ::commu_wrapper::CommUUtterRequest>
{
  static const char* value()
  {
    return MD5Sum< ::commu_wrapper::CommUUtter >::value();
  }
  static const char* value(const ::commu_wrapper::CommUUtterRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::commu_wrapper::CommUUtterRequest> should match 
// service_traits::DataType< ::commu_wrapper::CommUUtter > 
template<>
struct DataType< ::commu_wrapper::CommUUtterRequest>
{
  static const char* value()
  {
    return DataType< ::commu_wrapper::CommUUtter >::value();
  }
  static const char* value(const ::commu_wrapper::CommUUtterRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::commu_wrapper::CommUUtterResponse> should match 
// service_traits::MD5Sum< ::commu_wrapper::CommUUtter > 
template<>
struct MD5Sum< ::commu_wrapper::CommUUtterResponse>
{
  static const char* value()
  {
    return MD5Sum< ::commu_wrapper::CommUUtter >::value();
  }
  static const char* value(const ::commu_wrapper::CommUUtterResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::commu_wrapper::CommUUtterResponse> should match 
// service_traits::DataType< ::commu_wrapper::CommUUtter > 
template<>
struct DataType< ::commu_wrapper::CommUUtterResponse>
{
  static const char* value()
  {
    return DataType< ::commu_wrapper::CommUUtter >::value();
  }
  static const char* value(const ::commu_wrapper::CommUUtterResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // COMMU_WRAPPER_MESSAGE_COMMUUTTER_H