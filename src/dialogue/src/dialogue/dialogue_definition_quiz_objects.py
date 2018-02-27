import random
import rospy

from dialogue import Dialogue
from dialogue_action import *
from dialogue_manager import DialogueLibrary

# from gestures import *
from commu_wrapper.src.helper.robot.cumhelper import CUMHelper
# from commu_wrapper.srv import CommUMoveExec

import urllib2
import json

class DialogueLibraryQuiz(DialogueLibrary):
    """
    A DialogueLibrary that can be used when a CommU robot sees an object. This plays 'object hide-and-seek' with the user.
    """

    global utterance, cancelable, next_action, store
    store = {}


    def get_dialogue_for_topic(self, topic):
        # type: (str) -> Dialogue
        """
        Get the dialogue that can be used when CommU sees an object.
        :param topic:   The label assigned by the ssd network
        :return:        The Dialogue concerning the object.
        """
        #return Dialogue(DialogueActionTalkNoResponse(utterance='heya', cancelable=False, next_action=None))

        cjdata = self.request_script()
        store['full'] = cjdata
        x=1
        store['block'] = self.assign_return_dia(x)
#         return Dialogue(store['block'])
#         rospy.ServiceProxy('/commu_wrapper/move_exec ', CommUMoveExec)
        manager = CUMHelper("10.42.0.159", int(6001))
        manager.say_eng("Hello, I am CommU.")
        return Dialogue(DialogueActionTalkNoResponse(
            utterance='hey',
            cancelable=False,
            next_action=None
            # next_action=DialogueActionTalkBanzaiResponse(
            #     gesture_file='banzai',
            #     # gesture_file=open('gestures/banzai.s3r'),
            #     cancelable=False,
            #     next_action=None)
            ))

    def request_script(self):
        convo = urllib2.urlopen('http://192.168.1.166:9000/?json={test}')
        cjson = convo.read()
        cjdata = json.loads(cjson)
        #cjdata = convos[1]
        return cjdata

    def assign_return_dia(self,x):
        curint = str(x)
        if store['full'][curint]['type']=='last':
            return DialogueActionTalkNoResponse(
                store['full'][curint]['u'],
                store['full'][curint]['c'],
                next_action=None)
        if store['full'][curint]['type']=='pass':
            next = int(store['full'][curint]['next'])
            return DialogueActionTalkNoResponse(
                store['full'][curint]['u'],
                store['full'][curint]['c'],
                next_action=self.assign_return_dia(next)) 
        if store['full'][curint]['type']=='binary':
            yesloc = int(store['full'][curint]['yesloc'])
            noloc  = int(store['full'][curint]['noloc'])
#             neuloc = int(store['full'][curint]['neuloc'])
            return DialogueActionTalkBinaryResponse(
                store['full'][curint]['u'],
                store['full'][curint]['c'],next_action_yes=self.assign_return_dia(yesloc),
                next_action_no=self.assign_return_dia(noloc))


#     @staticmethod
#     def return_bby(self):
# #         service_name = 'look_helper/look_target'
#         set_move_exec = rospy.ServiceProxy('gesture/banzai', CommUMoveExec)
#         return set_move_exec

#     def return_arb_dia(self):
#         return DialogueActionTalkNoResponse(utterance='yes',cancelable=False,next_action=self.return_none_bby())
                
    def __get_object_noun(self, label):
        return self.object_proper_name_map.get(label, label)

    object_proper_name_map = {
        'aeroplane': 'airplane',
        'diningtable': 'dining table',
        'pottedplant': 'potted plant',
        'tvmonitor': 'screen'
    }
