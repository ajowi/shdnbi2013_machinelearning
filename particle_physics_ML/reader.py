from sklearn import tree
import numpy as np

import matplotlib.pylab as plt


import sys

# Read in the jet info for this event.
#jets = []
f = open('../resources/particle_physics/data/data.txt')
out_f = open('testing.dat','w')
#line = f.readline()
#njets = int(line)
for line  in f:
    line = f.readline()
    vals = line.split()
    e = float(vals[0])
    px = float(vals[1])
    py = float(vals[2])
    pz = float(vals[3])
    bquark_jet_tag = float(vals[4])
    #jets.append([e,px,py,pz,bquark_jet_tag])
    out_f.write("%f %f %f %d %f\n" % (e,px,py,pz,bquark_jet_tag))# Write our testing data for the ML algo -- added by @daaj
