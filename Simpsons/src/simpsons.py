'''
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

from os import getcwd as pwd, listdir as ls, system as cmd, chdir as cd
from random import randint as rand

def pickAFile():
        '''Pick a random file or directory from the current directory and return it'''
        files = [i for i in ls('.') if not ignore in i]
        f = files[rand(0, (len(files) -1))]
        return f

def run():
        '''pick a file/dir from the current directory. If it's a file, play it. 
        Else (we picked a directory) cd into that directory and recurse.'''

        f = pickAFile()
        if '.' in f:	# f is a file\
                cmd('"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe" "%s"&' %f)
        else:	# f is a dir
                cd(f)
                run()

if __name__ == "__main__":
        ignore = pwd().split('\\')[-1]
        cd("..")
        run()
