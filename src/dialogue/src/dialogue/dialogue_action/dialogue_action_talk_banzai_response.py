import rospy
from typing import Union
from commu_wrapper.srv import CommUMoveExec

from abstract_dialogue_action import AbstractDialogueAction


class DialogueActionTalkBanzaiResponse(AbstractDialogueAction):
    """
    DialogueActionTalkBanzaiResponse makes the Sota utter a sentence with a banzai gesture, without allowing the user to respond.
    """

    def __init__(self, gesturefile, cancelable, next_action):
        # type: (str, bool, Union[AbstractDialogueAction, None]) -> None
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

        self.move_exec(self.gesturefile)

        return self.next_action

    def can_cancel(self):
        # type () -> bool
        """
        Whether the Dialogue can logically be cancelled after this DialogueAction.
        :return: Is this a good place in the Dialogue to stop if the Dialogue has to be cancelled?
        """
        return self.cancelable

    @staticmethod
    def move_exec(move_exec_gesturefile):
        # type: (str) -> bool
        """
        Call the CommUUtter service to make the CommU/Sota execute the specified gesture.
        :param move_exec_gesturefile: The specified gesture to execute.
        :return: Whether the robot executed the gesture successfully.
        """
        service_name = '/commu_wrapper/move_exec'

        rospy.wait_for_service(service_name)

        try:
            move_exec_srv = rospy.ServiceProxy(service_name, CommUMoveExec)

            rospy.loginfo("Executing: " + str(move_exec_gesturefile))

            return move_exec_srv(move_exec_gesturefile)

        except rospy.ServiceException, e:
            print("Service call failed: %s" % e)
            raise

