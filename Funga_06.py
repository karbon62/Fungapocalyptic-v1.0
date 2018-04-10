import pprint
from sys import exit
from random import randint
from FungaStoryText import *

class Scene(object):

    def enter(self):
        sys.exit()

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):
    def enter(self):
        print ("{}".format(deathStart))
        print ("{}".format.deathEnd)
        print ("{}".format(linebreak))

        return 'first_level'

class Intro(Scene):

    def enter(self):
        print ("{}".format(linebreak))
        print ("{}".format(introStart))
        print ("{}".format(introVerse1))
        print ("{}".format(introVerse2))
        print ("{}".format(introVerse3))
        print ("{}".format(introVerse4))
        print ("{}".format(linebreak))
        print ("{}".format(introInteract))
        print ("{}".format(linebreak))

        action = input(">>> ")

        if action == "1":
            print ("{}".format(introStartActionY))
            print ("{}".format(linebreak))
            return 'attack_first_wave'

        elif action == "2":
            print ("{}".format(linebreak))
            print ("{}".format(introStartActionN))
            return exit(0)

        else:
            return 'game_over_screen'


class AttackFirstWave(Scene):

    def enter(self):
        print ("{}".format(linebreak))
        print ("{}".format(firstWaveIntro))
        print ("{}".format(linebreak))

        action = input("{}".format(firstWaveActionText))

        if action == "36":
            print ("{}".format(linebreak))
            print ("{}".format(firstWavePass))
            print ("{}".format(linebreak))
            return 'second wave'

        elif action != "36":
            print ("{}".format(linebreak))
            print ("{}".format(firstWaveFail))
            print ("{}".format(linebreak))
            return 'death'

        else:
            return 'game_over_screen'


class AttackSecondWave(Scene):

    def enter(self):
        print ("{}".format(linebreak))
        print ("{}".format(secondWaveIntro))
        print ("{}".format(linebreak))

        action = input("{}".format(secondWaveActionText))

        if action == "30":
            return 'attack_third_wave'

        elif action != "30":
            print ("{}".format(linebreak))
            print ("{}".format(secondWaveFail))
            print ("{}".format(linebreak))
            return 'death'

        else:
            return 'game_over_screen'


class AttackThirdWave(Scene):

    def enter(self):
        print ("{}".format(linebreak))
        print ("{}".format(thirdWaveIntro))
        print ("{}".format(linebreak))

        action = input("{}".format(thirdWaveActionText))

        if action == "250":
            print ("{}".format(linebreak))
            print ("{}".format(thirdWavePass))
            print ("{}".format(linebreak))
            return 'score_board'

        elif action != "250":
            return 'death'

        else:
            print ("{}".format(linebreak))
            print ("{}".format(thirdWaveFail))
            print ("{}".format(linebreak))
            return 'game_over_screen'


class GameOverScreen(Scene):
# untested

    def enter(self):
        print ("{}".format(Death))
        return 'player_details'

    def player_details(self):
        print ("{}".format(linebreak))
        var = input("{}".format())
        print ("{}".format())
        print ("{}".format(linebreak))
        return 'score_board'

    def ScoreBoard(self):
        print ("{},  {}".format(name, level))
        print ("{}".format())
        print ("{}".format())
        return 'retry'

class PlayerDetails(Scene):

    def enter(self):
        print ("Enter Name")
        input(">>")

        return input("").write()



class Retry(Scene):
# untested

    def enter(self):
        print("{}, {}".format(Y, N))

        retry = input(">>> ")

        if retry == Y:
            return 'first_level'
        else:
            return 'exit'


class ScoreBoard(Scene):
# untested

    attack_first_wave = '25'
    attack_second_wave = '25'
    attack_third_wave = '50'

    def player(self):

        player_details = player
        score_board = player_score
        new_score = player_score + player

    def score(self):
        empty = 0
        new = new_score
        if new_score == +1:
            return print("{}".format(score))

        if new_score:
            print ("{}".format(score))
            print ("{}".format(playagain))


class Map(object):

	scenes = {
		'first_level': Intro(),
		'attack_first_wave': AttackFirstWave(),
		'attack_second_wave': AttackSecondWave(),
		'attack_third_wave': AttackThirdWave(),
		'death': Death(),
		#'player_details': PlayerDetails(),
		'game_over_screen': GameOverScreen(),
		'score_board': ScoreBoard(),
        'retry': Retry(),

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
