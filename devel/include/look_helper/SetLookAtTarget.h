// Generated by gencpp from file look_helper/SetLookAtTarget.msg
// DO NOT EDIT!


#ifndef LOOK_HELPER_MESSAGE_SETLOOKATTARGET_H
#define LOOK_HELPER_MESSAGE_SETLOOKATTARGET_H

#include <ros/service_traits.h>


#include <look_helper/SetLookAtTargetRequest.h>
#include <look_helper/SetLookAtTargetResponse.h>


namespace look_helper
{

struct SetLookAtTarget
{

typedef SetLookAtTargetRequest Request;
typedef SetLookAtTargetResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct SetLookAtTarget
} // namespace look_helper


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::look_helper::SetLookAtTarget > {
  static const char* value()
  {
    return "1030478efebc9e6deae2c1ba1ffff144";
  }

  static const char* value(const ::look_helper::SetLookAtTarget&) { return value(); }
};

template<>
struct DataType< ::look_helper::SetLookAtTarget > {
  static const char* value()
  {
    return "look_helper/SetLookAtTarget";
  }

  static const char* value(const ::look_helper::SetLookAtTarget&) { return value(); }
};


// service_traits::MD5Sum< ::look_helper::SetLookAtTargetRequest> should match 
// service_traits::MD5Sum< ::look_helper::SetLookAtTarget > 
template<>
struct MD5Sum< ::look_helper::SetLookAtTargetRequest>
{
  static const char* value()
  {
    return MD5Sum< ::look_helper::SetLookAtTarget >::value();
  }
  static const char* value(const ::look_helper::SetLookAtTargetRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::look_helper::SetLookAtTargetRequest> should match 
// service_traits::DataType< ::look_helper::SetLookAtTarget > 
template<>
struct DataType< ::look_helper::SetLookAtTargetRequest>
{
  static const char* value()
  {
    return DataType< ::look_helper::SetLookAtTarget >::value();
  }
  static const char* value(const ::look_helper::SetLookAtTargetRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::look_helper::SetLookAtTargetResponse> should match 
// service_traits::MD5Sum< ::look_helper::SetLookAtTarget > 
template<>
struct MD5Sum< ::look_helper::SetLookAtTargetResponse>
{
  static const char* value()
  {
    return MD5Sum< ::look_helper::SetLookAtTarget >::value();
  }
  static const char* value(const ::look_helper::SetLookAtTargetResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::look_helper::SetLookAtTargetResponse> should match 
// service_traits::DataType< ::look_helper::SetLookAtTarget > 
template<>
struct DataType< ::look_helper::SetLookAtTargetResponse>
{
  static const char* value()
  {
    return DataType< ::look_helper::SetLookAtTarget >::value();
  }
  static const char* value(const ::look_helper::SetLookAtTargetResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // LOOK_HELPER_MESSAGE_SETLOOKATTARGET_H
