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

#wifi setup

#github fetcher

#weather fetcher

#clock


#menu class 