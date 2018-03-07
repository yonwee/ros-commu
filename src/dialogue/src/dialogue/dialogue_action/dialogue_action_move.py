
import rospy
from typing import Union
from commu_wrapper.srv import CommUMove

from abstract_dialogue_action import AbstractDialogueAction


class DialogueActionMove(AbstractDialogueAction):
    """
    DialogueActionMove tells the robot to move according to the gesturefile provided.
    """

    def __init__(self, gesturefile, cancelable, next_action):
        # type: (str, bool, Union[AbstractDialogueAction, None]) -> None
        """
        Initializes the DialogueLookAction
        :param gesturefile: The gesture filename present on the robot
        :param cancelable: Whether the dialogue can be cancelled after this action.
        :param next_action: The next action in this dialogue.
        """
        self.gesturefile = gesturefile
        self.cancelable = cancelable
        self.next_action = next_action

    def run(self, tf):
        # type: (str) -> AbstractDialogueAction
        """
        Use this function to perform an action and return the next action. Return None when there is no next action.
        :param tf: The name of the tf2_ros transform of the object that is currently being talked about.
        :return: The next action in the Dialogue. Return None when there is no next action.
        """

        self.move(self.gesturefile)

        return self.next_action

    def can_cancel(self):
        # type () -> bool
        """
        Whether the Dialogue can logically be cancelled after this DialogueAction.
        :return: Is this a good place in the Dialogue to stop if the Dialogue has to be cancelled?
        """
        return self.cancelable

    @staticmethod
    def move(gesture_name):
        # type: (str) -> bool
        """
        This function calls the move service, to execute a gesture.
        :param gesture_name: The name of the gesturefile to move to.
        :return: Whether the request succeeded.
        """
        service_name = '/commu_wrapper/move'

        rospy.wait_for_service(service_name)

        try:
            rospy.loginfo("Moving according to {}.".format(gesture_name))

            move_gesture = rospy.ServiceProxy(service_name, CommUMove)

            return move_gesture(gesture_name)
        except rospy.ServiceException, e:
            print "Service call failed: %s" % e
            raise