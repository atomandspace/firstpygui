# import everything from Tkinter
from Tkinter import *

# create a class "Application"
class Application(Frame):

    # response for addition button
    def add(self):
        print "first number a?"
        a=float(raw_input())
        print "second number b?"
        b=float(raw_input())
        print "sum of %r and %r is %r:" % (a,b,a+b)

    # response for subtract button
    def subtract(self):
        print "first number a?"
        a=float(raw_input())
        print "second number b?"
        b=float(raw_input())
        print "sum of %r and %r is %r:" % (a,b,a-b)
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

        # addition button
        self.third = Button(self)
        self.third["text"]="Add",
        self.third["command"]=self.add
        self.third.pack({"side": "top"})

        # subtract button
        self.third = Button(self)
        self.third["text"]="Add",
        self.third["command"]=self.add
        self.third.pack({"side": "top"})

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
