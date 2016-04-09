# Program for the GetAttr intent
@alexa.intent_handler('GetAttr')
def get_attr_intent_handler(request):
  """
  20 questions -- except not
  """

  # Get variables like userId, slots, intent name etc from the 'Request' object
  attr = request.slots["Attr"] 

  if attr == None:
    return alexa.create_response("Could not find an attr!")

  return alexa.create_response("Finding a recipe with the attr {}".format(attr), end_session=False)

def hasAttr(attr):
  # stuff
  
  return answer
