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

    global f, utterance, cancelable, next_action, i
    f = {}

    def get_dialogue_for_topic(self, topic):
        # type: (str) -> Dialogue
        """
        Get the dialogue that can be used when CommU sees an object.
        :param topic:   The label assigned by the ssd network
        :return:        The Dialogue concerning the object.
        """
        self.funcheck()

        for x in range (3,0,-1):            
            f[0]=str(x)
            self.funman()
            if x > 2:
                f[4] = DialogueActionTalkNoResponse(f[1], f[2], f[3])
            if x < 3:
                if x > 0:
                    f[4] = DialogueActionTalkNoResponse(f[1], f[2], f[4])
                else: break
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
        cjdata = self.request_script()
        utterance = cjdata[f[0]]['1']
        cancelable = cjdata[f[0]]['2']
        next_action = cjdata[f[0]]['3']
        f[1] = utterance
        f[2] = cancelable
        f[3] = next_action
       
    def funcheck(self):
        cjdata = self.request_script()
        i = 1
        while = cjdata[f[i]]['1']:
            i = i + 1
