#!/usr/bin/env python

''' Roku remote application '''

from roku import Roku
from ip import ip_address
import sys

roku = Roku(ip_address)

def start():
    print 'Type \'help\' to view commands'

    while True:

        # receive commands
        command = raw_input('Please enter command: ')

        if command == 'home':
            home()
        if command == 'search':
            search()
        if command == 'r':
            right()
        if command == 'l':
            left()
        if command == 'u':
            up()
        if command == 'd':
            down()
        if command == 'b':
            back()
        if command == 'select':
            select()
        if command == 'play':
            play()
        if command == 'netflix':
            netflix()
        if command == 'help':
            help()
        if command == 'exit':
            sys.exit(1)
        else:
            print 'Invalid command. Type \'help\' to view list of commands.'

def help():
    print '\nCommands:'
    print '----------------------------'
    print 'home: go to home screen'
    print 'search: search for title'
    print 'r: right'
    print 'l: left'
    print 'u: up'
    print 'd: down'
    print 'b: go back'
    print 'select: select title'
    print 'play: play'
    print 'netflix: go to netflix'
    print 'exit: exit remote'
    print '----------------------------'

def home():
    ''' home '''
    roku.home()

def search():
    ''' search '''
    #TODO: implement search with roku.iterate()

def right():
    ''' move right '''
    roku.right()

def left():
    ''' move left '''
    roku.left()

def up():
    ''' move up '''
    roku.up()

def down():
    ''' move down '''
    roku.down()

def back():
    ''' go back '''
    roku.back()

def select():
    ''' select '''
    roku.select()

def play():
    ''' play '''
    roku.play()

def netflix():
    ''' launch netflix '''
    netflix = roku['Netflix']
    netflix.launch()


if __name__ == '__main__':
    start()
