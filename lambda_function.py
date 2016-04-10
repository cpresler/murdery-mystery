# Placing the lambda function here in un-zipped form for easy reference.

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



def lambda_handler(request_obj, context=None):
    '''
    This is the main function to enter to enter into this code.
    If you are hosting this code on AWS Lambda, this should be the entry point.
    Otherwise your server can hit this code as long as you remember that the
    input 'request_obj' is JSON request converted into a nested python object.
    '''

    metadata = {'user_name' : 'SomeRandomDude'} # add your own metadata to the request using key value pairs
    
    if not 
    
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
    #use random module to select a random murder weapon
    murder_weapon = random.choice(weapon_list)

    #use random module to select a random murder location
    murder_location = random.choice(place_of_murdery)

    #create a suspected killers list
    suspected_killers = []

    #interate through the suspect dictionaries and append the 'name' values to the suspected killers list
    for suspect in suspects.keys():
        suspected_killers.append(suspects[suspect]['name'])

    #use random module to select a random killer
    killer = random.choice(suspected_killers)


    return alexa.create_response(message="One of you killed with a {0} in the {1}. Your team is allowed two questions and one guess to figure out who the murderer is. Guess correctly and they’ll be arrested and tried. Guess wrong and they go free forever.".format(murder_weapon, murder_location))


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


    if suspect == None:
        return alexa.create_response("Could not find a suspect!")

    elif suspect == killer:
        return alexa.create_response("You are correct! Congratulations, you have saved the day. Well, not the murder victims day. Or the killer’s day.  But someone’s day was surely saved.", end_session=True)

    else:
        return alexa.create_response("You are wrong, the killer will now go free and the victim’s murder will never be solved. Way to ruin everything. ", end_session=True)


@alexa.intent_handler('GetAttr')
def get_attr_handler(request):
    """
    You can insert arbitrary business logic code here    
    """

    # Get variables like userId, slots, intent name etc from the 'Request' object
    test = request.slots["Attr"] 

    return alexa.create_response(message="The attribute that was passed was {}".format(test))
