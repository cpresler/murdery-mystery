@alexa.intent_handler('GetTest')
def get_testing(request):
    """
    You can insert arbitrary business logic code here    
    """

    # Get variables like userId, slots, intent name etc from the 'Request' object
    test = request.slots["test"] 

    if test == None:
        return alexa.create_response("Could not find a test phrase!")
    
    return alexa.create_response("Hello World this is my test {}".format(test),
                                 end_session=False)