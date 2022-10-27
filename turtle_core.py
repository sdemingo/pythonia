
from turtle import *
import os
import signal

hero=Turtle()
titles=Turtle()

def reload_script():
    hero.reset()
    titles.reset()

    titles.hideturtle()
    titles.penup()
    titles.goto(-280,280)
    titles.write("Pulsa F5 para actualizar", move=False, align="left")
    
    
    exec(open('main.py').read())


def handler(signum, frame):
    print ("Cierra la ventana para cerrar la aplicación")


def run_editor():
    os.system("gedit main.py &")
    

if __name__=='__main__':

    
    wn = Screen()
    setup(600, 600,0,0)

    reload_script()
    # run_editor()

    wn.onkey(reload_script,'F5')

    signal.signal(signal.SIGINT, handler)
    try:
        wn.listen()
        wn.mainloop()
    except KeyboarInterrupt as err:
        print (err)

