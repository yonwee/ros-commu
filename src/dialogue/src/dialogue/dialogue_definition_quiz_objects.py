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

        # return Dialogue(DialogueLibraryQuiz.select_convo(self,topic))
        # return Dialogue(self.dialogue_string_test())
#         x = 3
#         f[0]=str(x)
#         self.funman()
#         f[4] = (DialogueActionTalkNoResponse(f[1], f[2], f[3]))
#         f[4]=0

###################################################################################################
#          xinhai is hungry
#         f[1] = utterance
#         f[2] = cancelable
#         f[3] = next_action
#         f[6] = next_action_yes
#         f[7] = next_action_no
###################################################################################################     
        
        f[5] = self.request_script()
        self.funman()
#         a = len(f[5])
#         for x in range (a,0,-1):            
#             f[0]=str(x)
#             self.funman()
#             if x == a:
#                 f[4] =  DialogueActionSleep(
#                     sleep_time=1,
#                     cancelable=False,
#                     next_action=DialogueActionTalkNoResponse(f[1].format(self.__get_object_noun(topic)), f[2], f[3]))                                                   
#             else:
        f[0] = '1'
        if f[5][f[0]]['3'] == "Binary":
# #                     f[4] = DialogueActionTalkBinaryResponse(f[1].format(self.__get_object_noun(topic)), f[2], f[6], f[7])
            f[4] = DialogueActionTalkNoResponse(
                    utterance="hey",
                    cancelable=False,
                    next_action=None)
#                 else:
#                     f[4] = DialogueActionTalkNoResponse(f[1].format(self.__get_object_noun(topic)), f[2], f[4])
        return Dialogue(f[4])
#         return Dialogue(DialogueActionTalkNoResponse(
#                             utterance="hey",
#                             cancelable=False,
#                             next_action=None))
    
    
    def request_script(self):
        convo = urllib2.urlopen('http://192.168.1.225:8080/?json={test}')
        cjson = convo.read()
        cjdata = json.loads(cjson)
        #keyvar = "1"
        #dia = cjdata[keyvar]['1']
        return cjdata
    
    
    def funman(self):
        #cjdata = self.request_script()
        #keyvar = "1"
        utterance = f[5][f[0]]['1']
        cancelable = f[5][f[0]]['2']
#         if f[5][f[0]]['3'] is "None":           
        next_action = None
#         else:
#             next_action = f[5][f[0]]['3']
        next_action_yes=0
        next_action_no=0
        #utterance="hey"
        #cancelable=False
#         next_action=None
        f[1] = utterance
        f[2] = cancelable
        f[3] = next_action
        f[6] = next_action_yes
        f[7] = next_action_no

    #         return Dialogue(
    #             DialogueActionTalkNoResponse(
    #                             utterance="hey",
    #                             cancelable=False,
    #                             next_action=None
    #             )
    #         )
    # """
#                 DialogueActionLook(
#                     look_type=DialogueActionLook.LOOK_TYPE_WATCH_CONVERSATION_PARTNER,
#                     cancelable=False,
#                     next_action=
#                     DialogueActionSleep(
#                         sleep_time=1,
#                         cancelable=False,
#                         next_action=
    #                     DialogueActionTalkBinaryResponse(
    #                         utterance="Do you also see {}?".format(self.__add_a_to_noun(self.__get_object_noun(topic))),
    #                         cancelable=False,
    #                         next_action_yes=
    #                         DialogueActionTalkNoResponse(
    #                             utterance="hey",
    #                             cancelable=False,
    #                             next_action=None   
    #                             #utterance=random.choice(self.positive_response_list)
    #                             #utterance=self.dialogue_string_test().format(self.__add_a_to_noun(self.__get_object_noun(topic))),
    #                             #self.funman2(),
    #                             #exec(self.dialogue_string_test()),
    #                             #self.funman(),
    #                             cancelable=False,
    #                             #cancelable=self.dialogue_string_test(),
    #                             next_action=
    #                             DialogueActionLook(
    #                                 look_type=DialogueActionLook.LOOK_TYPE_WATCH_ENVIRONMENT,
    #                                 cancelable=True,
    #                                 next_action=None
    #                             )
    #                         ),
    #                         next_action_no=
    #                         DialogueActionLook(
    #                             look_type=DialogueActionLook.LOOK_TYPE_WATCH_CONVERSATION_TOPIC,
    #                             cancelable=False,
    #                             next_action=
    #                             DialogueActionTalkNoResponse(
    #                                 utterance=random.choice(self.negative_response_list),
    #                                 cancelable=False,
    #                                 next_action=
#                                     DialogueActionSleep(
#                                         sleep_time=2,
#                                         cancelable=False,
    #                                     next_action=DialogueActionLook(
    #                                         look_type=DialogueActionLook.LOOK_TYPE_WATCH_ENVIRONMENT,
    #                                         cancelable=True,
    #                                         next_action=None
    #                                     )
    #                                 )
    #                             ),
    #                         )
    #                     )
    #                 )
    #             )
    #         )        
    # """

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

#     positive_response_list = [
#         "Cool, you're good!",
#         "Nice, me too!",
#         "I see it too!"
#     ]

#     negative_response_list = [
#         "I see it over there",
#         "It's over there",
#         "I can help you. It's over here"
#     ]

    #    def dialogue_string_test(self):
    #        i=1
    #        cjdata = self.request_script()
    #        #dia = self.generation(cjdata,i)
    #        keyvar = "1"
    #        #dia = 'utterance=' + cjdata[keyvar]['1']
    #        #dia = cjdata[keyvar]['1']
    #        return cjdata
   
        

        # def generation(self, cjdata, i):
        # fulldialogue = ''
        # 
        # dialogueA = 'DialogueActionTalkNoResponse('
        # dialogueU = 'utterance="' + cjdata[keyvar]['1']
        # dialogueC = '",cancelable="'
        # dialogueN = '",next_action='
        # try:
        #     i += 1
        #     # utterance  = u
        #     # cancelable = c
        #     # nextaction = n
        #     keyvar = str(i)
        #     fulldialogue += dialogueA
        #     fulldialogue += dialogueU
        #     fulldialogue += cjdata[keyvar]['1']
        #     fulldialogue += dialogueC
        #     fulldialogue += cjdata[keyvar]['2']
        #     fulldialogue += dialogueN
        #     fulldialogue += self.generation(cjdata, i)
        # except KeyError:
        #     return "None" + ')'
        # return fulldialogue 

# def funman(self):
# return exec(self.dialogue_string_test())

#    def funman2(self):
#        code = compile(dialogue_string_test, '<string>', 'exec')
#        exec (code)

#     def funcheck(self):
#         f[5] = self.request_script()
#         i = 1
#         j = str(i)
#         while f[5][f[j]]['1']:
#             i = i + 1
#         f[6]=i

################# kurisu ##################
# import random

# from dialogue import Dialogue
# from dialogue_action import *
# from dialogue_manager import DialogueLibrary

# import urllib2
# import json


# class DialogueLibraryQuiz(DialogueLibrary):
#     """
#     A DialogueLibrary that can be used when a CommU robot sees an object. This plays 'object hide-and-seek' with the user.
#     """

#     global f, utterance, cancelable, next_action
    
#     f = {}

#     def get_dialogue_for_topic(self, topic):
#         # type: (str) -> Dialogue
#         """
#         Get the dialogue that can be used when CommU sees an object.
#         :param topic:   The label assigned by the ssd network
#         :return:        The Dialogue concerning the object.
#         """
#         #self.request_script()
#         f[5] = self.request_script()
#         for x in range (3,0,-1):            
#             f[0]=str(x)
#             self.funman()
#             if x > 2:
#                 f[4] =  DialogueActionSleep(
#                     sleep_time=1,
#                     cancelable=False,
#                     next_action=DialogueActionTalkNoResponse(f[1].format(self.__get_object_noun(topic)), f[2], f[3]))                                                   
#             else:
#                 f[4] = DialogueActionTalkNoResponse(f[1].format(self.__get_object_noun(topic)), f[2], f[4])
#         return Dialogue(f[4])
        
#     def request_script(self):
#         convo = urllib2.urlopen('http://192.168.1.225:8080/?json={test}')
#         cjson = convo.read()
#         cjdata = json.loads(cjson)
#         return cjdata
        
#     def funman(self):
#         #cjdata = self.request_script()
#         utterance = f[5][f[0]]['1']
#         cancelable = f[5][f[0]]['2']
#         next_action = None
#         #next_action = f[5][f[0]]['3'].replace("zz","None")
#         f[1] = utterance
#         f[2] = cancelable
#         f[3] = next_action

#     def __get_object_noun(self, label):
#         return self.object_proper_name_map.get(label, label)

#     object_proper_name_map = {
#         'aeroplane': 'airplane',
#         'diningtable': 'dining table',
#         'pottedplant': 'potted plant',
#         'tvmonitor': 'screen'
#     }
