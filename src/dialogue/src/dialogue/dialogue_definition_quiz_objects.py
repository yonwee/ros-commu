
import random

from dialogue import Dialogue
from dialogue_action import *
from dialogue_manager import DialogueLibrary

import json
import urllib2

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
        linkget = urllib2.urlopen("http://192.168.1.171:8080/?json={gen" + topic + "}")
        mybytes = linkget.read()
        mydic = json.loads(mybytes)
        linkget.close()
        global utterance_list
        utterance_list = {}
        utterance_list[0] = mydic["U1"]
        utterance_list[1] = mydic["U2"]
        utterance_list[2] = mydic["U3"]
        utterance_list[3] = mydic["U4"]
        utterance_list[4] = mydic["U5"]

        if utterance_list[3] == None:
            return Dialogue(
                DialogueActionLook(
                    look_type=DialogueActionLook.LOOK_TYPE_WATCH_CONVERSATION_PARTNER,
                    cancelable=False,
                    next_action=
                    DialogueActionSleep(
                        sleep_time=1,
                        cancelable=False,
                        next_action=
                        DialogueActionTalkNoResponse(
                            utterance="{}".format(utterance_list[0]),
                            cancelable=False,
                            next_action=
                            DialogueActionSleep(
                                sleep_time=1,
                                cancelable=False,
                                next_action=
                                DialogueActionTalkNoResponse(
                                    utterance="{}".format(utterance_list[1]),
                                    cancelable=False,
                                    next_action=
                                    DialogueActionSleep(
                                        sleep_time=1,
                                        cancelable=False,
                                        next_action=
                                        DialogueActionTalkNoResponse(
                                            utterance="{}".format(utterance_list[2]),
                                            cancelable=False,
                                            next_action=None
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )

        if utterance_list[3] != None:
            return Dialogue(
                DialogueActionLook(
                    look_type=DialogueActionLook.LOOK_TYPE_WATCH_CONVERSATION_PARTNER,
                    cancelable=False,
                    next_action=
                    DialogueActionSleep(
                        sleep_time=1,
                        cancelable=False,
                        next_action=
                        DialogueActionTalkBinaryResponse(
                            utterance="{}".format(utterance_list[0]),
                            cancelable=False,
                            next_action_yes=
                            DialogueActionTalkNoResponse(
                                utterance="{}".format(utterance_list[1]),
                                cancelable=False,
                                next_action=
                                DialogueActionSleep(
                                    sleep_time=1,
                                    cancelable=False,
                                    next_action=
                                    DialogueActionTalkNoResponse(
                                        utterance="{}".format(utterance_list[2]),
                                        cancelable=False,
                                        next_action=None
                                    )
                                )
                            ),
                            next_action_no=
                            DialogueActionTalkNoResponse(
                                utterance="{}".format(utterance_list[3]),
                                cancelable=False,
                                next_action=
                                DialogueActionSleep(
                                    sleep_time=1,
                                    cancelable=False,
                                    next_action=
                                    DialogueActionTalkNoResponse(
                                        utterance="{}".format(utterance_list[4]),
                                        cancelable=False,
                                        next_action=None
                                    )
                                )
                            ),
                        )
                    )
                )
            )

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
