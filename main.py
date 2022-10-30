import turtle
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(10000)
turtle.shape("turtle")
contador = 1
while contador <=2:
		for i in range(12):
			for colors in["red","magenta","blue","orange","white"]:
				turtle.color(colors)
				turtle.right(10)
				turtle.fd(10)
				turtle.left(4)
				turtle.stamp()
		for i in range(12):
			for colors in ["red","magenta","blue","orange","white"]:
				turtle.color(colors)
				turtle.left(10)
				turtle.fd(10)
				turtle.right(4)
				turtle.stamp()
		for i in range(12):
			for colors in ["red","magenta","blue","orange","white"]:
				turtle.color(colors)
				turtle.right(10)
				turtle.fd(15)
				turtle.left(4)
				turtle.stamp()
			
		for i in range(12):
			for colors in ["red","magenta","blue","orange","white"]:
				turtle.color(colors)
				turtle.left(10)
				turtle.fd(12)
				turtle.right(4)
				turtle.stamp()
			
turtle.hideturtle()