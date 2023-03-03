#!/usr/bin/env python
from vpython import *
import numpy as np
import threading
import signal
import sys


class Air3DViz(object):
    def __init__(self):
        self.scene = canvas(title='Air3D visualizer ',
                          width=1000, height=1000,
                          center=vector(5,0,0), background=color.cyan)
        
        self.scene.caption = """To rotate "camera", drag with right button or Ctrl-drag.
                To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
                  On a two-button mouse, middle is left + right.
                To pan left/right and up/down, Shift-drag.
                Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""

        self.axes = None
        self.nozzle = None

        self.create_env()
        self._position = np.zeros(3)

        self.kill_loop = False

        signal.signal(signal.SIGINT, self.handler)
        self.thread = threading.Thread(target = self.run, args = ())
        self.thread.start()
        # self.thread.join()
        pass

    def handler(self, signal, frame):
        global THREADS
        print ("Ctrl-C.... Exiting")
        self.kill_loop = True
        sys.exit(0)


    def create_env(self):
      self.axes = []
      self.axes.append(arrow(pos=vector(0,0,0), axis=vector(5,0,0), color=vector(1,0,0), shaftwidth=0.1))
      self.axes.append(arrow(pos=vector(0,0,0), axis=vector(0,5,0), color=vector(0,1,0), shaftwidth=0.1))
      self.axes.append(arrow(pos=vector(0,0,0), axis=vector(0,0,5), color=vector(0,0,1), shaftwidth=0.1))   
      self.nozzle = sphere (color = color.green, radius = 0.1, make_trail=True, retain=-1)
      self.update_pos(np.zeros(3))

      return

    def delete_env(self):
      self.axes[0].visible =False
      self.axes[0].visible =False
      self.axes[0].visible =False
      del self.axes

      self.nozzle.visible = False
      del self.nozzle
      return

    def reset(self):
      self.delete_env()
      self.create_env()

    def update_pos(self, p):
        self._position = np.array([p[0], p[1], p[2]])
        self.nozzle.pos = vector(self._position[0],self._position[1],self._position[2])

    def run(self):
        while not self.kill_loop:
            rate(200)
            signal.pause() 


if __name__=="__main__":
    a = Air3DViz()
    a.run()
