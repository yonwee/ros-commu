# import rospy
# from commu_wrapper.srv import CommUMoveExec
#
# from abstract_dialogue_action import AbstractDialogueAction
#
#
# class AbstractDialogueActionGesture(AbstractDialogueAction):
#     """
#     AbstractDialogueActionTalk defines an abstract super-class for a DialogueAction which
#      makes the robot utter and allows for optional user input.
#     """
#
#     def run(self, tf):
#         # type: (str) -> AbstractDialogueAction
#         """
#         Use this function to perform an action and return the next action. Return None when there is no next action.
#         :param tf: The name of the tf2_ros transform of the object that is currently being talked about.
#         :return: The next action in the Dialogue. Return None when there is no next action.
#         """
#         raise NotImplementedError
#
#     def can_cancel(self):
#         # type () -> bool
#         """
#         Whether the Dialogue can logically be cancelled after this DialogueAction.
#         :return: Is this a good place in the Dialogue to stop if the Dialogue has to be cancelled?
#         """
#         raise NotImplementedError
#
#     @staticmethod
#     def move_exec(move_exec_gesturefile):
#         # type: (bool) -> bool
#         """
#         Call the CommUUtter service to make the CommU/Sota execute the specified gesture.
#         :param move_exec_gesturefile: The specified gesture to execute.
#         :return: Whether the robot executed the gesture successfully.
#         """
#         service_name = '/commu_wrapper/move_exec'
#
#         rospy.wait_for_service(service_name)
#
#         try:
#             move_exec_srv = rospy.ServiceProxy(service_name, CommUMoveExec)
#
#             rospy.loginfo("Executing: " + str(move_exec_gesturefile))
#
#             if move_exec_gesturefile is not None:
#                 success = move_exec_srv(move_exec_gesturefile)
#
#                 rospy.loginfo("Gesture " + ("succeeded" if success else "failed!"))
#
#                 return success
#             return True
#
#         except rospy.ServiceException, e:
#             print("Service call failed: %s" % e)
#             raise
