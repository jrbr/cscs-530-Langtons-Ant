import matplotlib as plt
plt.use('TkAgg')

import pylab as PL
import random as RD
import scipy as SP

# Set parameters

size = 100
width = size
height = size

# Now sample the agents.
def init():
    global ants, time, config, directions

    time = 0
    '''
    ants = [[height / 4, width / 4]]

    ants.append([3 * size / 4, size / 4])
    ants.append([size / 4, 3 * size / 4])
    ants.append([3 * size / 4, 3 * size / 4])

    '''

    ants = [[height / 2 -1, width / 2 - 1]]

    ants.append([height / 2 - 1, width / 2])
    ants.append([height / 2, width / 2 - 1])
    ants.append([height / 2, width / 2])
    directions = [0, 1, 2, 3]

    config = SP.zeros([height, width])
    facing = 1



def move_all_forward():
    global time, config, ants, directions

    for i in range(0,4):
        if directions[i] == 0: #north
            ants[i][0] = (ants[i][0] + 1) % height
        elif directions[i] == 1: #East
            ants[i][1] = (ants[i][1] + 1) % width
        elif directions[i] == 2: #South
            ants[i][0] = (ants[i][0] - 1)
        elif directions[i] == 3: #West
            ants[i][1] = (ants[i][1] - 1)
        
        if ants[i][0] < 0:
            ants[i][0] = height - 1
        if ants[i][1] < 0:
            ants[i][1] = width - 1
        
    #print("x = {} y = {}".format(space[0], space[1]))

def draw():
    PL.cla()
    PL.pcolor(config, vmin = 0, vmax = 1, cmap = PL.cm.binary)
    PL.axis('image')
    PL.title('t = ' + str(time))

def step():
    global time, config, ants, directions

    time += 1
    #if space config is black, change to white
    # then turns right
    for i in range(0,4):
        if config[ants[i][0], ants[i][1]] == 1:
            config[ants[i][0], ants[i][1]] = 0
            directions[i] = (directions[i] + 1) % 4
            
        #else space config is white, change to black
        # then turns left
        else:
            config[ants[i][0], ants[i][1]] = 1
            directions[i] = (directions[i] - 1)
            if directions[i] < 0:
                directions[i] = 3
        
    move_all_forward()
    

# Initialize config
import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])
        
        