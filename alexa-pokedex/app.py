from pokedex_logic import pokedex


def pokemon_intent(event, context):
    pokemon_species = pokedex.get_species()
    pokemon_data = pokedex.get_pokemon_data(pokemon_species)
    pokemon = pokedex.generate_alexa_text_string(pokemon_species, pokemon_data)
    speech_text = "Your pokemon today is {}. Goodbye!!".format(pokemon)
    print(speech_text)
    return statement("pokemon_intent", speech_text)

def cancel_intent():
    return statement("CancelIntent", "You want to cancel")


def help_intent():
    return statement("CancelIntent", "You want help")


def stop_intent():
    return statement("StopIntent", "You want to stop")


def intent_router(event, context):
    intent = event['request']['intent']['name']
    # Custom Intents
    if intent == "pokemon_intent":
        return pokemon_intent(event, context)
    # Required Intents
    if intent == "AMAZON.CancelIntent":
        return cancel_intent()
    if intent == "AMAZON.HelpIntent":
        return help_intent()
    if intent == "AMAZON.StopIntent":
        return stop_intent()

def build_response(message, session_attributes={}):
    response = {}
    response['version'] = '1.0'
    response['sessionAttributes'] = session_attributes
    response['response'] = message
    return response


def build_SimpleCard(title, body):
    card = {}
    card['type'] = 'Simple'
    card['title'] = title
    card['content'] = body
    return card


def build_PlainSpeech(body):
    speech = {}
    speech['type'] = 'PlainText'
    speech['text'] = body
    return speech


def statement(title, body):
    speechlet = {}
    speechlet['outputSpeech'] = build_PlainSpeech(body)
    speechlet['card'] = build_SimpleCard(title, body)
    speechlet['shouldEndSession'] = True
    return build_response(speechlet)


def on_launch(event, context):
    return statement("Alexa Pokedex", "The alexa pokedex")


def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event, context)
    elif event['request']['type'] == "IntentRequest":
        return intent_router(event, context)