# -*- coding: utf-8 -*-
"""

Ronan's playground, nobody else allowed on the rides ;)

"""

#%% Import libraries & functions

# import libraries
import numpy as np
import matplotlib.pyplot as plt
from tspFunctions import *
from plotdata import *
import pickle

#%% Load Experiments File

distances_file = 'tsp_matrices/toy_d.csv'
optimal_route_file = 'tsp_matrices/toy_s.csv'

int_R, optimal_route, optimal_route_cost =  loadTSPmatrix(distances_file, optimal_route_file)


#%% Q-Learning Experiment 1: Default parameters

# load and prepare plotting data
plotData = np.load('results/expResults1.npy')
plotData = plotData - optimal_route_cost
smooth = 50; plotData = getWindowAverage(plotData, smooth)
legendData =  pickle.load( open('results/expParameters1.p', 'rb' ))

# plot
title = ['Experiment 1: Q-Learning with Default Parameters\n', 'expResults1']

# plot and save
diagnosticsPlot(plotData, legendData, title, saveFile = True)

#%% Q-Learning Experiment 2:  Vary Learning Rate (Alpha)

# choose subset of problems for final plot
subset = [0,1,3,5,7]
subDict = {}

# load and prepare plotting data
plotData = np.load('results/expResults2.npy')
plotData = plotData - optimal_route_cost
plotData = plotData[:,subset] # select results of interest
smooth = 50; plotData = getWindowAverage(plotData, smooth)
legendData =  pickle.load( open('results/expParameters2.p', 'rb' ))

# update legendData to reflect subset of results being plotted
newIdx = 0
for d in subset:
    subDict[newIdx] = legendData[d]
    newIdx += 1  
legendData =  subDict

#plot
title = ['Experiment 2: Q-Learning with Different Learning Rates\n', 'expResults2']

# plot and save
diagnosticsPlot(plotData, legendData, title, saveFile = True)


#%% Q-Learning Experiment 3: Vary Gamma

# choose subset of problems for final plot
subset = [0,1,3,5,7]
subDict = {}

# load and prepare plotting data
plotData = np.load('results/expResults3.npy')
plotData = plotData - optimal_route_cost
plotData = plotData[:,subset] # select results of interest
smooth = 50; plotData = getWindowAverage(plotData, smooth)
legendData =  pickle.load( open('results/expParameters3.p', 'rb' ))

# update legendData to reflect subset of results being plotted
newIdx = 0
for d in subset:
    subDict[newIdx] = legendData[d]
    newIdx += 1  
legendData =  subDict

title = ['Experiment 3: Q-Learning with Different Discount Factors\n', 'expResults3']

# plot and save
diagnosticsPlot(plotData, legendData, title, saveFile = True)

#%% Q-Learning Experiment 4: Vary Epsilon Decay

# choose subset of problems for final plot
subset = [0,2,4,5,6]
subDict = {}

# load and prepare plotting data
plotData = np.load('results/expResults4.npy')
plotData = plotData - optimal_route_cost
plotData = plotData[:,subset] # select results of interest
smooth = 50; plotData = getWindowAverage(plotData, smooth)
legendData =  pickle.load( open('results/expParameters4.p', 'rb' ))

# update legendData to reflect subset of results being plotted
newIdx = 0
for d in subset:
    subDict[newIdx] = legendData[d]
    newIdx += 1  
legendData =  subDict

title = ['Experiment 4: Q-Learning with Different Decay Rates\n', 'expResults4']

# plot and save
diagnosticsPlot(plotData, legendData, title, saveFile = True)


#%% Q-Learning Experiment 5: #%% Q-Learning Experiment 5: Optimise Parameters (gamma)

# choose subset of problems for final plot
subset = [0,1,2,3,4,5,6,7]
subDict = {}

# load and prepare plotting data
plotData = np.load('results/expResults5.npy')
plotData = plotData - optimal_route_cost
plotData = plotData[:,subset] # select results of interest
smooth = 50; plotData = getWindowAverage(plotData, smooth)
legendData =  pickle.load( open('results/expParameters5.p', 'rb' ))

# update legendData to reflect subset of results being plotted
newIdx = 0
for d in subset:
    subDict[newIdx] = legendData[d]
    newIdx += 1  
legendData =  subDict

title = ['Experiment 5: Q-Learning with Different Decay Rates\n', 'expResults5']

# plot and save
diagnosticsPlot(plotData, legendData, title, saveFile = True)