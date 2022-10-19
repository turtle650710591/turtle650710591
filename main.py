"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

t = turtle.Turtle()

for c in ['red','red','red','red','red','red','red','red']:
    t.color(c)
    t.forward(90)
    t.left(45)

for i in range(0,8):
  t.right(45)
  for c in ['red','red','red','red','red','red','red','red']:
      t.color(c)
      t.forward(90)
      t.left(45)


t.circle9