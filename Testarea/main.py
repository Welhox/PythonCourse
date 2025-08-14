
# import turtle
# timmy = turtle.Turtle()
# my_screen = turtle.Screen()

# from turtle import Turtle, Screen
# tommy = Turtle()
#
# tommy.shape("turtle")
# tommy.color("CadetBlue3")
# tommy.forward(100)
#
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l'
print(table)

