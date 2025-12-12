
#!/usr/bin/env pybricks-micropython
# Square drive helper for EV3 (1x1 meter continuous square)

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

ev3 = EV3Brick()
ultra = UltrasonicSensor(Port.S4)
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

WHEEL_DIAMETER_MM = 56
AXLE_TRACK_MM = 114

drive_base = DriveBase(left_motor, right_motor, WHEEL_DIAMETER_MM, AXLE_TRACK_MM)

def meters_to_mm(meters: float) -> int:
    return int(round(meters * 1000))

def drive_straight_m(meters: float, pause_ms: int = 100) -> None:
    """Drive straight for a given distance in meters (blocking)."""
    distance_mm = meters_to_mm(meters)
    drive_base.straight(distance_mm)
    wait(pause_ms)

def turn_right_90(pause_ms: int = 100) -> None:
    """Turn approximately 90 degrees to the right (blocking)."""
    drive_base.turn(90)
    wait(pause_ms)

def square_once(side_m: float = 1.0) -> None:
    """Drive one 1x1 meter square (4 sides)."""
    for _ in range(4):
        drive_straight_m(side_m)
        turn_right_90()

def square_continuous(side_m: float = 1.0) -> None:
    """Keep driving continuous squares until the program is stopped."""
    ev3.speaker.beep(frequency=800, duration=150)
    while True:
        square_once(side_m)

# Entry point: continuously drive 1x1 meter squares
if __name__ == "__main__":
    # Ensure motors start from known angle
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)

    # Start continuous square driving (1 meter sides)
    square_continuous(1.0)
