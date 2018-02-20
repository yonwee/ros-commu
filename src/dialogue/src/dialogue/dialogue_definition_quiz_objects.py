import random

from dialogue import Dialogue
from dialogue_action import *
from dialogue_manager import DialogueLibrary

import urllib2
import json


class DialogueLibraryQuiz(DialogueLibrary):
    """
    A DialogueLibrary that can be used when a CommU robot sees an object. This plays 'object hide-and-seek' with the user.
    """

    global f, utterance, cancelable, next_action, cjdata
    f = {}

    def get_dialogue_for_topic(self, topic):
        # type: (str) -> Dialogue
        """
        Get the dialogue that can be used when CommU sees an object.
        :param topic:   The label assigned by the ssd network
        :return:        The Dialogue concerning the object.
        """
        #self.funcheck()
        f[5] = self.request_script()
        for x in range (3,0,-1):            
            f[0]=str(x)
            self.funman()
            if x > 2:
                f[4] = DialogueActionTalkNoResponse(f[1], f[2], f[3])
            else:
                f[4] = DialogueActionTalkNoResponse(f[1], f[2], f[4])
        return Dialogue(f[4])
#         return Dialogue(DialogueActionTalkNoResponse(
#                             utterance="hey",
#                             cancelable=False,
#                             next_action=None))
        
    def request_script(self):
        convo = urllib2.urlopen('http://192.168.1.225:8080/?json={test}')
        cjson = convo.read()
        cjdata = json.loads(cjson)
        return cjdata
        
    def funman(self):
        #cjdata = self.request_script()
        utterance = f[5][f[0]]['1'].format(self.__get_object_noun(topic))
        cancelable = f[5][f[0]]['2']
        next_action = f[5][f[0]]['3'].replace("zz","None")
        f[1] = utterance
        f[2] = cancelable
        f[3] = next_action
       
#     def funcheck(self):
#         cjdata = self.request_script()
#         i = 1
#         j = str(i)
#         while cjdata[f[j]]['1']:
#             i = i + 1
#             f[5]=i

#     def __add_a_to_noun(self, noun):
#         # type: (str) -> str

#         if noun[0].lower() in ['a', 'e', 'i', 'o', 'u']:
#             return 'an ' + noun
#         else:
#             return 'a ' + noun

    def __get_object_noun(self, label):
        return self.object_proper_name_map.get(label, label)

    object_proper_name_map = {
        'aeroplane': 'airplane',
        'diningtable': 'dining table',
        'pottedplant': 'potted plant',
        'tvmonitor': 'screen'
    }
