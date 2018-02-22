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
        cjdatalen = len(cjdata)
        store['full'] = cjdata
        store['block'] = self.assign_return_dia(topic,x=1)
        return Dialogue(store['block'])



    def request_script(self):
        convo = urllib2.urlopen('http://192.168.1.166:9000/?json={test}')
        cjson = convo.read()
        cjdata = json.loads(cjson)
        #cjdata = convos[1]
        return cjdata

    def assign_return_dia(self,topic,x):
        '''
        Assigns the utterances and cancelable parameters of the respective Dialogue functions,
        and reiterates for next action.
        :param x:   The current conversation iteration point/number
        :return:    Dialogue function
        '''

        curint = str(x)

        if store['full'][curint]['type']=='last':
            return DialogueActionTalkNoResponse(store['full'][curint]['u'].format(self.__get_object_noun(topic)),store['full'][curint]['c'],next_action=None)

        if store['full'][curint]['type']=='pass':
            next = int(store['full'][curint]['next'])
            return DialogueActionTalkNoResponse(store['full'][curint]['u'].format(self.__get_object_noun(topic)),store['full'][curint]['c'],next_action=self.assign_return_dia(next))

        if store['full'][curint]['type']=='binary':
            yesloc = int(store['full'][curint]['yesloc'])
            noloc  = int(store['full'][curint]['noloc'])

            return DialogueActionTalkBinaryResponse(store['full'][curint]['u'].format(self.__get_object_noun(topic)),store['full'][curint]['c'],next_action_yes=self.assign_return_dia(yesloc),next_action_no=self.assign_return_dia(noloc))


    def return_none_bby(self):
        return None

    def return_arb_dia(self):
        return DialogueActionTalkNoResponse(utterance='yes',cancelable=False,next_action=self.return_none_bby())

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
