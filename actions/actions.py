# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class ActionShowProject(Action):

    def name(self) -> Text:
        return "action_show_project"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        projects = tracker.get_slot('projects')
        project = tracker.latest_message['entities'][0]['value']

        for i in range(len(projects)):
            if project in projects[i]['payload']:
                del projects[i]
                break
        dispatcher.utter_message(template=project, buttons=projects)
        return [SlotSet("projects", projects)]


        # If 0 projects, reset it but show different template domain['slots']['projects']['initial_value']
