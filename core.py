
from turtle import *
from tkinter import *
import os
import sys
import signal
import traceback
import threading

HEIGHT=500
WIDTH=500

class Agent(Turtle):
    def __init__(self,name):
        Turtle.__init__(self)
        self.name=name
        self.counter=0
        self.speed(1)
        self.color("#000")
        self.onrelease(self.release_mouse_click)
        self.onclick(self.press_mouse_click)

    def release_mouse_click(self,btn,add):
        self.color("#000")

    def press_mouse_click(self,btn,add):
        self.color("#C10000")
        gui.print_console(self.info())

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

    def getAllAgents():
        return self.agents.values()

    def getAgentInPosition(self,x,y):
        for agent in self.agents.values():
            if ((abs(agent.xcor()-x)<10) and (abs(agent.ycor()-y)<10)):
                return agent
        return None

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
        
        self.console=[]
        self.running=False
        
        self.screen=wn
        self.screen.title("Pythonia 0.1")
        canvas = self.screen.getcanvas()
        canvas.master.minsize(WIDTH,HEIGHT)
        
        buttonOpen = Button(canvas.master, text="Open", height=1, width=5,
                            command=self.open_script)
        buttonEdit = Button(canvas.master, text="Edit", height=1, width=5,
                            command=self.edit_script)
        buttonRun = Button(canvas.master, text="Run", height=1, width=5,
                           command=self.run_script)
        labelFile = Label(canvas.master, text=self.scriptname, bg="#fff")
        self.labelError = Label(canvas.master, text="", bg="#fff",fg="#C10000")
        self.consoleText = Text(canvas.master,width=30,height=5,
                              font=("Arial",8),bd=0,highlightthickness = 0,
                              borderwidth=0)
        self.consoleText.config(spacing1=3)
        
        buttonOpen.place(x=5, y=5)
        buttonEdit.place(x=75, y=5)
        buttonRun.place(x=145, y=5)
        labelFile.place(x=215,y=15)
        
        self.labelError.place(x=7,y=50)
        self.consoleText.place(x=7,y=80)
        

    def reset(self):
        self.labelError.config(text="")
        
    def print_error(self,error,filename):
        exc_type, ex, tb = sys.exc_info()
        imported_tb_info = traceback.extract_tb(tb)[-1]
        line_number = imported_tb_info[1]
        print_format = 'ERROR en {} línea {}: {}'
        self.labelError.config(text=print_format.format(filename,line_number, ex))

    def run_script(self):
        if self.running:
            return
        
        self.running=True
        world.reset()
        self.reset()
        self.show_collisions()
        
        try:
            exec(open(self.worldpath).read())
        except Exception as error:
            self.print_error(error,self.worldname)
            self.running=False
            return
        
        try:
            exec(open(self.scriptpath).read())
        except Exception as error:
            self.print_error(error,self.scriptname)

        self.running=False
            
        
    def open_script(self):
        filepath = filedialog.askopenfilename()
        script.setFile(filepath)

    def edit_script(self):
        os.system("gedit "+script.filepath+" &")

    def print_console(self,text):
        if (len(self.console)>5):
            self.console=self.console[:5]
        self.console.insert(0,text)
        self.consoleText.delete('1.0',END)
        for l in self.console:
            self.consoleText.insert(INSERT,l)
        
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

    gui.run_script()
    
    gui.screen.listen()
    gui.screen.mainloop()

