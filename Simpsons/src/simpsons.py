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
