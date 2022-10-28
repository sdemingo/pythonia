
from turtle import *
from tkinter import Button,filedialog
import os
import signal

hero=Turtle()
titles=Turtle()

HEIGHT=500
WIDTH=500

main_script="main.py"

def reload_script():
    hero.reset()
    # titles.reset()
    # titles.hideturtle()
    # titles.penup()
    # titles.goto(-280,280)
    # titles.write("Pulsa F5 para actualizar", move=False, align="left")
    exec(open('main.py').read())


def open_script():
    filename = filedialog.askopenfilename()
    print ("Quieres abrir el fichero "+str(filename))



def edit_script():
    os.system("gedit "+main_script+" &")

    
def build_ui(screen):
    screen.title("Pythonia 0.1")
    canvas = screen.getcanvas()

    buttonOpen = Button(canvas.master, text="Open", height=1, width=5,  command=open_script)
    buttonEdit = Button(canvas.master, text="Edit", height=1, width=5, command=edit_script)
    buttonRun = Button(canvas.master, text="Run", height=1, width=5, command=reload_script)
    
    buttonOpen.place(x=5, y=5)
    buttonEdit.place(x=75, y=5)
    buttonRun.place(x=145, y=5)

    screen.onkey(reload_script,'F5')


    
def handler(signum, frame):
    print ("Cierra la ventana para cerrar la aplicación")


if __name__=='__main__':

    wn = Screen()
    setup(WIDTH, HEIGHT,0,0)
    build_ui(wn)

    reload_script()
    
    signal.signal(signal.SIGINT, handler)
    try:
        wn.listen()
        wn.mainloop()
    except KeyboarInterrupt as err:
        print (err)

