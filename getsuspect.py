# Program for the GetSuspect intent
@alexa.intent_handler('GetSuspect')
def get_suspect_intent_handler(request):
    """
    Whodunnit??
    """
    # Get variables like userId, slots, intent name etc from the 'Request' object
    suspect = request.slots["Suspect"]
    suspect = suspect.lowercase 


    if suspect == None:
        return alexa.create_response("Could not find a suspect!")

    elif suspect == killer_name:
        return alexa.create_response("You are correct! Congratulations, you have saved the day. Well, not the murder victims day. Or the killer’s day.  But someone’s day was surely saved.", end_session=True)

    elif susepct != killer_name and turn >1:
        return alexa.create_response("Nope! You're wrong. Ask for a clue about the killer or guess the killer again.")
        turn = turn -1

    elif suspect != killer_name and turn = 1:
        return alexa.create_response("Too bad so sad! You're wrong. You have one more guess to catch the killer.")
        turn = turn - 1

    else:
        return alexa.create_response("You are wrong, the killer will now go free and the victim’s murder will never be solved. Way to ruin everything. ", end_session=True)

