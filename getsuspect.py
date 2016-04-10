# Program for the GetSuspect intent
@alexa.intent_handler('GetSuspect')
def get_suspect_intent_handler(request):
    """
    Whodunnit??
    """
    # Get variables like userId, slots, intent name etc from the 'Request' object
    suspect = request.slots["Suspect"] 


    if suspect == None:
        return alexa.create_response("Could not find a suspect!")

    elif suspect == murderer:
        return alexa.create_response("You are correct! Congratulations, you have saved the day. Well, not the murder victims day. Or the killer’s day.  But someone’s day was surely saved.", end_session=True)

    else:
        return alexa.create_response("You are wrong, the killer will now go free and victim’s murder will never be solved. Way to ruin everything. ", end_session=True)

