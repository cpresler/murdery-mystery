# Program for the GetAttr intent
@alexa.intent_handler('GetAttr')
def get_attr_intent_handler(request):
  """
  20 questions -- except not
  """

  # Get variables like userId, slots, intent name etc from the 'Request' object
  attr = request.slots["Attr"]
  attr = attr.lowercase

  if attr == None:
    return alexa.create_response("I'm sorry I didn't understand your question, can you please ask again?")
  elif (turn > 1):
    if(attr == 'facial hair' || attr == 'beard' || attr == 'moustache'):
      if(killer_hair == 'yes'):
        return alexa.create_response("Yes, the killer has facial hair", end_session=False)  
      else:
        return alexa.create_response("No, the killer does not have facial hair", end_session=False) 
    elif(attr == 'scarf'):
      if(killer_scarf == 'yes'):
        return alexa.create_response("Yes they are", end_session=False)  
      else:
        return alexa.create_response("No they are not", end_session=False) 
    elif(attr == 'hat'):
      if(killer_hat == 'yes'):
        return alexa.create_response("Yes, the killer is wearing a hat", end_session=False)  
      else:
        return alexa.create_response("No, the killer does not have a hat", end_session=False) 

    elif(attr == 'freckles'):
      if(killer_freckles == 'yes'):
        return alexa.create_response("The killer has freckles", end_session=False)  
      else:
        return alexa.create_response("No, the killer does not have freckles", end_session=False) 

    elif(attr == 'pet'):
      if(killer_hair == 'yes'):
        return alexa.create_response("The killer does have a pet", end_session=False)  
      else:
        return alexa.create_response("The killer does not have a pet", end_session=False) 

    elif(attr == 'glasses'):
      if(killer_glasses == 'yes'):
      return alexa.create_response("Yes, the killer is wearing glasses", end_session=False)  
      else:
        return alexa.create_response("No, the killer does not have a glasses", end_session=False) 
    else:
      return alexa.create_response("We have not yet discovered this information about the killer.", end_session=False)      
  else:
    #prompt to guess
    return alexa.create_response("You have asked your questions, now it is time to guess the identity of the killer.".format(attr), end_session=False)


def hasAttr(attr):
  # stuff
  
  return answer
