import time
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_RGB332
from pimoroni import RGBLED
from machine import Pin

#wifi imports
import network
import socket
import rp2
import ntptime

#api call imports
import requests

#local file import
import secrets
import weather_api

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
    display.set_pen(BLACK)
    led.set_rgb(0,0,0)
    display.clear()
    display.update()
    

"""
Calculates the width of the  display then splits strings to fit on them by
inserting newline escape characters
"""


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
            
    if but_a.value() ==0:
        print(menu.selected)
        if menu.selected == 0:
            pass
        elif menu.selected == 1:
            weather_con_message = 'Connecting to weather api please wait'
            menu.clear_display()
            display.text(weather_con_message, 0, 10)
            display.update()
            time.sleep(5)
            weather = Page(weather_api.parse_weather_api_response(weather_api.weather_api_call()))
            
        elif menu.selected == 2:
            open_clock()
    
    if but_b.value== 0:
        pass
    menu.draw_menu()
    
    
#wifi setup
ssid = secrets.SSID
wifi_password = secrets.PASSWORD
rp2.country('GB')


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, wifi_password)
    
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        print('connected')
        break
    max_wait -= 1
    print("awaiting connection")
    time.sleep(1)




#github fetcher
def get_github_chart():
    pass

#clock
def open_clock():
    active = 1
    while active:
        now = time.localtime()
        h, m = now[3], now[4]
        time_string = f"{h}:{m}"
        display.set_pen(BLACK)
        display.clear()
        display.set_pen(WHITE)
        display.text(time_string, 10, 5, 200, 10)
        display.update()
        if but_b.value() == 0:
            active = 0

#menu class
class Menu:
    def __init__(self, itemList):
        self.items = itemList
        self.selected = 0
        self.cursor = '>'
        self.colour = "WHITE"
        
    def clear_display(self):
        display.set_pen(BLACK)
        display.clear()
        display.set_pen(WHITE)
        
        
    def draw_menu(self):
        self.clear_display()
        line = 10
        for i in range(len(self.items)):
            menuItem = self.items[i]
            if i == self.selected:
                menuItem = self.cursor + menuItem
            display.text(menuItem, 80, line)
            line += 20
        display.update()


class Page:
    def __init__(self, content):
        self.colour = 'WHITE'
        self.escape_but = 'B'
        self.content = content
    
    
    def draw_page(content):
        display.set_pen(BLACK)
        display.clear()
        display.set_pen(WHITE)
        
        line = 10
        for i in range(len(self.content)):
            item = self.items[i]
            if item[0] == '|':
                pass #handle image
            else:
                display.text(item, 80, line)
                line += 20
        display.update()
        
        
        
mainMenu = ["github", "weather", "clock"]
menu = Menu(mainMenu)


#setup
menu.draw_menu()

#weather_api.parse_weather_api_response(weather_api.weather_api_call())

#main loop
while True:
    button_input_handler(menu)
    time.sleep(0.1)
    