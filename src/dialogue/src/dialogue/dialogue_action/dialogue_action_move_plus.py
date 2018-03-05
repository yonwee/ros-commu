
import rospy
from typing import Union
from commu_wrapper.srv import CommUMovePlus

from abstract_dialogue_action import AbstractDialogueAction


class DialogueActionMovePlus(AbstractDialogueAction):
    """
    DialogueActionMove tells the robot to add the gesturefile provided.
    """

    def __init__(self, new_name, definition, cancelable, next_action):
        # type: (str, str, bool, Union[AbstractDialogueAction, None]) -> None
        """
        Initializes the DialogueLookAction
        :param new_name: The new gesture filename to be created.
        :param definition: The contents of the new gesture file to be created.
        :param cancelable: Whether the dialogue can be cancelled after this action.
        :param next_action: The next action in this dialogue.
        """
        self.new_name = new_name
        self.definition = definition
        self.cancelable = cancelable
        self.next_action = next_action

    def run(self, tf):
        # type: (str) -> AbstractDialogueAction
        """
        Use this function to perform an action and return the next action. Return None when there is no next action.
        :param tf: The name of the tf2_ros transform of the object that is currently being talked about.
        :return: The next action in the Dialogue. Return None when there is no next action.
        """

        self.moveplus(self.new_name, self.definition)

        return self.next_action

    def can_cancel(self):
        # type () -> bool
        """
        Whether the Dialogue can logically be cancelled after this DialogueAction.
        :return: Is this a good place in the Dialogue to stop if the Dialogue has to be cancelled?
        """
        return self.cancelable

    @staticmethod
    def moveplus(gesture_name, gesture_def):
        # type: (str, str) -> bool
        """
        This function calls the move service, to execute a gesture.
        :param gesture_name: The new gesture filename to be created.
        :param gesture_def: The contents of the new gesture file to be created.
        :return: Whether the request succeeded.
        """
        service_name = '/commu_wrapper/move_plus'

        rospy.wait_for_service(service_name)

        try:
            rospy.loginfo("Moving according to {}.".format(gesture_name))

            move_plus_gesture = rospy.ServiceProxy(service_name, CommUMovePlus)

            return move_plus_gesture(gesture_name, gesture_def)
        except rospy.ServiceException, e:
            print "Service call failed: %s" % e
            raise