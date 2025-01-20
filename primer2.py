from turtle import *
speed(100)                  # hitreje riše
pencolor("blue")
pensize(3)
for i in range(36):         # ponovi 36 krat primer1 brez barvanja
    for i in range(4):
        forward(100)
        right(90)
    
    lt(10)                  # obrni levo za 10 stopinj

exitonclick()
