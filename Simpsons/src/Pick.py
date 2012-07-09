'''
Created on Aug 6, 2010

@author: ashwin
'''
from os import getcwd as pwd, listdir as ls, system as cmd, chdir as cd
from os.path import isdir
from random import randint as rand
from cPickle import dump as save, load
import easygui, sys
ignore = pwd()

def getDir():
	return easygui.diropenbox(msg="Pick the folder where all the Simpsons Files are located", \
							 title="Ashwin's Badass Random Simpsons Player")
	
def getPlayer():
	return easygui.fileopenbox(msg="Choose your favorite Media Player", \
							 title="Ashwin's Badass Random Simpsons Player")
	
def about():
	text = """General Stuff:
			I originally wrote this program for a friend by the name of Freddy. 
			This program was meant to play a random Simpsons episode.
			As I wrote this program, however, I came to the realization that 
			it can be used to play any of a bunch of random media files.
			
			Program Specs (for the techies):
			This program has one config file: UserSettings.SIMPSONS.
			Nothing too bad happens if you delete it. If you do so, all that will happen is that 
			you will be prompted to input your settings on the next run"""

def viewSettings():
	playerpath = load("UserSettings.SIMPSONS")
	easygui.msgbox(msg="Your current Media Player is: %s" %playerpath, title="Ashwin's Badass Simpsons Player")
	
def changeSettings():
	easygui.msgbox("Choose your favorite Media Player. This can be changed later", "Ashwin's Badass Simpsons Player")
	playerpath = easygui.fileopenbox(msg="Choose your favorite Media Player", \
									 title="Ashwin's Badass Random Simpsons Player")
	
	if not playerpath:
		sys.exit(0)

	save(playerpath, "UserSettings.SIMPSONS")
	easygui.msgbox("Your new settings have been changed", "Ashwin's Badass Random Simpsons Player")
	

def play(rootDir, playerPath=None):
	cd(rootDir)
	files = [i for i in ls('.') if not ignore in i or not (isdir(i) and not(ls(i)))]
	choice = files[rand(0, len(files)-1)]
	if isdir(choice):
		play(choice)
	else:
		if not playerPath:
			cmd("%s %s" %(getPlayer(), choice))
		else:
			cmd("%s %s" %(playerPath, choice))

if __name__ == "__main__":
	if not 'UserSettings.SIMPSONS' in ls("."):  # first time launch
		easygui.msgbox("Welcome to your first time using Ashwin's Badass Simpsons Player", \
					   "Ashwin's Badass Simpsons Player")
		
		goAhead = easygui.ccbox("Welcome to your first time using Ashwin's Badass Simpsons Player", \
					   "Ashwin's Badass Simpsons Player")
		if goAhead:
			changeSettings()
		
	else:   # program has been launched before
		
		name_to_func = {
			'View Settings'	 : viewSettings(),
			'Change Settings'   : changeSettings(),
			'Play an Episode'   : play,
			'About'			 : about()
		}
		
		choice = easygui.choicebox(msg="What would you like to do?", \
								   title="Ashwin's Badass Simpsons Player", \
								   choices=name_to_func.keys())
		if not choice:
			sys.exit(0)
			
		if choice == "Play an Episode":
			mustLoadSettings = easygui.buttonbox(msg="Use Previous settings?", \
									 title="Ashwin's Badass Random Simpsons Player", \
									 choices=("Yes", "No"))
		
			if mustLoadSettings == "YES":
				playerPath = load(open('UserSettings.SIMPSONS'))
				save = easygui.ynbox("Save New Settings?", "Ashwin's Badass Simpsons Player")
				if save:
					try:
						save(playerPath, "UserSettings.SIMPSONS")
						easygui.msgbox("New Settings Saved", "Ashwin's Badass Simpsons Player")
					except Exception, e:
						easygui.msgbox("ERROR:\n%s"%e, "Ashwin's Badass Simpsons Player")
			
				rootDir = None
				while not rootDir:
					rootDir = easygui.diropenbox("Where are all the show files located?", "Ashwin's Badass Simpsons Player")
	
				play(rootDir, playerPath)