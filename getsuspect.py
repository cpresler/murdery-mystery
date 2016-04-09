# Program for the GetSuspect intent
@alexa.intent_handler('GetSuspect')
def get_suspect_intent_handler(request):
    """
    Whodunnit??
    """

    # Get variables like userId, slots, intent name etc from the 'Request' object
    suspect = request.slots["Suspect"] 

    if ingredient == None:
        return alexa.create_response("Could not find an ingredient!")

    card = alexa.create_card(title="GetRecipeIntent activated", subtitle=None,
                             content="asked alexa to find a recipe using {}".format(ingredient))
    
    return alexa.create_response("Finding a recipe with the ingredient {}".format(ingredient),
                                 end_session=False, card_obj=card)
