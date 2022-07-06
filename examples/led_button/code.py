# import a few modules to control the specialized hardware
import board
import digitalio
import neopixel


# setup the 3 color LED (neopixel)
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)

# set the LED color by defining the red, green and blue
# components using values from 0 to 255
# (255, 0, 0) will be red
# (0, 255, 0) will be green
# (255, 255, 0) will be yellow
# (255, 255, 255) will be white
pixel.fill((255, 0, 0))

# configure the button pin (digital pin 5, D5)
button = digitalio.DigitalInOut(board.D5)

# define button pin as an input
button.direction = digitalio.Direction.INPUT

# add a 'pull up' to set the default value of this pin to True
button.pull = digitalio.Pull.UP

# run this code forever (until powered down)
while True:
    # if the button is pressed..
    # the button was configured with a 'pull up' so it's default value is True
    # pressing the button connects the button pin to ground and changes
    # the value to False
    if not button.value:
        # set the LED brightness to a value from 0 to 1
        pixel.brightness = 1.0
    else:
        # else, turn off the LED by setting brightness to 0
        pixel.brightness = 0.0
