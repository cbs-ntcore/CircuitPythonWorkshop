import board
import digitalio
import neopixel

import time


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


# start trial count at 0
trial_count = 0

# set led color to pure red
set_color(255, 0, 0)

# run trials
while True:
    # turn on light
    set_brightness(1.0)

    # record starting time
    start_time = time.monotonic()

    # wait for the button to be pressed
    while not is_button_pressed():
        # do nothing if the button is not pressed
        pass

    # record time end time (when button was pressed)
    end_time = time.monotonic()

    # turn off light
    set_brightness(0.0)

    # compute time between light onset and button press
    reaction_time = end_time - start_time

    # report reaction time as comma separated text
    print("%s,%s" % (trial_count, reaction_time))

    # increment trial count
    trial_count += 1

    # wait a short time between trials
    time.sleep(5)
