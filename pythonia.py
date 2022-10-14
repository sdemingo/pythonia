import turtle



def cal_intersection(a1,b1,a2,b2):
    try:
        x = (b2-b1)/(a1-a2)
        y = a1*(b2-b1)/(a1-a2) + b1
        return (x,y)
    except Exception as e:
        print(str(e))
        return None


class Hero (turtle.Turtle): 
    def __init__(self,x,y):
        super(Hero,self).__init__(  )
        self.pu()
        self.goto(x,y)
        self.pd()


class Wall:
    def __init__(self,x0,y0,x1,y1):
        self.x0=x0
        self.y0=y0
        self.x1=x1
        self.y1=y1
        self.wall=turtle.Turtle()

    def draw(self):
        self.wall.hideturtle()
        self.wall.speed(20)
        self.wall.pu()
        self.wall.color("red")
        self.wall.setpos(self.x0,self.y0)
        self.wall.pd()
        self.wall.goto(self.x1,self.y1)


wall1=Wall(100,-50,100,200)
wall1.draw()



hero = Hero(10,100)
hero.fd(150)




turtle.mainloop()