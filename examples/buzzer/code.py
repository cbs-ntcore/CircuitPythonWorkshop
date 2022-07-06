# import a few modules to control the specialized hardware
import board
import digitalio
import pwmio


# see the led_button code for descriptions about setting up pins
button = digitalio.DigitalInOut(board.D5)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# configure digital pin 10 to drive the buzzer
buzzer = pwmio.PWMOut(board.D10, variable_frequency=True)
# at a frequency of 440 hertz
buzzer.frequency = 440

# the buzzer is driven with a PWM (pulse width modulation) signal
# this signal is a square wave with varying pulse width
# for driving the buzzer we want to use a 50% duty cycle PWM
# signal which means the digital pin is high 50% of the time
# CircuitPython uses a number between 0 and 2 ** 16 to set the duty
# cycle so 2 ** 15 is 50% and will generate a square wave that is
# high 50% of the time
# to make this easier to use we'll define some variables to store
# the duty cycle values for ON and OFF
ON = 2 ** 15
OFF = 0

# run this code forever (until powered down)
while True:
    # if the button is pressed..
    if not button.value:
        # turn on the buzzer
        buzzer.duty_cycle = ON
    else:
        # turn off the buzzer
        buzzer.duty_cycle = OFF
