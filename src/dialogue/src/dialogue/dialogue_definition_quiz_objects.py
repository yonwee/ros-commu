from dialogue import Dialogue
from dialogue_action import *
from dialogue_manager import DialogueLibrary

from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, unquote, quote
import json
import urllib.request


class DialogueLibraryTalk(DialogueLibrary):
    """
    A DialogueLibrary that can be used when a CommU robot sees an object.
    """

    def get_dialogue_for_topic(self, topic):
        # type: (str) -> Dialogue
        """
        Get the dialogue that can be used when CommU sees an object.
        :param topic:   The label assigned by the ssd network
        :return:        The pre-scripted Dialogue concerning the object.
        """
        return Dialogue(DialogueLibraryTalk.dialogue_map[topic])



    def xinhai(self):
        #topic = "dog"  # change to robot object recogn input accordingly
        linkget = urllib.request.urlopen("http://192.168.1.225:8080/?json={gen" + topic + "}")
        mybytes = linkget.read()
        mystr = json.loads(mybytes)
        linkget.close()
        exec(mystr)

    dialogue_map = {
        'dog':
            xinhai(),
    }

