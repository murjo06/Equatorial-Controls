import time

SLOW_MOTION_TO_SPHERICAL = 1.5
GEAR_RATIO = 1
EARTH_ROTATION_SPEED = 0.004166666
MOVE_SPEED = 1
HEMISPHERE = 1 #set hemisphere as 1 for northern, -1 for southern

#make sure that the telescope is centered at Polaris (the celestial pole) before using this program

rightAscension = 0
declenation = 0
tracking = False
speedResolution = 0.02

def spinMotor(motor, speed, duration = 0, direction = 1):
    if duration != 0:
        print(f"spinning motor {motor} at {speed} degrees per second for {duration} seconds")
    if duration == 0:
        print("    ")

def move(ra, dec):
    rightAscensionDifference = rightAscension - ra
    declenationDifference = declenation - dec
    spinMotor("ra", MOVE_SPEED, rightAscensionDifference / MOVE_SPEED)
    spinMotor("dec", MOVE_SPEED, declenationDifference / MOVE_SPEED)
    rightAscension = ra
    declenation = dec

def track(ra, dec):
    move(ra, dec)
    spinMotor("ra", EARTH_ROTATION_SPEED * HEMISPHERE)
    while tracking:
        rightAscension += EARTH_ROTATION_SPEED * speedResolution
        time.sleep(speedResolution)