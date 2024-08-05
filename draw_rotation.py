import turtle
import math # import math module

def rotate_point(x, y, angle):
    """Rotate a point around the origin (0, 0) by angle in degrees."""
    rad = math.radians(angle)
    x_new = x * math.cos(rad) - y * math.sin(rad)
    y_new = x * math.sin(rad) + y * math.cos(rad)
    return x_new, y_new

# Original triangle vertices
vertices = [(0, 0), (100, 0), (50, 87)]

# Rotation angle
angle = 30

# Rotate each vertex
rotated_vertices = [rotate_point(x, y, angle) for x, y in vertices]

# Set up the screen
screen = turtle.Screen()
screen.title("Rotated Triangle")

# Create a turtle
tri = turtle.Turtle()

# Draw the original triangle
tri.penup()
tri.goto(vertices[0])
tri.pendown()
for vertex in vertices[1:]:
    tri.goto(vertex)
tri.goto(vertices[0])

# Draw the rotated triangle
tri.penup()
tri.goto(rotated_vertices[0])
tri.pendown()
for vertex in rotated_vertices[1:]:
    tri.goto(vertex)
tri.goto(rotated_vertices[0])

# Finish
turtle.done()

# OKOLI CHISOM DANIEL
# 2020/245178
# COMPUTER SCIENCE
# COS 435