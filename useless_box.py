#
#
# Project: Useless Box CircuitPython Code
#
# Written By: Daniel Yu
# Date: June 8, 2023
# Edited: June 25, 2023
# Planned By: Connor Dawson, Jared Steier, Raina Owen, Daniel Yu
#
# Tesla – Useless Box Project
# Sci-Fi Science Camps 2023
#
#

# Basic library imports
import board, time, digitalio, pwmio, random

# Importing motor and audio libraries
from adafruit_motor import servo

# Initializing the random integer
rand_int = 1

# Setting input output for button
button = digitalio.DigitalInOut(board.GP13)
button.switch_to_input(pull = digitalio.Pull.DOWN)

# Setting input output for LEDs
led_one = digitalio.DigitalInOut(board.GP14)
led_one.direction = digitalio.Direction.OUTPUT
led_two = digitalio.DigitalInOut(board.GP15)
led_two.direction = digitalio.Direction.OUTPUT
led_three = digitalio.DigitalInOut(board.GP16)
led_three.direction = digitalio.Direction.OUTPUT

# Create PWMOut objects on Pin GP0 and GP1
pwm_lid = pwmio.PWMOut(board.GP0, duty_cycle = 2 ** 15, frequency = 50)
pwm_arm = pwmio.PWMOut(board.GP1, duty_cycle = 2 ** 15, frequency = 50)

# Create servo motor objects
lid = servo.Servo(pwm_lid)
arm = servo.Servo(pwm_arm)

# Various LED lighting effects determined by the given integer parameter
def lighting(effect):
    
    # Effect 1: Quick flashing
    if effect == 1:
        for i in range(8):
            led_one.value = True
            led_two.value = True
            led_three.value = True
            time.sleep(0.05)
            led_one.value = False
            led_two.value = False
            led_three.value = False
            time.sleep(0.05)
    
    # Effect 2: Slow blinking
    elif effect == 2:
        for i in range(5):
            led_one.value = True
            led_two.value = True
            led_three.value = True
            time.sleep(0.1)
            led_one.value = False
            led_two.value = False
            led_three.value = False
            time.sleep(0.1)
    
    # Fast rotating flashes
    elif effect == 3:
        for i in range(5):
            led_one.value = True
            led_two.value = False
            led_three.value = False
            time.sleep(0.05)
            led_one.value = False
            led_two.value = True
            led_three.value = False
            time.sleep(0.05)
            led_one.value = False
            led_two.value = False
            led_three.value = True
            time.sleep(0.05)
    
    # Fast dual rotating flashes
    elif effect == 4:
        for i in range(5):
            led_one.value = True
            led_two.value = True
            led_three.value = False
            time.sleep(0.08)
            led_one.value = False
            led_two.value = True
            led_three.value = True
            time.sleep(0.08)
            led_one.value = True
            led_two.value = False
            led_three.value = True
            time.sleep(0.08)
    
    # Keeps all LEDs on when closing the lid
    led_one.value = True
    led_two.value = True
    led_three.value = True
    
# Main movement
def movements(num):
    # Turns on all LEDs when lid opens
    led_one.value = True
    led_two.value = True
    led_three.value = True
    
    # ---------- Movement 1: Regular Movement ---------- #
    if num == 1:
        lid.angle = 60
        time.sleep(1) # Wait 1 second
        arm.angle = 180
    # --------------- End of Movement 1 --------------- #
    
    
    
    
    # ---------- Movement 2: Fast Lid & Arm ---------- #
    elif num == 2:
        lid.angle = 60
        arm.angle = 180
    # --------------- End of Movement 2 --------------- #
    
    
    
    
    # ---------- Movement 3: Lighting Show ---------- #
    elif num == 3:
        lid.angle = 60
        lighting(random.randint(1, 4)) # Calls for a light show
        time.sleep(0.05)
        arm.angle = 180
    # --------------- End of Movement 3 --------------- #
    
    
    
    
    # ---------- Movement 4: Annoyed & Petty ---------- #
    elif num == 4:
        lid.angle = 90
        time.sleep(0.5)
        lid.angle = 180
        time.sleep(1)
        lid.angle = 30
        time.sleep(0.5)
        lid.angle = 180
        time.sleep(3)
        arm.angle = 180
        time.sleep(2)
        arm.angle = 90
        time.sleep(0.5)
        arm.angle = 150
    # --------------- End of Movement 4 --------------- #
    
    
    
    
    # ---------- Movement 5: Throwing A Fit ---------- #
    elif num == 5:
        for i in range(2):
            for j in range(3):
                lid.angle = 30
                time.sleep(0.2)
                lid.angle = 180
                time.sleep(0.2)
            for k in range(5):
                lid.angle = 30
                time.sleep(0.1)
                lid.angle = 180
                time.sleep(0.1)
        
        lid.angle = 30
        lighting(random.randint(1, 4))
        
        for x in range(3):
            arm.angle = 150
            time.sleep(0.25)
            arm.angle = 0
            time.sleep(0.25)
        
        arm.angle = 0
        lighting(random.randint(1, 4))
        arm.angle = 180
        time.sleep(0.5)
        arm.angle = 0
        # --------------- End of Movement 5 --------------- #
        
# All closing animations function
def exit_movement(num):
    
    # Lid closing animation for Movements 1
    if num == 1:
        arm.angle = 0
        time.sleep(1)
        lid.angle = 180
    
    # Lid closing animation for Movements 2, 3, & 5
    elif num == 2 or num == 3 or num == 5:
        arm.angle = 0
        time.sleep(0.2)
        lid.angle = 180
    
    #Lid closing animation for Movement 4
    elif num == 4:
        time.sleep(0.75)
        arm.angle = 0
        time.sleep(0.2)
        lid.angle = 180

# Main loop
while True:
    
    # Starts the Useless Box if switch is flipped on
    if button.value:
        movements(rand_int) # Calls the different movement function given a random integer
    
    # Otherwise, keep all LEDs off and lid closed
    else:
        exit_movement(rand_int) # Calls the closing arm and lif animation given the same integer as the movement
        # Turns off all the LEDs
        led_one.value = False
        led_two.value = False
        led_three.value = False
        rand_int = random.randint(1, 5) # Generates a random movement for the next switch flip

