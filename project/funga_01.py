from sys import exit
from random import randint

class Scene(object):
	
	def enter(self):
		exit(1)

class Engine(object):
	
	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True:
			print "\n---------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)




class Death(Scene):
	def enter(self):
		print "You imbacile, you couldn't even get through the first wave, we shouldn't of have depended on you... there is only... profound sadness.....",
		print "we shouldn't of have depended on you, there is only profound sadness.....",
		"We were all counting on you. Please dont give up on us now, we need your help!"
		return 'first_level'



class FirstLevel(Scene): 
	
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
			return 'death'

		else:
			return 'first_level'


class AttackFirstWave(Scene): 

	def enter(self):
		print "So, I've calculated the area, there are 6 spores, if you need 6 fungus to eliminate 1 how many will you need in total?"

		action = raw_input("Please choose the right one, we're all counting on you >") 


		if action == "36":
			print "I really didn't think you had it in you, I admit, I was wrong. Now go back there, and kick ass!"	
			return 'attack_second_wave'

		elif action != '36':
			print "You imbacile, you couldn't even get through the first wave, we shouldn't of have depended on you, there is only profound sadness....."
			return('death')

		else:
			return 'first_level'



class AttackSecondWave(Scene):
	def enter(self):
		print "Hello Again, I see that you've passed through to the second wave!"

		action = raw_input ("if you need 5 fungus to eliminate them all, how many will you need to plant in total?")

		if action == "125":
			return 'attack_third_wave'

		elif action != "125":
			return 'first_level'
		
		else:
			print "You imbecile, you couldn't even get through the first wave, we shouldn't of have depended on you, what is left is only profound sadness....."
			return('first_level')

		

class AttackThirdWave(Scene):
	def enter(self):
		print "My oh My, you have made it quite far, so here goes the last wave of this level"
		
		action = raw_input ("There are 60 spores in total, 6 are inbred, which means that they make up half of that groups total unit and 12 that are super spores which means that you will need double the amount of Fungus to rid the area, how many will you need in total to rid all the spores if you need 5 to eliminate 1?")
	
		if action == "250":
			print "You did it, you help save our land! Our Earth and all living things deeply thank you with all our gratitudes."
			return 'player_deatils'

		elif action != "250":
			return 'player_deatils'

		else:
			print "We were all counting on you. Please dont give up on us now, we need your help!"
			return('first_level')



class PlayerDetails(Scene):


	var = raw_input("Who Passes Here?? Enter Name Here: ")
	print "you entered ", var



class Map(object):

	scenes = {
		'first_level': FirstLevel(),
		'attack_first_wave': AttackFirstWave(),
		'attack_second_wave': AttackSecondWave(),
		'attack_third_wave': AttackThirdWave(),
		'death': Death(),
		'player_deatils': PlayerDetails(), 

	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)

	def opening_scene(self):
		return self.next_scene(self.start_scene)


a_map = Map('first_level')
a_game = Engine(a_map)
a_game.play()








		