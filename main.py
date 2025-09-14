import time, gc
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_RGB332
from pimoroni import RGBLED
from machine import Pin

#configure display
display = PicoGraphics(DISPLAY_PICO_DISPLAY_2, pen_type= PEN_RGB332, rotate=0)
display.set_backlight(0.5)

#configure buttons
but_a = Pin(12, Pin.IN, Pin.PULL_UP)
but_b = Pin(13, Pin.IN, Pin.PULL_UP)
but_x = Pin(14, Pin.IN, Pin.PULL_UP)
but_y = Pin(15, Pin.IN, Pin.PULL_UP)


#get display sizes 
WIDTH, HEIGHT = display.get_bounds()

#colour constants
BLACK = display.create_pen(0, 0, 0)
WHITE = display.create_pen(255, 255, 255)
RED = display.create_pen(255, 0, 0)
GREEN = display.create_pen(0, 255, 0 )
BLUE = display.create_pen(0,0,255)

led = RGBLED(6,7,8)
led.set_rgb(0,0,0)

def clear():
    display.set_pen(black)
    led.set_rgb(0,0,0)
    display.clear()
    display.update()


def  button_input_handler(menu):
    #handles button presses will eventually take the state of the program into account but for now just
    #works with the Menu
    if but_y.value()==0:
        if menu.selected < (len(menu.items)-1):
            menu.selected += 1
        else:
            menu.selected = 0 #loops round to first menu item
    
    if but_x.value()==0:
        if menu.selected > 0:
            menu.selected -= 1
        else:
            menu.selected = len(menu.items) -1
    menu.draw_menu()
#wifi setup

#github fetcher

#weather fetcher

#clock

#menu class
class Menu:
    def __init__(self, itemList):
        self.items = itemList
        self.selected = 0
        self.cursor = '>'
        self.colour = "WHITE"
        
    def draw_menu(self):
        display.set_pen(BLACK)
        display.clear()
        display.set_pen(WHITE)
        
        line = 10
        for i in range(len(self.items)):
            menuItem = self.items[i]
            if i == self.selected:
                menuItem = self.cursor + menuItem
            display.text(menuItem, 80, line)
            line += 20
        display.update()

mainMenu = ["github", "weather", "clock"]
menu = Menu(mainMenu)

#setup
menu.draw_menu()

#main loop
while True:
    button_input_handler(menu)
    time.sleep(0.1)