'''
Created on Aug 7, 2010

@author: ashwin

 Licensed to Ashwin Panchapakesan under one or more
 contributor license agreements.  See the NOTICE file distributed with
 this work for additional information regarding copyright ownership.
 Ashwin licenses this file to You under the Apache License, Version 2.0
 (the "License"); you may not use this file except in compliance with
 the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
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