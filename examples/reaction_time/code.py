import board
import digitalio
import neopixel

import time


# see the led_button code for descriptions about setting up pins
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
button = digitalio.DigitalInOut(board.D5)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# start trial count at 0
trial_count = 0

# set led color to pure red
pixel.fill((255, 0, 0))

# run trials
while True:
    # turn on light
    pixel.brightness = 1.0

    # record starting time
    start_time = time.monotonic()

    # wait for the button to be pressed (button.value == False when pressed)
    while button.value:
        # do nothing if the button is not pressed
        pass

    # record time end time (when button was pressed)
    end_time = time.monotonic()

    # turn off light
    pixel.brightness = 0.0

    # compute time between light onset and button press
    reaction_time = end_time - start_time

    # report reaction time as comma separated text
    print("%s,%s" % (trial_count, reaction_time))

    # increment trial count
    trial_count += 1

    # wait a short time between trials
    time.sleep(5)
