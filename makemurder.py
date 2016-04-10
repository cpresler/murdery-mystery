# Program for picking a killer, location, and weapon.

#import random module, weapon list, location list, and suspects dictionaries
import random
from weaponlist import weapon_list
from Place_List import place_of_murdery
from suspects import suspects

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


return alexa.create_response(message="One of you killed with a {0} in the {1}. Your team is allowed two questions and one guess to figure out who the murderer is. Guess correctly and they’ll be arrested and tried. Guess wrong and they go free forever.".format(murder_weapon, murder_location))







