# imports
from guizero import App, Drawing, Combo, Slider, PushButton, Text

# functions

def save():
    app.select_file(save=True)

def start(event):
    painting.last_event = event
    
def draw(event):
    painting.line(
        painting.last_event.x, painting.last_event.y,
        event.x, event.y,
        color=color.value,
        width=width.value
        )
    
    painting.last_event = event

# ...definding? dont know maby unsure
app = App("paint", width="200", height="200")
app.bg =  (251, 251, 208)

painting = Drawing(app, width="128", height="128")
painting.bg = "blue"

color = Combo(app, options=["#7fb238", "#f7dfa3", "#c7c7c7", "#ff0000", "#a0a0ff", "#a7a7a7", "#00ff00", "#ffffff", "#a4a8b8", "#976d4d", "#707070", "#4040ff", "#8f7748", "#fffff5", "#d880033", "#b24cd8", "#b24cd8", "#6699d8", "#e5e533", "#7ecc19", "#f27fa5", "#4c4c4c", "#999999", "#4c7f99", "#7e3fb2", "#334cb2", "#664c33", "#667f33", "#993333", "#191919", "#faee4d", "#5cdbd5", "#4a80ff", "#0080ff", "#815631", "#7a0200", "#d1b1a1", "#9f5124", "#95576c", "#706c8a", "#ba7424", "#677535", "#a04d4e", "#392923", "#876b62", "#575c5c", "#7a4958", "#4c3e5c", "#4c3223", "#4c522a", "#8e3c2e", "#251610", "#bd3030", "#943f61", "#5c191d", "#167f86", "#3a8e8d", "#562c3e", "#14b484"])
color.bg = "gray"

width = Slider(app, start=1, end=10)
width.bg = "lightgray"

painting.when_left_button_pressed = start
painting.when_mouse_dragged = draw

button = PushButton(app, save, text="save")
file_name = Text(app)

# this displays the window (app) in line 15
app.display()