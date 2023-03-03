import numpy as np
import cvxpy as cvx
import time
from collections import deque


class PIDController(object):
    def __init__(self, mass=1.0, dt=1/100):
        self._kp = np.array([4, 4, 6])
        self._ki = np.array([0.5, 0.5, 1])
        self._kd = np.array([2.5, 2.5, 3])

        self._gvec = np.array([0., 0., 9.81])
        self._mass = mass
        self._dt = dt
        self._integral_error = deque([], maxlen=500)


    def run(self, p, v, pd, vd=np.zeros(3), ad=np.zeros(3), ff=np.zeros(3)):
        pos_err = p-pd
        integral_force = np.multiply(self._ki, sum(self._integral_error)) 
        # print(integral_force)
        force = -np.multiply(self._kp, pos_err) - \
            np.multiply(self._kd, v-vd) + self._mass*(self._gvec+ad) - \
            integral_force + ff
        self._integral_error.append(pos_err*self._dt)
        return force

class CBF_QP(object):
    def __init__(self):
        self._pid  = PIDController()
        self.uRef = np.zeros(3)
        self.uPrev = np.zeros(3)
        self.Qref = 10 * np.eye(3) #(u-uRef)^T*Qref*(u-uRef)
        self.Qprev = np.zeros((3, 3)) #(u-uRef)^T*Qprev*(u-uRef)
        self.uMax = np.array([9.81, 9.81, 9.81])
        self.uMin = np.array([-9.81, -9.81, 9.81])
        self.Aineq = np.zeros(3)
        self.bineq = -1e10 * np.ones(3)
        self._mass = 1.0
        self.u = cvx.Variable(3)

        self.constraints = [self.uMin <= self.u, self.u <= self.uMax, self.Aineq @ self.u >= self.bineq]
        self.obj = cvx.Minimize(0)
        qp = cvx.Problem(self.obj, self.constraints)  # Initialize problem with zero objective
        qp.solve(solver='OSQP', max_iter = 10000)
        
    def run(self, p, v, pd, xj, vj, vd, ad, ff):
        fOpt = self.run_cbf_qp(p, v, pd, xj, vj, vd, ad, ff)
        print(fOpt)
        if fOpt is None:
            print("CBF failed using PID control")
            return self.uRef
        else:
            return fOpt

    def run_cbf_qp(self, p, v, pd, xj, vj, vd, ad, ff):
        self.uRef = self._pid.run(p , v, pd, vd, ad, ff)
        start = time.time()
        self.compute_barrier_constraints(self.uRef, p, v, xj, vj)
        
        self.cost1 = cvx.quad_form(self.u - self.uRef, self.Qref)
        self.cost2 = cvx.quad_form(self.u - self.uPrev, self.Qprev)
        self.cost = self.cost1 + self.cost2
        self.obj = cvx.Minimize(self.cost)
        qp = cvx.Problem(self.obj, self.constraints)
        qp.solve(solver='OSQP', max_iter = 10000)
        #print("status:", qp.status)
        #print("optimal value", qp.value)
        #print("optimal var", self.u.value)
        stop = time.time()
        duration = stop - start
        
        print("Time taken by compute_barrier_constraints: ", duration * 1e3, " ms")
        #print("Aineq: ", self.Aineq)
        #print("bineq: ", self.bineq)
        
        return self.u.value

    def compute_barrier_constraints(self, u, p ,v, xj, vj):
        radius = 0.6
        self.xi = p
        self.xj = xj
        self.vi = v
        self.vj = vj
        accel = u/self._mass
        B = ((self.xi - self.xj).transpose() @ (self.xi - self.xj)) - radius**2
        dB = 2 * ((self.xi - self.xj).transpose() @ (self.vi - self.vj))
        LgLfB = 2 * (self.xi - self.xj).transpose()
        L2fB = -2 * ((self.xi - self.xj).transpose() * accel) + 2 * ((self.vi - self.vj).transpose() @ (self.vi - self.vj))
        k1 = -2
        k2 = -1
        self.bineq = k1 * B + k2 * dB - L2fB
        self.Aineq = LgLfB
        self.constraints = [self.uMin <= self.u, self.u <= self.uMax, self.Aineq @ self.u >= self.bineq]
    
