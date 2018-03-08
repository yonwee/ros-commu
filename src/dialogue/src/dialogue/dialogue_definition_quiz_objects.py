import random
import rospy

from dialogue import Dialogue
from dialogue_action import *
from dialogue_manager import DialogueLibrary

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

        # cjdata = self.request_script()
        # cjdatalen = len(cjdata)
        # store['full'] = cjdata
        # store['block'] = self.assign_return_dia(topic,x=1)
        # return Dialogue(store['block'])

        # return Dialogue(DialogueActionTalkNoResponse(
        #     'arm down', False, next_action=DialogueActionMove(
        #     'acchi_arm_down', False, next_action=DialogueActionSleep(
        #     sleep_time=1, cancelable=False, next_action=DialogueActionTalkNoResponse(
        #             'arm left', False, next_action=DialogueActionMove(
        #             'acchi_arm_left', False, next_action=DialogueActionSleep(
        #             sleep_time=1, cancelable=False, next_action=DialogueActionTalkNoResponse(
        #                     'arm right', False, next_action=DialogueActionMove(
        #                     'acchi_arm_right', False, next_action=DialogueActionSleep(
        #                     sleep_time=1, cancelable=False, next_action=DialogueActionTalkNoResponse(
        #                             'arm up', False, next_action=DialogueActionMove(
        #                             'acchi_arm_up', False, next_action=DialogueActionSleep(
        #                             sleep_time=1, cancelable=False, next_action=DialogueActionTalkNoResponse(
        #                                     'atama kaki', False, next_action=DialogueActionMove(
        #                                     'atama_kaki', False, next_action=DialogueActionSleep(
        #                                     sleep_time=1, cancelable=False, next_action=DialogueActionTalkNoResponse(
        #                                             'atama tonton', False, next_action=DialogueActionMove(
        #                                             'atama_tonton', False, next_action=DialogueActionSleep(
        #                                             sleep_time=1, cancelable=False, next_action=DialogueActionTalkNoResponse(
        #                                                     'choki', False, next_action=DialogueActionMove(
        #                                                     'choki', False, next_action=DialogueActionSleep(
        #                                                     sleep_time=1, cancelable=False, next_action=DialogueActionTalkNoResponse(
        #                                                             'eyeblink', False, next_action=DialogueActionMove(
        #                                                             'eyeblink', False, next_action=DialogueActionSleep(
        #                                                             sleep_time=1, cancelable=False, next_action=DialogueActionTalkNoResponse(
        #                                                                     'gu', False, next_action=DialogueActionMove(
        #                                                                     'gu', False, next_action=DialogueActionSleep(
        #                                                                     sleep_time=1, cancelable=False, next_action=None))))))))))))))))))))))))))))
#
#         return Dialogue(DialogueActionTalkNoResponse(
#             'banzai2', False, next_action=DialogueActionMovePlus(
#             'banzai2', """0.0     P       0.0     100     2       -80     3       0       -1
# 0.0     P       0.0     100     4       15      5       0       -1
#
# 1.5     P       0.0     150     4       15      5       -30     -1
# 0.0     P       0.0     50      10      15      11      15      -1
# 2.0     P       0.0     40      10      0       11      0       -1
# 0.3     P       0.0     40      0       0       1       0       -1
# 0.0     P       0.0     80      4       -80     2       -80     -1
# 0.0     P       0.0     40      5       0       3       0       -1
# 0.0     P       0.0     40      6       0       7       0       -1
# 0.0     P       0.0     40      8       0       9       0       -1
# 0.0     P       0.0     40      10      0       11      0       -1
# 0.0     P       0.0     40      12      0       -1
# 1.0     t""",
#              False, next_action=DialogueActionMove(
#                                 'banzai2', False, next_action=DialogueActionSleep(
#                                     sleep_time=1, cancelable=False, next_action=None)))))

        # return Dialogue(DialogueActionTalkNoResponse(
        #     'yay', False, next_action=DialogueActionMove(
        #         'yay', False, next_action=DialogueActionSleep(
        #             sleep_time=3, cancelable=False, next_action=DialogueActionTalkNoResponse(
        #                 'reset', False, next_action=DialogueActionMove(
        #                     'reset', False, next_action=DialogueActionSleep(
        #                         sleep_time=2, cancelable=False, next_action=DialogueActionTalkNoResponse(
        #     'original hi', False, next_action=DialogueActionMove(
        #         'hi', False, next_action=DialogueActionSleep(
        #             sleep_time=3, cancelable=False, next_action=DialogueActionTalkNoResponse(
        #                 'reset', False, next_action=DialogueActionMove(
        #                     'reset', False, next_action=DialogueActionSleep(
        #                         sleep_time=2, cancelable=False, next_action=DialogueActionTalkNoResponse(
        #     'hi2', False, next_action=DialogueActionMove(
        #         'hi2', False, next_action=DialogueActionSleep(
        #             sleep_time=3, cancelable=False, next_action=DialogueActionTalkNoResponse(
        #                 'reset', False, next_action=DialogueActionMove(
        #                     'reset', False, next_action=DialogueActionSleep(
        #                         sleep_time=2, cancelable=False, next_action=DialogueActionTalkNoResponse(
        #     'sugoi', False, next_action=DialogueActionMove(
        #         'sugoi', False, next_action=DialogueActionSleep(
        #             sleep_time=3, cancelable=False, next_action=DialogueActionTalkNoResponse(
        #                 'reset', False, next_action=DialogueActionMove(
        #                     'reset', False, next_action=DialogueActionSleep(
        #                         sleep_time=2, cancelable=False, next_action=DialogueActionTalkNoResponse(
        #     'point_left', False, next_action=DialogueActionMove(
        #         'point_left', False, next_action=DialogueActionSleep(
        #             sleep_time=3, cancelable=False, next_action=DialogueActionTalkNoResponse(
        #                 'reset', False, next_action=DialogueActionMove(
        #                     'reset', False, next_action=DialogueActionSleep(
        #                         sleep_time=2, cancelable=False, next_action=None)))))))))))))))))))))))))))))))
        # return Dialogue(DialogueActionTalkNoResponse(
        #     'point_left', False, next_action=DialogueActionMove(
        #         'point_left', False, next_action=DialogueActionSleep(
        #             sleep_time=3, cancelable=False, next_action=DialogueActionTalkNoResponse(
        #                 'reset', False, next_action=DialogueActionMove(
        #                     'reset', False, next_action=DialogueActionSleep(
        #                         sleep_time=2, cancelable=False, next_action=None)))))))

        return Dialogue(DialogueActionTalkNoResponse(
            'hi2', False, next_action=DialogueActionMove(
                'hi2', False, next_action=None)))


    def request_script(self):
        convo = urllib2.urlopen('http://192.168.1.166:9000/?json={test}')
        cjson = convo.read()
        cjdata = json.loads(cjson)
        rospy.loginfo("Received data from conversation server.")
        return cjdata

    # def assign_return_dia(self,topic,x):
    #     '''
    #     Assigns the utterances and cancelable parameters of the respective Dialogue functions,
    #     and reiterates for next action.
    #     :param x:   The current conversation iteration point/number
    #     :return:    Dialogue function
    #     '''
    #     topicstr = str(topic)
    #     curint = str(x)
    #
    #     if store['full'][curint]['type']=='last':
    #         #store['full'][curint]['u'] =store['full'][curint]['u'].format(topic=(self.__get_object_noun(topic)), atopic =self.__add_a_to_noun(self.__get_object_noun(topic)))
    #         #for future grammar processing of the topic - anoun to add 'a' or 'an' into the topic string
    #         #consider using inflect library as well
    #         store['full'][curint]['u'] = store['full'][curint]['u'].format(topicstr)
    #         # return DialogueActionTalkNoResponse(store['full'][curint]['u'],
    #         #                                     store['full'][curint]['c'],
    #         #                                     next_action=None)
    #         return DialogueActionMove("banzai",
    #                                             store['full'][curint]['c'],
    #                                             next_action=None)
    #
    #     if store['full'][curint]['type']=='pass':
    #         next = int(store['full'][curint]['next'])
    #         store['full'][curint]['u'] = store['full'][curint]['u'].format(topicstr)
    #         return DialogueActionMove("banzai",
    #                                             store['full'][curint]['c'],
    #                                             next_action=self.assign_return_dia(topicstr,next))
    #
    #     if store['full'][curint]['type']=='binary':
    #         yesloc = int(store['full'][curint]['yesloc'])
    #         noloc  = int(store['full'][curint]['noloc'])
    #         store['full'][curint]['u'] = store['full'][curint]['u'].format(topicstr)
    #         return DialogueActionTalkBinaryResponse(store['full'][curint]['u'],
    #                                                 store['full'][curint]['c'],
    #                                                 next_action_yes=self.assign_return_dia(topicstr,yesloc),
    #                                                 next_action_no=self.assign_return_dia(topicstr,noloc))
    #
    #     if store['full'][curint]['type'] == 'ternary':
    #         yesloc = int(store['full'][curint]['yesloc'])
    #         noloc = int(store['full'][curint]['noloc'])
    #         neuloc = int(store['full'][curint]['neuloc'])
    #         store['full'][curint]['u'] = store['full'][curint]['u'].format(topicstr)
    #         return DialogueActionTalkTernaryResponse(store['full'][curint]['u'],
    #                                                 store['full'][curint]['c'],
    #                                                 next_action_yes=self.assign_return_dia(topicstr, yesloc),
    #                                                 next_action_no=self.assign_return_dia(topicstr, noloc),
    #                                                 next_action_neutral=self.assign_return_dia(topicstr,neuloc))
        # #unimplemented look command
        # if store['full'][curint]['type'] == 'look':
        #     next = int(store['full'][curint]['next'])
        #     lookat = int(store['full'][curint]['looktarget'])
        #     #lookat should be DialogueActionLook.LOOK_TYPE_WATCH_CONVERSATION_PARTNER or similar
        #     store['full'][curint]['u'] = store['full'][curint]['u'].format(topicstr)
        #     return DialogueActionLook(lookat,
        #                               store['full'][curint]['c'],
        #                               next_action=self.assign_return_dia(topicstr, next))





    def return_arb_dia(self):
        return DialogueActionTalkNoResponse(utterance='yes',cancelable=False,next_action=None)

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
