# Program for picking a killer, location, and weapon.

#import random module, weapon list, location list, and suspects dictionaries
import random
from weaponlist import weapon_list
from Place_List import place_of_murdery
from suspects import suspects

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





