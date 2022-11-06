# Ejemplo de mundo para pythonia


    
zona1 = Agent("zona1",-150,40,5)
world.add(zona1)


zona1.do(zona1.fd,20)
zona1.do(zona1.rt,180)
zona1.do(zona1.fd,20)
zona1.do(zona1.goto,5,5)
       

zona2 = Agent("zona2",50,38,radius=3)
world.add(zona2)



world.procAgentsPrograms()


