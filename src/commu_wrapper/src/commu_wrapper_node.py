#!/usr/bin/env python

import rospy
from commu_wrapper.srv import CommUUtter, CommUUtterResponse, CommUUtterRequest, CommULook, CommULookResponse, \
    CommULookRequest, CommUMoveAdd, CommUMoveAddResponse, CommUMoveAddRequest, CommUMoveExec, CommUMoveExecResponse, \
    CommUMoveExecRequest

from debug_handler import DebugHandler
from wrapper import CommUWrapper


def utter_callback(wrapper):
    def utter(req):
        # type: (CommUUtterRequest) -> CommUUtterResponse
        success = wrapper.utter(req.utterance, req.blocking, req.english)

        return CommUUtterResponse(success)

    return utter

def look_callback(wrapper):
    def look(req):
        # type: (CommULookRequest) -> CommULookResponse

        success = wrapper.look(req.look_x, req.look_y, req.look_z)

        return CommULookResponse(success)

    return look

def move_add_callback(wrapper):
    def move_add(req):
        # type: (CommUMoveAddRequest) -> CommUMoveAddResponse

        success = wrapper.move_add(req.gesture_name, req.gesture_definition)

        return CommUMoveAddResponse(success)

    return move_add

def move_exec_callback(wrapper):
    def move_exec(req):
        # type: (CommUMoveExecRequest) -> CommUMoveExecResponse

        success = wrapper.move_exec(req.gesturefile)

        return CommUMoveExecResponse(success)

    return move_exec

def init_service_handlers(wrapper):
    rospy.loginfo("Initializing CommU wrapper node message listener.")

    rospy.Service('/commu_wrapper/utter', CommUUtter, utter_callback(wrapper))
    rospy.Service('/commu_wrapper/look', CommULook, look_callback(wrapper))
    rospy.Service('/commu_wrapper/move_add', CommUMoveAdd, move_add_callback(wrapper))
    rospy.Service('/commu_wrapper/move_exec', CommUMoveExec, move_exec_callback(wrapper))


if __name__ == '__main__':
    rospy.init_node("commu_wrapper")

    commu_ip = rospy.get_param("commu_wrapper/commu_ip", "127.0.0.1")
    commu_port = rospy.get_param("commu_wrapper/commu_port", "6009")
    commu_volume = rospy.get_param("commu_wrapper/commu_volume", 10)
    debug_mode = rospy.get_param("commu_wrapper/debug_mode", True)
    classification_topic = rospy.get_param("commu_wrapper/classification_topic", "/ssd_node/classification_result")

    rospy.loginfo("Starting commu_wrapper_node..")
    rospy.loginfo(
        """commu_wrapper initializing with: {
            commu_ip: %s,
            commu_port: %d,
            commu_volume: %f,
            debug_mode: %d,
            classification_topic: %s    
        }""", commu_ip, commu_port, commu_volume, debug_mode, classification_topic
    )


    if bool(debug_mode):
        wrapper = CommUWrapper(commu_ip, commu_port, commu_volume, DebugHandler(classification_topic))
    else:
        wrapper = CommUWrapper(commu_ip, commu_port, commu_volume)

    init_service_handlers(wrapper)

    rospy.spin()
