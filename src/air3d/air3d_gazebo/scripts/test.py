
from sdf_generator import *
import numpy as np

sdfgen = SDFGenerator('sample', folder='../models/')

sdfgen.generateConfigFile()

sdfgen.open()
# sdfgen.addline(sdfgen.includeDrone("falcon1", np.zeros(6), updateRate=500.0))
sdfgen.addline(sdfgen.addCylinder("link0", np.zeros(6), material='Red'))
sdfgen.close()
