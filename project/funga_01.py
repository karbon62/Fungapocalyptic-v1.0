from sys import exit
from random import randint
#Entering this line to see if it makes any difference to making the code run 

class Scene(object):
	
	def enter(self):
		exit(1, esc)
# This code has been refractured, added the esc function. 

class Engine(object):
	
	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True:
			print "\n---------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

#class Death(Scene):
#	def enter(self):
#		print "You imbacile, you couldn't even get through the first wave, we shouldn't of have depended on you... there is only... profound sadness.....",
#		print "we shouldn't of have depended on you, there is only profound sadness.....",
#		"We were all counting on you. Please dont give up on us now, we need your help!"
	 # This code has been refractured, changed the print string. 

	#def enter(self):
	#	print Death.quips[randint(0, len,(self.quips)-1)] # This code has been refractured, added an additional esc ini the randint. 
	#	eixt(1) # This has been refractured, changed the esc



class FirstLevel(Scene): 
# The origial of Central corridor code has been refractured. 
	
	def enter(self):
		print "Before the dawn of Humans, Earth was a place of purity, clean."
		print "Earth had given us a home, Humans exploited everything that it had to offer"
		print "Now, Polution and exploitation has brought it to its knees."
		print "There a virus brewing, a deadly Spores that fills the air with poisonus oxygen. Many have not been able to survive this emdemic, time has now come that you must do what you can to save whats left. Life and Death, its in your Hands!" 
		print "Type (1) If you Care (2) If you have not faith"		 
		
		action = raw_input("> ")
		
		if action == "1":
			print "Lets do this!"
			return 'attack_first_wave'
		
		elif action == "2":
			print "This just isn't going to work"
			return 'first_level'
		# This has been refractured, changed the print script 


		#if action == "Pog":
		#	print "We are depending on you, take this serious!"
		#	return 'death'

		#elif action == "dodge!":
		#	print "We are dying"
		#	return 'death'

		#else:
		#	print "You got the hang of this!"
		#	return 'attack_first_wave'

class AttackFirstWave(Scene): # This has been refractured - original script is LaserWeaponArmory(Scene)

	def enter(self):
		print "So, I've calculated the area, there are 6 spores, if you need 6 fungus to eliminate 1 how many will you need in total?" #This will need to be refractured 
		#chance = "%d" % (int(12))
		#eliminate = raw_input ("Please choose the right one, we're all counting on you > ") #This will have to be edited 
		#eliminating = 0

		action = raw_input("Please choose the right one, we're all counting on you >") # Raw_input has been changed to adap to the script. 

		#while eliminate != chance and eliminating < 13:
			#print "Well Done!"

			#eliminating += 6
			#eliminate = raw_input("So, I've calculated the area, there are 6 spores, if you need 6 fungus to eliminate 1 how many will you need in total?")

		if action == "36":
			print "I really didn't think you had it in you, I admit, I was wrong. Now go back there, and kick ass!"	
			return 'attack_second_wave'

		else: 
			print "You imbacile, you couldn't even get through the first wave, we shouldn't of have depended on you, there is only profound sadness....."
			return()
			# I will have to include additional elif statements "If User enters anything else besides 36 + "

# The code below will have to refractured so that the second wave can take place

class AttackSecondWave(Scene):
	def enter(self):
		print "Hello Again, I see that you've passed through to the second wave!"

		action = raw_input ("if you need 5 fungus to eliminate them all, how many will you need to plant in total?")

		if action == "125":
			return 'attack_third_wave'

#	elif action:
#		pass

		else:
			print "You imbecile, you couldn't even get through the first wave, we shouldn't of have depended on you, there is only profound sadness....."
			return()

class AttackThirdWave(Scene):
	def enter(self):
		print "My oh My, you have made it quite far, so here goes the last wave of this level"
		
		action = raw_input ("There are 60 spores in total, 6 are inbred, which means that they make up half of that groups total unit and 12 that are super spores which means that you will need double the amount of Fungus to rid the area, how many will you need in total to rid all the spores if you need 5 to eliminate 1?")
	
		if action == "250":
			print "You did it, you help save our land! Our Earth and all living things deeply thank you with all our gratitudes. Please dont stop now, we are close to purifying Earth. And once more need your help!"
			return 'end_of_game'

		else:
			print "We were all counting on you. Please dont give up on us now, we need your help!"
			return()
# This will be the first set of code. Wrapping everything up from below onwards, if anything else added above will also have to alter below. 

#class EndOfGame(Scene):
#	print "you did it" 

class Map(object):

	scenes = {
		'first_level': FirstLevel(),
		'attack_first_wave': AttackFirstWave(),
		'attack_second_wave': AttackSecondWave(),
		'attack_third_wave': AttackThirdWave(),
		#'end_of_game': EndOfGame(),
		#'death': Death()

	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)

	def opening_scene(self):
		return self.next_scene(self.start_scene)
# Code above has NOT been refractured - if error alter to make sure that it works accordingly

a_map = Map('first_level')
a_game = Engine(a_map)
a_game.play()








		