import turtle



# def cal_intersection(a1,b1,a2,b2):
#     try:
#         x = (b2-b1)/(a1-a2)
#         y = a1*(b2-b1)/(a1-a2) + b1
#         return (x,y)
#     except Exception as e:
#         print(str(e))
#         return None


def isCollision2(t1, t2):
        if abs (t1.xcor () - t2.xcor ()) < 20 :
            a = t1.ycor ()
            b = t2.ycor ()
            if a < b and a > b - 400 :
                return True
        else:
            return False


def isCollision(t1,t2):
    if t1.distance(t2) < 10:
        return True
    else:
        return False
        
        
class Hero (turtle.Turtle): 
    def __init__(self,x,y):
        super(Hero,self).__init__( )
        self.pu()
        self.goto(x,y)
        self.pd()

        
class Area (turtle.Turtle):
    def __init__(self,x,y):
        super(Area,self).__init__()
        self.x=x
        self.y=y
        self.shape("square")
        self.pu()
        
    def draw(self):
        self.goto(self.x, self.y)
        

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



def main():

    area1=Area(40,40)
    area1.draw()
    
    hero = Hero(40,40)
    hero.fd(20)

    print (isCollision(hero,area1))


    turtle.mainloop()    

if __name__ == '__main__':
    main()
