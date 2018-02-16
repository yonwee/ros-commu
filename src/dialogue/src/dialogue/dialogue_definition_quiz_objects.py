import random

from dialogue import Dialogue
from dialogue_action import *
from dialogue_manager import DialogueLibrary
from dialogue_dictionary import *

import urllib2
import json

class DialogueLibraryQuiz(DialogueLibrary):
    """
    A DialogueLibrary that can be used when a CommU robot sees an object. This plays 'object hide-and-seek' with the user.
    """

    def get_dialogue_for_topic(self, topic):
        # type: (str) -> Dialogue
        """
        Get the dialogue that can be used when CommU sees an object.
        :param topic:   The label assigned by the ssd network
        :return:        The Dialogue concerning the object.
        """
        #return Dialogue(DialogueLibraryQuiz.select_convo(self,topic))
        return Dialogue(DialogueLibraryQuiz.dialogue_string_test(self))

        # return Dialogue(
        #     DialogueActionLook(
        #         look_type=DialogueActionLook.LOOK_TYPE_WATCH_CONVERSATION_PARTNER,
        #         cancelable=False,
        #         next_action=
        #         DialogueActionSleep(
        #             sleep_time=1,
        #             cancelable=False,
        #             next_action=
        #             DialogueActionTalkBinaryResponse(
        #                 utterance="Do you also see {}?".format(self.__add_a_to_noun(self.__get_object_noun(topic))),
        #                 cancelable=False,
        #                 next_action_yes=
        #                 DialogueActionTalkNoResponse(
        #                     utterance=random.choice(self.positive_response_list),
        #                     cancelable=False,
        #                     next_action=
        #                     DialogueActionLook(
        #                         look_type=DialogueActionLook.LOOK_TYPE_WATCH_ENVIRONMENT,
        #                         cancelable=True,
        #                         next_action=None
        #                     )
        #                 ),
        #                 next_action_no=
        #                 DialogueActionLook(
        #                     look_type=DialogueActionLook.LOOK_TYPE_WATCH_CONVERSATION_TOPIC,
        #                     cancelable=False,
        #                     next_action=
        #                     DialogueActionTalkNoResponse(
        #                         utterance=random.choice(self.negative_response_list),
        #                         cancelable=False,
        #                         next_action=
        #                         DialogueActionSleep(
        #                             sleep_time=2,
        #                             cancelable=False,
        #                             next_action=DialogueActionLook(
        #                                 look_type=DialogueActionLook.LOOK_TYPE_WATCH_ENVIRONMENT,
        #                                 cancelable=True,
        #                                 next_action=None
        #                             )
        #                         )
        #                     ),
        #                 )
        #             )
        #         )
        #     )
        # )


    def __add_a_to_noun(self, noun):
        # type: (str) -> str

        if noun[0].lower() in ['a', 'e', 'i', 'o', 'u']:
            return 'an ' + noun
        else:
            return 'a ' + noun

    def __get_object_noun(self, label):
        return self.object_proper_name_map.get(label, label)

    object_proper_name_map = {
        'aeroplane': 'airplane',
        'diningtable': 'dining table',
        'pottedplant': 'potted plant',
        'tvmonitor': 'screen'
    }

    positive_response_list = [
        "Cool, you're good!",
        "Nice, me too!",
        "I see it too!"
    ]

    negative_response_list = [
        "I see it over there",
        "It's over there",
        "I can help you. It's over here"
    ]

    def dialogue_string_test(self):
        i=1
        cjdata = self.request_script()
        dia = str(self.generation(cjdata,i))

        return eval(dia)


    def request_script(self):

            ##################RIP_requesting_from_server#########################
            # convo = urllib2.urlopen('http://192.168.1.225:8080/?json={tedt}')##
            # cjson = convo.read()                                              #
            # cjdata = json.loads(cjson)                                       ##
            #####################################################################
            cjdata = convos['convo' + str(random.randint(1, 6))]
            return cjdata

    def generation(self,cjdata,i):

        fulldialogue = ''

        dialogueA = "DialogueActionTalkNoResponse("
        dialogueU = "utterance='"
        dialogueC = "',cancelable='"
        dialogueN = "',next_action="

        try:
            i+=1

            # utterance  = u
            # cancelable = c
            # nextaction = n

            keyvar = 'line'+ str(i)

            fulldialogue += dialogueA
            fulldialogue += dialogueU
            fulldialogue += cjdata[keyvar]['1']
            fulldialogue += dialogueC
            fulldialogue += cjdata[keyvar]['2']
            fulldialogue += dialogueN
            fulldialogue += self.generation(cjdata,i)

        except KeyError:
            return "None"+ ')'*(i-2)

        return fulldialogue
