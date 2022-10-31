
from turtle import *
from tkinter import Button,Label,filedialog
import os
import sys
import signal
import traceback

HEIGHT=500
WIDTH=500

class Agent(Turtle):
    def __init__(self,name):
        Turtle.__init__(self)
        self.name=name
        self.counter=0
        self.speed(1)

    def reset(self):
        self.clear()
        self.hideturtle()
        self.counter=0

    def put(self,area):
        self.counter+=1

    def take(self,area):
        if (self.counter > 1):
            self.counter-=1
        else:
            raise AgentError("Agent's counter is zero")

    def info(self):
        x=int(self.xcor())
        y=int(self.ycor())
        return "{:>8.8} [counter:{:2d}  pos:({:3d},{:3d})]\n".format(self.name,self.counter,x,y)


class Area(Agent):
    def __init__(self,name,x,y):
        Agent.__init__(self,name)
        self.shape("circle")
        self.pu()
        self.setposition(x,y)

    def setInitialCounter(self,n):
        self.counter=n
        

class AgentError(Exception):
    def __init__(self, message):
        super().__init__(message)






COLLISION_DISTANCE=30

class World:
    def __init__(self):
        self.agents={}

    def add(self,agent):
        self.agents[agent.name]=agent

    def reset(self):
        for name,agent in self.agents.items():
            agent.reset()
        self.agents={}
        
    def info(self):
        s=""
        for name,agent in self.agents.items():
            s+=agent.info()
        return s

    def detect_collisions(self):
        allnames=self.agents.keys()
        for agent in allnames:
            for other in allnames:
                if (agent!=other):
                    if (self.agents[agent].distance(self.agents[other])<=5):
                        return "ERROR por colisión entre {} y {}".format(agent,other)

    

class GUI:
    def __init__(self):
        wn = Screen()
        setup(WIDTH, HEIGHT,0,0)

        self.scriptpath="main.py"
        self.scriptname=os.path.basename(self.scriptpath)
        self.worldpath="world.py"
        self.worldname=os.path.basename(self.worldpath)
        
        self.screen=wn
        self.screen.title("Pythonia 0.1")
        canvas = self.screen.getcanvas()
        canvas.master.minsize(WIDTH,HEIGHT)
        
        buttonOpen = Button(canvas.master, text="Open", height=1, width=5,  command=self.open_script)
        buttonEdit = Button(canvas.master, text="Edit", height=1, width=5, command=self.edit_script)
        buttonRun = Button(canvas.master, text="Run", height=1, width=5, command=self.run_script)
        labelFile = Label(canvas.master, text=self.scriptname, bg="#fff")
        self.labelError = Label(canvas.master, text="", bg="#fff",fg="#C10000")
        self.labelInfo = Label(canvas.master, text="", bg="#fff",fg="#000",font=("Arial", 8))
        
        buttonOpen.place(x=5, y=5)
        buttonEdit.place(x=75, y=5)
        buttonRun.place(x=145, y=5)
        labelFile.place(x=215,y=15)
        
        self.labelError.place(x=7,y=50)
        self.labelInfo.place(x=7,y=80)
        

    def reset(self):
        self.labelError.config(text="")
        
    def print_error(self,error,filename):
        exc_type, ex, tb = sys.exc_info()
        imported_tb_info = traceback.extract_tb(tb)[-1]
        line_number = imported_tb_info[1]
        print_format = 'ERROR en {} línea {}: {}'
        self.labelError.config(text=print_format.format(filename,line_number, ex))

    def run_script(self):
        world.reset()
        gui.reset()
        
        try:
            exec(open(self.worldpath).read())
        except Exception as error:
            self.print_error(error,self.worldname)
            return
        
        try:
            exec(open(self.scriptpath).read())
        except Exception as error:
            self.print_error(error,self.scriptname)
            
        
    def open_script(self):
        filepath = filedialog.askopenfilename()
        script.setFile(filepath)

    def edit_script(self):
        os.system("gedit "+script.filepath+" &")

    def show_info(self):
        s=world.info()
        self.labelInfo.config(text=s)
        self.screen.ontimer(self.show_info,100)

    def show_collisions(self):
        s=world.detect_collisions()
        self.labelError.config(text=s)
        self.screen.ontimer(self.show_collisions,50)
        

    
def handler(signum, frame):
    print ("Cierra la ventana para cerrar la aplicación")




world=World()
gui=GUI()


if __name__=='__main__':

    signal.signal(signal.SIGINT, handler)
    gui.screen.onkey(gui.run_script,'F5')

    gui.show_info()

    gui.show_collisions()
    
    gui.run_script()

    #gui.collisions()

    
    gui.screen.listen()
    gui.screen.mainloop()

