import multiprocessing
import time

import rospy
from keyboard.msg import Key
from typing import Union

from abstract_dialogue_action import AbstractDialogueAction
from abstract_dialogue_action_talk import AbstractDialogueActionTalk

#
# class Timeout(Exception):
#     pass
#
#
# def handler(sig, frame):
#     raise Timeout
#
# signal.signal(signal.SIGALRM, handler)  # register interest in SIGALRM events
#
# signal.alarm(2)  # timeout in 2 seconds
# try:
#     time.sleep(60)
# except Timeout:
#     print('took too long')


class DialogueActionTalkTernaryResponse(AbstractDialogueActionTalk):
    """
    DialogueActionTalkTernaryResponse makes the Sota utter a sentence and allows the user to respond by pressing either
    the 'y' or 'n' keys on their keyboard, or offer a neutral response by timing out.
    """

    def __init__(self, utterance, cancelable, next_action_yes, next_action_no, next_action_neutral):
        # type: (str, bool, Union[AbstractDialogueAction, None], Union[AbstractDialogueAction, None], Union[AbstractDialogueAction, None]) -> None
        self.utterance = utterance
        self.cancelable = cancelable
        self.next_action_yes = next_action_yes
        self.next_action_no = next_action_no
        self.next_action_neutral = next_action_neutral

    def run(self, tf):
        # type: (str) -> AbstractDialogueAction
        """
        Use this function to perform an action and return the next action. Return None when there is no next action.
        :param tf: The name of the tf2_ros transform of the object that is currently being talked about.
        :return: The next action in the Dialogue. Return None when there is no next action.
        """
        AbstractDialogueActionTalk.utter(self.utterance, blocking=False)

        rospy.loginfo("Waiting for either 'y' or 'n' to be pressed on the keyboard, else timeout will occur")

        # Start wait_for_kb as a process
        p = multiprocessing.Process(target=self.wait_for_kb())
        p.start()

        # Wait for 10 seconds or until process finishes
        p.join(10)

        # If thread is still active
        if p.is_alive():
            p.join()
            return self.next_action_neutral


    def wait_for_kb(self):
        key = rospy.wait_for_message('/keyboard/keydown', Key) # type: Key

        rospy.loginfo("Key {} pressed.".format(key.code))

        if key.code == Key.KEY_y:
            return self.next_action_yes
        if key.code == Key.KEY_n:
            return self.next_action_no

    def can_cancel(self):
        # type () -> bool
        """
        Whether the Dialogue can logically be cancelled after this DialogueAction.
        :return: Is this a good place in the Dialogue to stop if the Dialogue has to be cancelled?
        """
        return self.cancelable


