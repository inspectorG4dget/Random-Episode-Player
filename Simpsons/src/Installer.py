'''
Created on Aug 7, 2010

@author: ashwin
'''
from os.path import isdir
from os import listdir as ls
import easygui, shutil
easygui.msgbox("Installing", "Ashwin's Badass Simpsons Player", ok_button="Begin Installation")
installpath = easygui.diropenbox("Choose Installation Location", "Ashwin's Badass Simpsons Player", "C:\\Program Files\\Random Player")
for f in [i for i in ls(".") if isdir(i)]:
	shutil.copy(f, installpath)

easygui.msgbox("Installation Finished", "Ashwin's Badass Simpsons Player")