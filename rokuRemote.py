#!/usr/bin/env python

''' Roku remote application '''

from roku import Roku
from ip import *
import sys

import signal

while True:
    location = raw_input('Upstairs/Downostairs? [u/d]: ')

    # upstairs roku
    if location == 'u':
        roku = Roku(upstairs)
        break
    # downstairs roku
    if location == 'd':
        roku = Roku(downstairs)
        break
    print 'Invalid input.'


def start():
    print 'Type \'help\' to view commands'

    while True:

        # receive commands
        command = raw_input('Please enter command: ')

        # TODO: implement arrow key directions, get search working
        if command == 'h':
            print 'home'
            roku.home()
        elif command == 'r':
            roku.right()
        elif command == 'l':
            roku.left()
        elif command == 'u':
            roku.up()
        elif command == 'd':
            roku.down()
        elif command == 'b':
            roku.back()
        elif command == 's':
            roku.select()
        elif command == 'p':
            roku.play()
        elif command == 'n':
            netflix = roku['Netflix']
            netflix.launch()
        elif command == 'help':
            help()
        elif command == 'exit':
            print '\nRemote off\n'
            sys.exit(1)
        else:
            print 'Invalid command. Type \'help\' to view list of commands.'


def help():
    print '\nCommands:'
    print '----------------------------'
    print 'h: go to home screen'
    print 'r: right'
    print 'l: left'
    print 'u: up'
    print 'd: down'
    print 'b: go back'
    print 'p: play/pause'
    print 's: select title'
    print 'n: go to netflix'
    print 'exit: exit remote'
    print '----------------------------'

def sigint_handler(signum, frame):
    print '\n\nRemote off\n'
    sys.exit(1)

signal.signal(signal.SIGINT, sigint_handler)

if __name__ == '__main__':
    start()
