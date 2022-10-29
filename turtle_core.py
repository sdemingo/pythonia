
from turtle import *
from tkinter import Button,Label,filedialog
import os
import sys
import signal
import traceback

hero=Turtle()
titles=Turtle()

HEIGHT=500
WIDTH=500

main_script="main.py"

ui=None

def reload_script():
    hero.reset()
    ui.reset()
    try:
        exec(open('main.py').read())
    except Exception as error:
        #print (str(error))
        ui.print_error(error)

def open_script():
    filename = filedialog.askopenfilename()
    print ("Quieres abrir el fichero "+str(filename))

def edit_script():
    os.system("gedit "+main_script+" &")


class GUI:
    def __init__(self,scr):
        self.screen=scr
        scr.title("Pythonia 0.1")
        canvas = scr.getcanvas()
        canvas.master.minsize(WIDTH,HEIGHT)
        
        self.filename_script=os.path.basename(main_script)
        buttonOpen = Button(canvas.master, text="Open", height=1, width=5,  command=open_script)
        buttonEdit = Button(canvas.master, text="Edit", height=1, width=5, command=edit_script)
        buttonRun = Button(canvas.master, text="Run", height=1, width=5, command=reload_script)
        labelFile = Label(canvas.master, text=self.filename_script, bg="#fff")
        self.labelError = Label(canvas.master, text="", bg="#fff",fg="#C10000")

        buttonOpen.place(x=5, y=5)
        buttonEdit.place(x=75, y=5)
        buttonRun.place(x=145, y=5)
        labelFile.place(x=215,y=10)
        self.labelError.place(x=7,y=50)

        self.screen.onkey(reload_script,'F5')

    def reset(self):
        self.labelError.config(text="")
        
    def print_error(self,error):
        exc_type, ex, tb = sys.exc_info()
        imported_tb_info = traceback.extract_tb(tb)[-1]
        line_number = imported_tb_info[1]
        print_format = 'ERROR en línea {}: {}'
        self.labelError.config(text=print_format.format(line_number, ex))


    
def handler(signum, frame):
    print ("Cierra la ventana para cerrar la aplicación")


if __name__=='__main__':

    wn = Screen()
    setup(WIDTH, HEIGHT,0,0)
    ui=GUI(wn)

    reload_script()
    
    signal.signal(signal.SIGINT, handler)
    try:
        wn.listen()
        wn.mainloop()
    except KeyboarInterrupt as err:
        print (err)

