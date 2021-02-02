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


# Would be best to keep messages in domain.yml, because NLU + Stories also want to show them
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_list_projects"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        template = 'utter_show_personal_projects'
        buttons=[]
        projects = tracker.get_slot('projects')

        projectPicked = len(tracker.latest_message['entities']) > 0
        if (projectPicked):
            template = tracker.latest_message['entities'][0]['value']
            buttons=projects
            for i in range(len(projects)):
                if projects[i]['payload'].index(template) > 0:
                    del projects[i]
                    break
            print('template', template)
            print('buttons', buttons)
            print('projects', projects)
            dispatcher.utter_message(template=template, buttons=buttons)
            return [SlotSet("projects", projects)]

        print('template', template)
        print('buttons', buttons)
        print('projects', projects)
        dispatcher.utter_message(template=template)

        return []
