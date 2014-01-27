# Standard Pygame inits
import pygame
pygame.mixer.init()
music = pygame.mixer.music

# Lists, dirs
commands = ["Available Commands:", "start", "exit", "stop", "pause", "resume", "help", "tracks"]
tracks = ["Tracks:", "animals.aiff", "devmusic.aiff"]

# Functions
def checkIfValid(input, list):
    if input in list:
        return True
    else:
        return False

def startTrack():
    printList(tracks)
    musicFile = raw_input("Track to play: ")

    while checkIfValid(musicFile, tracks) == False:
        print "This is not a track!"
        musicFile = raw_input("Track to play: ").lower()
    
    music.load(musicFile)
    music.play()
    print "Playing music..."

def printList(list):
    print "======"
    print list[0]
    for item in list[1:]:
        print item
    print "======"

# Main Program Loop #
command = raw_input("Command: ").lower()
exitCode = 0

while exitCode != 1:

    # Validates User Input #
    while checkIfValid(command, commands) == False:
        print "Command not recognized. Type 'help' for list available commands"
        command = raw_input("Command: ").lower()

    if command == "start":
        startTrack()
        command = raw_input("Command: ").lower()
    elif command == "stop":
        music.stop()
        print "Music stopped..."
        command = raw_input("Command: ").lower()
    elif command == "pause":
        music.pause()
        print "Music paused... To unpause, use command 'resume'"
        command = raw_input("Command: ").lower()
    elif command == "resume":
        music.unpause()
        print "Music resumed!"
        command = raw_input("Command: ").lower()
    elif command == "help":
        printList(commands)
        command = raw_input("Command: ").lower()
    elif command == "tracks":
        printList(tracks)
        command = raw_input("Command: ").lower()
    elif command == "exit":
        print "EXIT"
        music.stop()
        exitCode = 1
