import turtle
a = turtle.Screen()
turtle.speed(10)
for i in range(20):
    turtle.circle(10*i)
    turtle.circle(-10*i)
    turtle.left(i)
turtle.exitonclick()
