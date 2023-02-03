# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet

from rasa_sdk import Action, Tracker,  FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from api import quote_api

dict1 = {"john12@gmail.com": "john12",
        "jenny25@gmail.com": "jenny25"}
class ValidateDetailsForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_details_form"
    

    def validate_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        email = tracker.get_slot("email")
        if email not in dict1.keys():
            dispatcher.utter_message(text="Invalid email please enter correct email")
            return{"email": None}
        return{"email": email}

    def validate_password(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
        password = tracker.get_slot("password")
        email = tracker.get_slot("email")
        
        print(password != dict1[email]) 
        if password != dict1[email]:
            dispatcher.utter_message(text="Invalid password please enter correct password")
            return{"password": None}
        return{"password": password}

class ActionQuotes(Action):

    def name(self) -> Text:
        return "action_quotes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        result = quote_api()
        dispatcher.utter_message(text= f"Thank you, here is the quote '{result}'")
  
        return []

# class ActionEmail(Action):
#     def name(self) -> Text:
#         return "action_email"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dict1 = {'john12@gmail.com': 'abcdef', 
#                 'jenny45@gmail.com': 'efghjk',
#                 'cris23@gmail.com': 'hijklm'}
#         if email not in dict1.keys():
#             # print(email)
#             dispatcher.utter_message(text="email you entered is not correct")
#         return[]