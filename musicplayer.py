import pygame
pygame.mixer.init()
music = pygame.mixer.music

# Docs: #
# music.load(file)
# music.play()
# music.stop()

commands = ["Available Commands:", "start", "exit", "stop", "help", "tracks"]
tracks = ["Tracks:", "animals.aiff", "devmusic.aiff"]

def checkCommands(input):
    if input in commands:
        return True
    else:
        return False

def printList(list):
    print "==="
    print list[0]
    for item in list[1:]:
        print item
    print "==="

command = raw_input("Command: ").lower()
exitCode = 0

# Main Program Loop #
while exitCode != 1:

    # Validates User Input #
    while checkCommands(command) == False:
        print "Command not recognized. Type 'help' for list available commands"
        command = raw_input("Command: ").lower()

    if command == "start":
        printList(tracks)
        musicFile = raw_input("Track to play: ")
        music.load(musicFile)
        music.play()
        print "Playing music..."
        command = raw_input("Command: ").lower()
    elif command == "stop":
        music.stop()
        print "Music stopped..."
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
