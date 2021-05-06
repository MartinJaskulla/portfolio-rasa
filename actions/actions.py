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

# Now I need to actions, one to list remaining one if other we want to relist them? and one to pick and delete. Because now I do not want to relist both
# Or 3 actions. One is to reset. NLU "Show me all projects again"
class ActionChooseSuggestion(Action):

    def name(self) -> Text:
        return "action_choose_suggestion"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        suggestions = tracker.get_slot('suggestions')
        suggestion = tracker.latest_message['entities'][0]['value']
        print('suggestion', suggestion)
        print('before deletion', suggestions)
        for i in range(len(suggestions)):
            if suggestion in suggestions[i]['payload']:
                print('deleting', suggestions[i])
                del suggestions[i]
                break
        print('after deletion', suggestions)
        dispatcher.utter_message(template=suggestion)
        if(len(suggestions) == 0):
            print('none')
            return [SlotSet("suggestions", None)]
        return [SlotSet("suggestions", suggestions)]

class ActionRemainingSuggestions(Action):

    def name(self) -> Text:
        return "action_remaining_suggestions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # maybe I need to add second list slot with seen ones and filter them?
        suggestions = tracker.get_slot('suggestions')
        print('listing suggestions', suggestions)
        dispatcher.utter_message(buttons=suggestions)
        return []