import logging
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response
from pokedex_logic import pokedex

sb = SkillBuilder()


@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):
    speech_text = "Welcome to the Alexa Pokedex!"
    return handler_input.response_builder.speak(speech_text).set_card(SimpleCard("Hello World", speech_text)).set_should_end_session(False).response


@sb.request_handler(can_handle_func=is_intent_name("pokemon_intent"))
def pokemon_intent_handler(handler_input):
    pokemon_species = pokedex.get_species()
    pokemon_data = pokedex.get_pokemon_data(pokemon_species)
    pokemon = pokedex.generate_alexa_text_string(pokemon_species, pokemon_data)
    speech_text = "{}".format(pokemon)
    return handler_input.response_builder.speak(speech_text).set_card( SimpleCard("Pokedex", speech_text)).set_should_end_session(True).response


@sb.request_handler(can_handle_func=is_intent_name("AMAZON.HelpIntent"))
def help_intent_handler(handler_input):
    speech_text = "You can ask me for a pokemon!"
    return handler_input.response_builder.speak(speech_text).ask(speech_text).set_card(SimpleCard("Hello World", speech_text)).response


@sb.request_handler(can_handle_func=lambda handler_input: is_intent_name("AMAZON.CancelIntent")(handler_input) or is_intent_name("AMAZON.StopIntent")(handler_input))
def cancel_and_stop_intent_handler(handler_input):
    speech_text = "Goodbye!"
    return handler_input.response_builder.speak(speech_text).set_card(SimpleCard("Hello World", speech_text)).response


@sb.request_handler(can_handle_func=is_request_type("SessionEndedRequest"))
def session_ended_request_handler(handler_input):
    return handler_input.response_builder.response


@sb.exception_handler(can_handle_func=lambda i, e: True)
def all_exception_handler(handler_input, exception):
    speech = "Sorry, there was some problem. Please try again!!"
    handler_input.response_builder.speak(speech).ask(speech)
    return handler_input.response_builder.response

def lambda_handler(*args, **kwargs):
    skill_handler = sb.lambda_handler()
    return skill_handler(*args, **kwargs)

