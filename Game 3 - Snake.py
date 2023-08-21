from tkinter import *
import random

#Key game metrics here
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = ("Green")
FOOD_COLOR = ("Red")
BACKGROUND_COLOR = ("Black")


class Snake:
    pass

class Food:

    def __init__(self):
        #Deciding where to place the food in the game space.
        #We're dividing the height and/or weight by the size of the spaces.
        x = random.randint(0,(GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        x = random.randint(0,(GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x,y]

        #CREATING FOOD
        #select oval shape, determine size, color and tag of the food.
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")
def next_turn():
    pass

def change_direction(new_direction):
    pass

def check_collisions():
    pass

def game_over ():
    pass

#Window information
window = Tk()
window.title("Snek gehm")
window.resizable(False, False)

#Score information
score = 0
direction = "down"
label = Label(window, text="Score:{}".format(score), font=('consolas',40))
label.pack()

#Importing game colors and sizes
canvas = Canvas (window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

#Centralise the screen
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
window.geometry (f"{window_width}x{window_height}+{x}+{y}")

snake = Snake()
food = Food()

window.mainloop()