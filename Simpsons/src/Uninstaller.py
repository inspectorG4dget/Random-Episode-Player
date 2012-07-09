'''
Created on Aug 7, 2010

@author: ashwin
'''
from os.path import isdir
from os import listdir as ls, chdir as cd
import easygui, shutil
easygui.msgbox("Uninstallation", "Ashwin's Badass Simpsons Player", ok_button="Begin Uninstallation")
easygui.msgbox("By default, this program should be installed in: C:\\Program Files\\Random Player\\", \
				"Ashwin's Badass Simpsons Player", ok_button="Begin Uninstallation")

installpath = easygui.diropenbox("Where is the program installed?", "Ashwin's Badass Simpsons Player", "C:\\Program Files\\Random Player\\")
cd(installpath)
shutil.rmtree(installpath)

easygui.msgbox("Uninstallation Finished", "Ashwin's Badass Simpsons Player")