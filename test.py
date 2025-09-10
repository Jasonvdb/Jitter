#!/usr/bin/python

import time
import sys
sys.path.append('/home/jason/Bot/example_code/python')
from PCA9685 import PCA9685

# Initialize PCA9685
pwm = PCA9685(0x40, debug=False)
pwm.setPWMFreq(50)  # Set frequency to 50Hz for servos

# Define servo positions (in microseconds)
MIN_PULSE = 500   # Minimum pulse width (0.5ms)
MID_PULSE = 1500  # Middle position (1.5ms)
MAX_PULSE = 2500  # Maximum pulse width (2.5ms)

print("Starting servo test - moving 7 servos one by one")

# Move each servo from min to max and back to center
for channel in range(7):
    print(f"\nMoving servo on channel {channel}")
    
    # Move to minimum position
    print(f"  Channel {channel}: Moving to MIN position")
    pwm.setServoPulse(channel, MIN_PULSE)
    time.sleep(1)
    
    # Move to maximum position
    print(f"  Channel {channel}: Moving to MAX position")
    pwm.setServoPulse(channel, MAX_PULSE)
    time.sleep(1)
    
    # Return to center position
    print(f"  Channel {channel}: Returning to CENTER position")
    pwm.setServoPulse(channel, MID_PULSE)
    time.sleep(1)

print("\nServo test complete - all 7 servos have been moved")