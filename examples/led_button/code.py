import board
import digitalio
import neopixel


# the following globals and functions could be included as a module

# make an object to control the NEOPIXEL, multi-color LED
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)

# configure the button pin (digital pin 5, D5)
button = digitalio.DigitalInOut(board.D5)

# define button pin as an input
button.direction = digitalio.Direction.INPUT

# add a 'pull up' to set the default value of this pin to True
button.pull = digitalio.Pull.UP


def set_brightness(value):
    # set the LED brightness to a value from 0 to 1
    pixel.brightness = value


def set_color(red, green, blue):
    # set the LED color by defining the red, green and blue
    # components using values from 0 to 255
    # (255, 0, 0) will be red
    # (0, 255, 0) will be green
    # (255, 255, 0) will be yellow
    # (255, 255, 255) will be white
    pixel.fill((red, green, blue))


def is_button_pressed():
    # the pin was configured with a 'pull up' so it's default value is True
    # pressing the button connects the button pin to ground and changes
    # the value to False
    # this function should return True when the button is pressed so we need
    # to invert the value
    return not button.value

# set the pixel color to red
set_color(255, 0, 0)

# run this code forever (until powered down)
while True:
    # if the button is pressed..
    if is_button_pressed():
        # turn on the light, LED, to full brightness
        set_brightness(1.0)
    else:
        # else, turn off the LED
        set_brightness(0.0)
