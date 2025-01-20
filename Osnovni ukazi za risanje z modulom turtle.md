# turtle
turtle je Pythonov modul za želvjo grafiko. Na začetku programa uvozimo modul z ukazom:
```
from turtle import *
```

# Primer programa
```
from turtle import *

fillcolor("yellow")
begin_fill()
pencolor("red")
for i in range(4):
    forward(100)
    right(90)

end_fill()

exitonclick()
```

## Najpogostejši ukazi
```
from turtle import *	# iz modula turtle uvozimo vse ukaze za risanje z želvjo grafiko
fd(d) ali forward(d)	# želva se premakne naprej za podano vrednost d
bk(d) ali backward(d) 	# želva se premakne nazaj za podano vrednost d
right(kot)		# želva se za obrne v desno smer za določen kot (na mestu)
left(kot)		# želva se za podano vrednost kota obrne v levo
up()			# želva dvigne svoje pero, ne pušča sled
down()			# želva spusti pero na platno in pušča sled
width(d)		# nastavitev debeline peresa
color(imebarve)		# spremeni se barva črnila v peresu
fillcolor(barva)	# določimo barvo notranjosti lika
begin_fill()		# začetek barvanja notranjosti lika
end_fill()		# zaključek barvanja notranjosti
goto(x, y)		# premik želve na koordinate x, y
setheading(90)		# nastavitev smeri želve (0=vzhod, 90=sever, 180=zahod, 270=jug)
```