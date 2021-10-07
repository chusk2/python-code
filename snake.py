from turtle import Turtle, Screen

src = Screen()
src.setup(height=600, width=600)
src.bgcolor('black')
src.title('Snake Game')

snakes = [Turtle() for i in range(3)]
for i in range(3):
	snake = snakes[i]
	snake.shape("square")
	snake.color('white')
	snake.pensize(1)
	snake.shapesize(2,2)
	snake.setpos(280,0)



src.exitonclick()