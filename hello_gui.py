# import everything from Tkinter
from Tkinter import *

# create a class "Application"
class Application(Frame):
    # response when say_hi function is called upon
    def say_hi(self):
        print "Hello world!"

    # create Widegets
    def createWidgets(self):
        # create QUIT Button
        self.QUIT = Button(self)
        # Text on the Button
        self.QUIT["text"] = "QUIT"
        # foreground color
        self.QUIT["fg"]   = "red"
        # background color
        self.QUIT["bg"]   = "blue"
        # command associated with the click
        self.QUIT["command"] =  self.quit
        # position of the button
        self.QUIT.pack({"side": "right"})
        # second Button
        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack({"side": "right"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

# initialize Tkinter
root = Tk()
# giving the main window a name
root.title("Hello")

app = Application(master=root)
app.mainloop()
root.destroy()
