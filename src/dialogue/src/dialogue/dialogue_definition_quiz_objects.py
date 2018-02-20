import random

from dialogue import Dialogue
from dialogue_action import *
from dialogue_manager import DialogueLibrary


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
                        utterance="Hey",
                        cancelable=False,
                        next_action=
                        DialogueActionSleep(
                            Sleep_time=3,
                            cancelable=False,
                            next_action=
                            DialogueActionTalkNoResponse(
                                utterance="Do you",
                                cancelable=False,
                                next_action=
                                DialogueActionSleep(
                                    Sleep_time=3,
                                    cancelable=False,
                                    next_action=
                                    DialogueActionTalkNoResponse(
                                        utterance="Hello",
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
