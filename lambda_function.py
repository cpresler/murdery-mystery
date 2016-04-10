"""
In this file we specify default event handlers which are then populated into the handler map using metaprogramming
Copyright Anjishnu Kumar 2015
Happy Hacking!
"""

from ask import alexa
import random
from weaponlist import weapon_list
from Place_List import place_of_murdery
from suspects import suspects

#limit number of turns
turn = 3
killer = {}
killer_name = ''
killer_hair = ''
killer_scarf = ''
killer_hat = ''
killer_freckles = ''
killer_pet = ''
killer_glasses = ''
suspect = ''


def lambda_handler(request_obj, context=None):
    '''
    This is the main function to enter to enter into this code.
    If you are hosting this code on AWS Lambda, this should be the entry point.
    Otherwise your server can hit this code as long as you remember that the
    input 'request_obj' is JSON request converted into a nested python object.
    '''

    metadata = {'user_name' : 'SomeRandomDude'} # add your own metadata to the request using key value pairs

    ''' inject user relevant metadata into the request if you want to, here.
    e.g. Something like :
    ... metadata = {'user_name' : some_database.query_user_name(request.get_user_id())}

    Then in the handler function you can do something like -
    ... return alexa.create_response('Hello there {}!'.format(request.metadata['user_name']))
    '''
    return alexa.route_request(request_obj, metadata)


@alexa.default_handler()
def default_handler(request):
    """ The default handler gets invoked if no handler is set for a request """
    return alexa.create_response(message="I don't know how to handle that request.")


@alexa.request_handler("LaunchRequest")
def launch_request_handler(request):
    #limit number of turns
    turn = 3

    #use random module to select a random murder weapon
    murder_weapon = random.choice(weapon_list)

    #use random module to select a random murder location
    murder_location = random.choice(place_of_murdery)

    #create a suspected killers list
    suspected_killers = []

    #interate through the suspect dictionaries and append the 'name' values to the suspected killers list
    for suspect in suspects.keys():
        suspected_killers.append(suspects[suspect])

    #use random module to select a random killer
    killer = random.choice(suspected_killers)

    killer_name = killer['name']
    killer_hair = killer['facial hair']
    killer_scarf = killer['scarf']
    killer_hat = killer['hat']
    killer_freckles = killer['freckles']
    killer_pet = killer['pet']
    killer_glasses = killer['glasses']

    return alexa.create_response(message="One of you killed with a {0} in the {1}. Your team is allowed two questions and one guess to figure out who the murderer is. Guess correctly and they'll be arrested and tried. Guess wrong and they go free forever. No pressure. So, what is your first question?".format(murder_weapon, murder_location))


@alexa.request_handler("SessionEndedRequest")
def session_ended_request_handler(request):
    return alexa.create_response(message="Goodbye!")


@alexa.intent_handler('GetSuspect')
def get_suspect_intent_handler(request):
    """
    Whodunnit??
    """
    # Get variables like userId, slots, intent name etc from the 'Request' object
    suspect = request.slots["Suspect"]
    suspect = suspect.lower()


    if suspect == None:
        return alexa.create_response("Could not find a suspect!")

    elif suspect == killer_name:
        return alexa.create_response("You are correct! Congratulations, you have saved the day. Well, not the murder victims day. Or the killer's day.  But someone's day was surely saved.", end_session=True)

    elif suspect != killer_name and turn > 1:
        return alexa.create_response("Nope! You're wrong. Ask for a clue about the killer or guess the killer again.")
        turn = turn -1

    elif suspect != killer_name and turn == 1:
        return alexa.create_response("Too bad so sad! You're wrong. You have one more guess to catch the killer.")
        turn = turn - 1

    else:
        return alexa.create_response("You are wrong, the killer will now go free and the victim's murder will never be solved. Way to ruin everything. ", end_session=True)


@alexa.intent_handler('GetAttr')
def get_attr_handler(request):
      """
      20 questions -- except not
      """

      # Get variables like userId, slots, intent name etc from the 'Request' object
      attr = request.slots["Attr"]
      attr = attr.lower()

      if attr == None:
        return alexa.create_response("I'm sorry I didn't understand your question, can you please ask again?")
      elif (turn > 1):
        if(attr == 'facial hair' or attr == 'beard' or attr == 'moustache'):
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
