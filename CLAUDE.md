# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Raspberry Pi Zero 2 robot control project that interfaces with a PCA9685 16-channel PWM servo driver HAT with 7 servo channels connected. The robot uses I2C communication to control servos for movement.

## Hardware Configuration

- **Platform**: Raspberry Pi Zero 2 running Linux 6.12.25+rpt-rpi-v8
- **Servo Controller**: PCA9685 16-channel PWM driver at I2C address 0x40
- **Active Channels**: 7 servo channels (0-6)
- **PWM Frequency**: 50Hz for servo control
- **Pulse Width Range**: 500-2500 microseconds (0.5ms to 2.5ms)

## Key Commands

### Running Servo Control Scripts
```bash
# Test all servos sequentially
python /home/jason/Bot/test.py
```

### Git Operations
When the user says "commit", automatically:
1. Stage all changes: `git add .`
2. Create a commit with a descriptive message based on the changes
3. Push to the remote repository: `git push`

Repository: https://github.com/Jasonvdb/Jitter

## Architecture

### Core Library: PCA9685.py
Located at `/home/jason/Bot/example_code/python/PCA9685.py`
- Provides low-level I2C communication with the servo controller
- Key methods:
  - `setPWMFreq(freq)`: Set PWM frequency (use 50Hz for servos)
  - `setServoPulse(channel, pulse)`: Set servo position in microseconds
  - `setPWM(channel, on, off)`: Direct PWM control

### Control Modes

**Direct Control**: Scripts like `test.py` that directly control servos through the PCA9685 library

### Servo Movement Pattern
All control scripts use a step-based movement system:
- Servos move in increments (Step0, Step1, Step2, Step3)
- Position limits enforced: 500μs (min) to 2500μs (max)
- Timer-based updates every 20ms for smooth motion
- Center/neutral position: 1500μs

## Dependencies

- Python 2.7 or Python 3
- smbus or smbus2 library for I2C communication
- Standard libraries: time, math

## Important Notes

- The PCA9685 library exists in both python/ and python3/ directories with identical functionality
- When creating new servo control scripts, import the PCA9685 library using:
  ```python
  sys.path.append('/home/jason/Bot/example_code/python')
  from PCA9685 import PCA9685
  ```
- Always initialize with 50Hz frequency for standard servo operation
- Servo positions are specified in microseconds, not degrees
- The robot body has physical constraints - extreme servo positions may cause mechanical issues