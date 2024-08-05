# OKOLI CHISOM DANIEL
# 2020/245178
# COMPUTER SCIENCE
# COS 435

import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Translated Triangle")

# Create a turtle
tri = turtle.Turtle()

# Draw the original triangle
tri.penup()
tri.goto(0, 0)
tri.pendown()
tri.goto(100, 0)
tri.goto(50, 87)
tri.goto(0, 0)

# Translate the triangle by moving the turtle
tri.penup()
tri.goto(100, 100)  # Translation vector (100, 100)
tri.pendown()

# Draw the translated triangle
tri.goto(200, 100)
tri.goto(150, 187)
tri.goto(100, 100)

turtle.done()
