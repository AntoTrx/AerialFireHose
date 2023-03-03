import numpy as np
from collections import deque


class PIDController(object):
    def __init__(self, mass=0.75, dt=1/100):
        self._kp = np.array([4, 4, 6])
        self._ki = np.array([0.5, 0.5, 1])
        self._kd = np.array([2.5, 2.5, 3])

        self._gvec = np.array([0., 0., 9.81])
        self._mass = mass
        self._dt = dt
        self._integral_error = deque([], maxlen=500)

    def run(self, p, v, pd, vd=np.zeros(3), ff=np.zeros(3)):

        pos_err = p-pd
        integral_force = np.multiply(self._ki, sum(self._integral_error)) 
        # print(integral_force)
        force = -np.multiply(self._kp, pos_err) - \
            np.multiply(self._kd, v-vd) + self._mass*self._gvec - \
            integral_force + ff
        self._integral_error.append(pos_err*self._dt)
        return force

        # Define the Control Barrier Function (CBF)
    def cbf(x):
        h = x[0] + x[1] - 1
        dh = np.array([1, 1])
        alpha = 1
        beta = 1
        cbf_val = alpha * h + beta * np.dot(dh, x[2:])
        return cbf_val

    # Define the safety set
    def safety_set(x):
        if x[0] + x[1] >= 1:
            return True
        else:
            return False

    # Define the dynamics with the CBF
    def dynamics_with_cbf(t, x):
        u = -K.dot(x)
        cbf_val = cbf(x)
        if cbf_val <= 0:
            # Apply the safety controller
            v = np.zeros((1, 2))
            v[0, 0] = -x[2] - 1
            v[0, 1] = -x[3] - 1
            u = u + np.dot(np.transpose(x[2:]), v)
        xdot = A.dot(x) + B.dot(u)
        return xdot