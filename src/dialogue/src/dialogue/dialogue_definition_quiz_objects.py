import random
import rospy

from dialogue import Dialogue
from dialogue_action import *
from dialogue_manager import DialogueLibrary
from dialogue_dictionary import convos

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

            convo = urllib2.urlopen('http://192.168.1.225:8080/?json={test}') #add .format(topic) when full implemented
            cjson = convo.read()
            cjdata = json.loads(cjson)
            keyvar = 1
            #rospy.loginfo("topic generation is %s", topic)
            rospy.loginfo("Got Dialogue from server.")

            try:
                for keyvar in cjdata:

                    utterance = cjdata[keyvar]['1'] #cjdata[keyvar]['u']  # u refers to sublist for utterance, change if server syntax changes
                    cancelable = False
                    next_action = None  # c refers to sublist for cancelable, change if server syntax changes

                    keyvar += 1

                    return Dialogue(DialogueActionTalkNoResponse(utterance,cancelable,next_action))

            except TypeError:
                return Dialogue(DialogueActionTalkNoResponse(utterance="end",cancelable=False,next_action=None))


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

    # def dialogue_string_test(self):
    #     i=1
    #     cjdata = self.request_script()
    #     rospy.loginfo("cjdata is %s", cjdata)
    #     #dia = self.generation(cjdata,i)
    #     dia = repr(self.generation(cjdata,i))
    #     rospy.loginfo("repr generation is %s", dia)
    #     return DialogueActionTalkNoResponse(utterance='heya',cancelable=False,next_action=DialogueActionTalkNoResponse(utterance='heyb',cancelable=False,next_action=None))
    #
    #
    # def request_script(self):
    #
    #     return convos['convo' + str(random.randint(1, 6))]
    #
    # def generation(self,cjdata,i):
    #
    #     fulldialogue = ''
    #
    #     dialogueA = "DialogueActionTalkNoResponse("
    #     dialogueU = "utterance='"
    #     dialogueC = "',cancelable="
    #     dialogueN = ",next_action="
    #
    #     try:
    #         i+=1
    #
    #         # utterance  = u
    #         # cancelable = c
    #         # nextaction = n
    #
    #         keyvar = 'line'+ str(i)
    #
    #         fulldialogue += dialogueA
    #         fulldialogue += dialogueU
    #         fulldialogue += cjdata[keyvar]['u'] #u refers to sublist for utterance, change if server syntax changes
    #         fulldialogue += dialogueC
    #         fulldialogue += cjdata[keyvar]['c'] #c refers to sublist for cancelable, change if server syntax changes
    #         fulldialogue += dialogueN
    #         fulldialogue += self.generation(cjdata,i)
    #
    #     except KeyError:
    #         return "None"+ ')'*(i-2)
    #
    #     return fulldialogue
    #
