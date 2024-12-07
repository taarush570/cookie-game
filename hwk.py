import pgzrun
import random

WIDTH= 450
HEIGHT= 500
TITLE= ("Cookie clicker")

#variable to store the messages getting displayed on the screen
message=""


#getting the picture and making it a sprite
#Actor function for it

cookie = Actor("cookie")

def draw():
    screen.clear() #This clears the screen if anything is placed on the screen before
    #screen is a default variable

    #adding background colour for the screen
    screen.fill(color=(65,225,10))

    #adding picture on the screen which has been taken already in a vairable name
    cookie.draw()

    #adding text in the screen
    screen.draw.text(message, center= (400,30), fontsize=40)


def place_cookie(): #this functiom is to give random positions for the alien
    cookie.x = random.randint(0,WIDTH)
    cookie.y = random.randint(0,HEIGHT)


def on_mouse_down(pos):
    global message #global means making the variable global so that changes are reflected all over the code and not limited to only this function
    if cookie.collidepoint(pos):
        message="Good Job!"
        place_cookie()
    else:
        message="Oh no, you missed!"
    
place_cookie()
pgzrun.go()