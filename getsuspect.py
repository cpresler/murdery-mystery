# Program for the GetSuspect intent
@alexa.intent_handler('GetSuspect')
def get_suspect_intent_handler(request):
    """
    Whodunnit??
    """

    # Get variables like userId, slots, intent name etc from the 'Request' object
    # suspect = request.slots["Suspect"] 

    # if suspect == None:
    #     return alexa.create_response("Could not find a suspect!")

    # card = alexa.create_card(title="GetRecipeIntent activated", subtitle=None,
    #                          content="asked alexa to find a recipe using {}".format(suspect))
    
    # return alexa.create_response("Finding a recipe with the suspect {}".format(suspect),
    #                              end_session=False, card_obj=card)


    # Testing Code:
    test = request.slots["test"] 

    if test == None:
        return alexa.create_response("Could not find a test phrase!")
    
    return alexa.create_response("Hello World this is my test {}".format(test),
                                 end_session=False)