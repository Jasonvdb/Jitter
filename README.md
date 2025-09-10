# Jitter

A Raspberry Pi Zero 2 robot control project that interfaces with a PCA9685 16-channel PWM servo driver HAT for precise servo movement control.

## Hardware Setup

- **Platform**: Raspberry Pi Zero 2 running Linux 6.12.25+rpt-rpi-v8
- **Servo Controller**: PCA9685 16-channel PWM driver at I2C address 0x40
- **Active Channels**: 7 servo channels (0-6)
- **PWM Frequency**: 50Hz for servo control
- **Pulse Width Range**: 500-2500 microseconds (0.5ms to 2.5ms)

## Quick Start

Test all servos sequentially:
```bash
python /home/jason/Bot/test.py
```

## Architecture

### Core Library
The project uses the PCA9685 library located at `/home/jason/Bot/example_code/python/PCA9685.py` for I2C communication with the servo controller.

**Key Methods:**
- `setPWMFreq(freq)`: Set PWM frequency (use 50Hz for servos)
- `setServoPulse(channel, pulse)`: Set servo position in microseconds
- `setPWM(channel, on, off)`: Direct PWM control

### Movement System
All control scripts use a step-based movement system:
- Servos move in increments (Step0, Step1, Step2, Step3)
- Position limits enforced: 500μs (min) to 2500μs (max)
- Timer-based updates every 20ms for smooth motion
- Center/neutral position: 1500μs

## Dependencies

- Python 2.7 or Python 3
- smbus or smbus2 library for I2C communication
- Standard libraries: time, math

## Usage

When creating new servo control scripts, import the PCA9685 library:
```python
import sys
sys.path.append('/home/jason/Bot/example_code/python')
from PCA9685 import PCA9685

# Initialize with 50Hz frequency
pwm = PCA9685()
pwm.setPWMFreq(50)

# Set servo position (channel 0 to center position)
pwm.setServoPulse(0, 1500)
```

## Important Notes

- Servo positions are specified in microseconds, not degrees
- Always initialize with 50Hz frequency for standard servo operation
- The robot body has physical constraints - extreme servo positions may cause mechanical issues
- The PCA9685 library exists in both python/ and python3/ directories with identical functionality
