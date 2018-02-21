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

    global f, utterance, cancelable, next_action
    
    f = {}

    def get_dialogue_for_topic(self, topic):
        # type: (str) -> Dialogue
        """
        Get the dialogue that can be used when CommU sees an object.
        :param topic:   The label assigned by the ssd network
        :return:        The Dialogue concerning the object.
        """
        #self.request_script()
        f[5] = self.request_script()
        for x in range (3,0,-1):            
            f[0]=str(x)
            self.funman()
            if x > 2:
                f[4] =  DialogueActionSleep(
                    sleep_time=2,
                    cancelable=False,
                    next_action=DialogueActionTalkNoResponse(f[1].format(self.__get_object_noun(topic)), f[2], f[3])                                                   
            else:
                f[4] = DialogueActionTalkNoResponse(f[1].format(self.__get_object_noun(topic)), f[2], f[4])
        return Dialogue(f[4])
        
    def request_script(self):
        convo = urllib2.urlopen('http://192.168.1.225:8080/?json={test}')
        cjson = convo.read()
        cjdata = json.loads(cjson)
        return cjdata
        
    def funman(self):
        #cjdata = self.request_script()
        utterance = f[5][f[0]]['1']
        cancelable = f[5][f[0]]['2']
        next_action = None
        #next_action = f[5][f[0]]['3'].replace("zz","None")
        f[1] = utterance
        f[2] = cancelable
        f[3] = next_action

    def __get_object_noun(self, label):
        return self.object_proper_name_map.get(label, label)

    object_proper_name_map = {
        'aeroplane': 'airplane',
        'diningtable': 'dining table',
        'pottedplant': 'potted plant',
        'tvmonitor': 'screen'
    }
