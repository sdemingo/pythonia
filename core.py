
from turtle import *
from tkinter import Button,Label,filedialog
import os
import sys
import signal
import traceback

HEIGHT=500
WIDTH=500

class Agent(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.counter=0

    def put(self,n=1):
        self.counter+=n
        
    def take(self,n=1):
        if (self.counter > n):
            self.counter-=n
        else:
            raise AgentError("Agent's counter is zero")

    def reset(self):
        Turtle.reset(self)
        self.counter=0

    def info(self,show=True):
        self.pu()
        self.setpos(self.xcor()-10,self.ycor()-10)
        self.write(self.counter)
        self.setpos(self.xcor()+10,self.ycor()+10)
        self.pd()
        

class AgentError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Script:
    def __init__(self):
        self.setFile("main.py")

    def setFile(self,filepath):
        self.filename=os.path.basename(filepath)
        self.filepath=filepath
        
    def reload(self):
        hero.reset()
        gui.reset()
        exec(open(self.filename).read())
        hero.info()



class GUI:
    def __init__(self):
        wn = Screen()
        setup(WIDTH, HEIGHT,0,0)

        self.screen=wn
        self.screen.title("Pythonia 0.1")
        canvas = self.screen.getcanvas()
        canvas.master.minsize(WIDTH,HEIGHT)
        
        buttonOpen = Button(canvas.master, text="Open", height=1, width=5,  command=self.open_script)
        buttonEdit = Button(canvas.master, text="Edit", height=1, width=5, command=self.edit_script)
        buttonRun = Button(canvas.master, text="Run", height=1, width=5, command=self.run_script)
        labelFile = Label(canvas.master, text=script.filename, bg="#fff")
        self.labelError = Label(canvas.master, text="", bg="#fff",fg="#C10000")

        buttonOpen.place(x=5, y=5)
        buttonEdit.place(x=75, y=5)
        buttonRun.place(x=145, y=5)
        labelFile.place(x=215,y=10)
        self.labelError.place(x=7,y=50)

    def reset(self):
        self.labelError.config(text="")
        
    def print_error(self,error):
        exc_type, ex, tb = sys.exc_info()
        imported_tb_info = traceback.extract_tb(tb)[-1]
        line_number = imported_tb_info[1]
        print_format = 'ERROR en línea {}: {}'
        self.labelError.config(text=print_format.format(line_number, ex))

    def run_script(self):
        try:
            script.reload()
        except Exception as error:
            self.print_error(error)
        
    def open_script(self):
        filepath = filedialog.askopenfilename()
        script.setFile(filepath)

    def edit_script(self):
        os.system("gedit "+script.filepath+" &")


    
def handler(signum, frame):
    print ("Cierra la ventana para cerrar la aplicación")





hero=Agent()
script=Script()
gui=GUI()


if __name__=='__main__':

    signal.signal(signal.SIGINT, handler)
    gui.screen.onkey(gui.run_script,'F5')

    gui.run_script()    
    gui.screen.listen()
    gui.screen.mainloop()

