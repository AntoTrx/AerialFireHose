import numpy as np
import cvxpy as cvx
import casadi as ca
import time
from collections import deque


class PIDController(object):
    def __init__(self, mass=1.0, dt=1/100):
    	#4,4,6
    	#0.5,0.5,1
    	#2.5,2.5,3
        self._kp = np.array([1.2, 1.2, 2.8])
        self._ki = np.array([0.6, 0.6, 1.0])
        self._kd = np.array([3, 3, 5])
	
        self._gvec = np.array([0., 0., 9.81])
        self._mass = mass
        self._dt = dt
        self._integral_error = deque([], maxlen=500)
        self.u = np.zeros(3)


    def run(self, p, v, pd, vd=np.zeros(3), ad=np.zeros(3), ff=np.zeros(3)):
        pos_err = p-pd
        integral_force = np.multiply(self._ki, sum(self._integral_error)) 
        #print("Integral force: ", integral_force)
        #print("ff : ", ff)
        force = -np.multiply(self._kp, pos_err) - \
            np.multiply(self._kd, v-vd) + self._mass*(self._gvec+ad) - \
            integral_force + ff
        self._integral_error.append(pos_err*self._dt)
        self.u = force
        #print("PID Value: ", force)
        return force

class CBF_QP_Casadi(object):
    
    def __init__(self):
        self._pid  = PIDController()
        self.uPID = np.zeros(3)
        self.Aineq = np.ones(2)
        self.bineq = -1*np.ones(2)

        #initialize CASADI
        self.opti = ca.Opti()
        x = opti.variable(2, 1)

        self.opti.subject_to(x <= self.uMax) #constraints
        self.opti.subject_to(self.uMin <= x)
        self.opti.subject_to(self.Aineq[0] * x[0] >= self.bineq[0])
        self.opti.subject_to(self.Aineq[1] * x[1] >= self.bineq[1])

        self.Q = np.diag([2, 10]) #vectors for cost function
        self.c = np.array([[1, 2]]).T

        cost = x.T@self.Q@x + self.c.T@x
        self.opti.minimize(cost)
        option = {"verbose": False, "ipopt.print_level": 0, "print_time": 0} 
        self.opti.solver("ipopt", option)
        sol = self.opti.solve()
        x_opti = sol.value(x)
        print(x_opti)

    def run():
        fOpt = self.uPID

    def solve_casadi(self):
        """
        Update contraints for CASADI
        """
        self.opti.subject_to(x <= self.uMax)
        self.opti.subject_to(self.uMin <= x)
        self.opti.subject_to(self.Aineq[0] * x[0] >= self.bineq[0])
        self.opti.subject_to(self.Aineq[1] * x[1] >= self.bineq[1])
 
        self.update_constraint()
        self.cost = self.x.T@self.Q@self.x + self.c.T@self.x
        self.opti.minimize(self.cost)
        option = {"verbose": False, "ipopt.print_level": 0, "print_time": 0} 
        self.opti.solver("ipopt", option)
        sol = self.opti.solve()
        x_opti = sol.value(self.x)


class CBF_QP_OSQP(object):
    def __init__(self):
        self._pid  = PIDController()
        self.uPID = np.zeros(3)
        self._mass = 1.0
        
        #Inititalize Cost Function
        self.uRef = np.zeros(2)
        self.uPrev = np.zeros(2)
        self.Qref = 10 * np.eye(2) #(u-uRef)^T*Qref*(u-uRef)
        self.Qprev = np.zeros((2, 2)) #(u-uRef)^T*Qprev*(u-uRef)
        self.uMax = np.array([5.0, 5.0])
        self.uMin = np.array([-5.0, -5.0])
        self.Aineq = np.ones(2)
        self.bineq = -1*np.ones(2)
    
        self.k1 = -2.0
        self.k2 = -3.0
        self.B = 0.0

        #Initialize CVXPY with zero objective
        self.u = cvx.Variable(2)
        self.constraints = [self.uMin <= self.u, self.u <= self.uMax, self.Aineq @ self.u >= self.bineq]
        self.obj = cvx.Minimize(0)
        qp = cvx.Problem(self.obj, self.constraints)
        qp.solve(solver='OSQP', max_iter = 10000)
        
    def run(self, p, v, pd, xj, vj, aj, vd, ad, ff):
        fOpt = self.run_cbf_qp(p, v, pd, xj, vj, aj, vd, ad, ff)
        if fOpt is None:
            return self.uPID
        else:
            return fOpt

    def run_cbf_qp(self, p, v, pd, xj, vj, aj, vd, ad, ff):
        self.uPID = self._pid.run(p , v, pd, vd, ad, ff)
        self.uRef = self.uPID[0:2]

        #Calculate CBF constraints
        self.compute_barrier_constraints(self.uRef, p, v, xj, vj, aj)

        #Use cvxpy to solve the nonlinear system
        self.cost1 = cvx.quad_form(self.u - self.uRef, self.Qref)
        self.cost2 = cvx.quad_form(self.u - self.uPrev, self.Qprev)
        self.cost = self.cost1 + self.cost2
        self.obj = cvx.Minimize(self.cost)
        qp = cvx.Problem(self.obj, self.constraints)
        qp.solve(solver='OSQP', max_iter = 20000)
        #print("status:", qp.status)
        #print("optimal value", qp.value)
        self.uRef = self.u.value
        self.uPrev = self.uRef
        uOpt = np.array([self.uRef[0], self.uRef[1], self.uPID[2]])
        return uOpt
	    
    def compute_barrier_constraints(self, u, p ,v, xj, vj, aj):
        """
        Calculate CBF contraints
        """
        radius = 1.0
        xi = p[0:2]
        xj = xj[0:2]
        vi = v[0:2]
        vj = vj[0:2]
        ai = u/self._mass
        aj = aj[0:2]

        self.B = ((xi - xj).transpose() @ (xi - xj)) - radius**2
        print("B: ", self.B)
        dB = 2 * ((xi - xj).transpose() @ (vi - vj))
        d2B = (2*(xi - xj).transpose() @ (ai - aj)) + 2*(vi - vj).transpose() @ (vi - vj)
        LgLfB = 2 * (xi - xj).transpose()
        L2fB = -2 * ((xi - xj).transpose() @ (aj)) + 2 * ((vi - vj).transpose() @ (vi - vj))
        self.bineq = self.k1 * self.B + self.k2 * dB - L2fB
        self.Aineq = LgLfB
        self.constraints = [self.uMin <= self.u, self.u <= self.uMax, self.Aineq @ self.u  >= self.bineq]
    
 

