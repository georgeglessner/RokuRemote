#!/usr/bin/env python

''' Roku remote application '''

from roku import Roku
from ip import *
import sys

while True:
    location = raw_input('Upstairs/Downostairs? [u/d]: ')

    if location == 'u':
        roku = Roku(upstairs)
        break
    if location == 'd':
        roku = Roku(downstairs)
        break
    print 'Invalid input.'


def start():
    print 'Type \'help\' to view commands'

    print "Enter Command: "
    while True:

        # receive commands
        command = raw_input('Please enter command: ')

        # TODO: implement arrow key directions, get search working
        if command == 'h':
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
            roku.netflix()
        elif command == 'help':
            help()
        elif command == 'exit':
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


if __name__ == '__main__':
    start()
