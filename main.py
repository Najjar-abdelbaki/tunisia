import turtle
import pandas
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

data = pandas.read_csv(resource_path("governorates.csv"))
states = data["governorates"].to_list()
screen = turtle.Screen()
screen.title("ولايات البلاد التونسية")
# screen.setup(width=600, height=800)
screen.addshape(resource_path("tunisie19_resized.gif"))
turtle.shape(resource_path("tunisie19_resized.gif"))

guss_gov =[]

while len(guss_gov) < 24:

    answer = screen.textinput(f"{len(guss_gov)}/50 ولاية صحيحة", "اكتب اسم ولاية اخرى")
    answer = answer.strip()

    if answer == "غادر":
        missing_states = [state for state in states if state not in guss_gov]

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing.txt")
        break

    if answer in states:
        x = data[data.governorates == answer]

        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(int(x.x), int(x.y))
        tim.color("red")
        tim.write(answer, font=("Arial", 14, "normal"), align="center")
        guss_gov.append(answer)
