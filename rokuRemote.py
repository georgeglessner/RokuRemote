#!/usr/bin/env python

''' Roku remote application '''

from Tkinter import *
from ip import *
from roku import Roku
from PIL import ImageTk
from PIL import Image

# get location of roku
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


class Application(Frame):

    def home(self):
        roku.home()

    def right(self):
        roku.right()

    def left(self):
        roku.left()

    def up(self):
        roku.up()

    def down(self):
        roku.down()

    def back(self):
        roku.back()

    def select(self):
        roku.select()

    def play(self):
        roku.play()

    def netflix(self):
        netflix = roku['Netflix']
        netflix.launch()

    def createWidgets(self):

        #TODO: implement search?
        
        # create images for buttons
        home_button = Image.open("buttons/home_button.png")
        home_button = home_button.resize((50, 50), Image.ANTIALIAS)
        self.home_button = ImageTk.PhotoImage(home_button)
        self.left_button = ImageTk.PhotoImage(
            Image.open("buttons/left_button.png"))
        self.right_button = ImageTk.PhotoImage(
            Image.open("buttons/right_button.png"))
        self.up_button = ImageTk.PhotoImage(
            Image.open("buttons/up_button.png"))
        self.down_button = ImageTk.PhotoImage(
            Image.open("buttons/down_button.png"))
        self.play_button = ImageTk.PhotoImage(
            Image.open("buttons/play_button.png"))
        self.pause_button = ImageTk.PhotoImage(
            Image.open("buttons/pause_button.png"))
        netflix_button = Image.open("buttons/netflix_button.jpeg")
        netflix_button = netflix_button.resize((100, 50), Image.ANTIALIAS)
        self.netflix_button = ImageTk.PhotoImage(netflix_button)

        # create buttons
        self.HOME = Button(self)
        # self.HOME["text"] = "Home"
        self.HOME["command"] = self.home

        self.LEFT = Button(self)
        self.LEFT["text"] = "Left"
        self.LEFT["command"] = self.left

        self.RIGHT = Button(self)
        self.RIGHT["text"] = "Right"
        self.RIGHT["command"] = self.right

        self.UP = Button(self)
        self.UP["text"] = "Up"
        self.UP["command"] = self.up

        self.DOWN = Button(self)
        self.DOWN["text"] = "Down"
        self.DOWN["command"] = self.down

        self.NETFLIX = Button(self)
        self.NETFLIX["text"] = "Netflix",
        self.NETFLIX["command"] = self.netflix

        self.SELECT = Button(self)
        self.SELECT["text"] = "Select"
        self.SELECT["command"] = self.select

        self.PAUSE = Button(self)
        self.PAUSE["text"] = "Select"
        self.PAUSE["command"] = self.select

        # Netflix button
        self.NETFLIX.config(image=self.netflix_button,
                            width="100", height="50")
        self.NETFLIX.pack(side='bottom')

        self.HOME.config(image=self.home_button, width="50", height="50")
        self.HOME.pack(side='bottom')

        # left button
        self.LEFT.config(image=self.left_button, width="100", height="100")
        self.LEFT.pack(side='left', expand=True)

        # right button
        self.RIGHT.config(image=self.right_button, width="100", height="100")
        self.RIGHT.pack(side='right', expand=True)

        # up button
        self.UP.config(image=self.up_button, width="100", height="100")
        self.UP.pack(side='top', expand=True)

        # down button
        self.DOWN.config(image=self.down_button, width="100", height="100")
        self.DOWN.pack(side='bottom', expand=True)

        # play button
        self.SELECT.config(image=self.play_button, width="50", height="50")
        self.SELECT.pack(side='left', expand=True)

        # pause button
        self.PAUSE.config(image=self.pause_button, width="50", height="50")
        self.PAUSE.pack(side='right', expand=True)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


root = Tk()
root.title('Roku Remote')
root.geometry('350x400')
app = Application(master=root)
app.mainloop()
try:
    root.destroy()
except:
    pass
