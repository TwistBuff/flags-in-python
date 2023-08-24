from turtle import *

def france():
    for i in range(2):
        forward(270)
        right(90)
        forward(270/2)
        right(90)
    
    fillcolor("blue")
    begin_fill()
    
    for i in range(2):
        forward(270/3)
        right(90)
        forward(270/2)
        right(90)
    
    
    end_fill()

    forward(270)

    fillcolor("red")
    begin_fill()

    for i in range(2):
        right(90)
        forward(270/2)
        right(90)
        forward(270/3)
    
    end_fill()



    done() 


france()