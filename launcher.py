# This will be the app used to contain all the Games and their commands to run
import subprocess

def MW():
    subprocess.call(['sh','./MW.sh'])

def hello():
    print('Hello, World!')
    exit()

game = input("Choose a game: ")

if game == 'MW':
    MW()
else:
    hello()
