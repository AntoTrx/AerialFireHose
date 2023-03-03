import numpy as np
from collections import deque

class DroneAltitudeController:
    def __init__(self, desired_altitude, max_throttle, min_throttle, kp, ki, kd):
        self.desired_altitude = desired_altitude
        self.max_throttle = max_throttle
        self.min_throttle = min_throttle
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.integrator = 0
        self.previous_error = 0
    
    def get_throttle(self, current_altitude):
        error = self.desired_altitude - current_altitude
        self.integrator += error
        derivative = error - self.previous_error
        self.previous_error = error
        throttle = self.kp * error + self.ki * self.integrator + self.kd * derivative
        throttle = max(min(throttle, self.max_throttle), self.min_throttle)
        return throttle
