import matplotlib as plt
plt.use('TkAgg')

import pylab as PL
import random as RD
import scipy as SP

# Set parameters

width = 200
height = 200

# Now sample the agents.
def init():
    global time, config, space, facing

    time = 0

    config = SP.zeros([height, width])

    space = [height / 2, width / 2]
    facing = 1


def move_forward():
    global time, config, space, facing

    if facing == 0: #north
        space[0] = (space[0] + 1) % height
    elif facing == 1: #East
        space[1] = (space[1] + 1) % width
    elif facing == 2: #South
        space[0] = (space[0] - 1)
    elif facing == 3: #West
        space[1] = (space[1] - 1)
    
    if space[0] < 0:
        space[0] = height - 1
    if space[1] < 0:
        space[1] = width - 1
        
    #print("x = {} y = {}".format(space[0], space[1]))
        
    return space

def draw():
    PL.cla()
    PL.pcolor(config, vmin = 0, vmax = 1, cmap = PL.cm.binary)
    PL.axis('image')
    PL.title('t = ' + str(time))

def step():
    global time, config, space, facing

    time += 1
    #if space config is black, change to white
    # then turns right
    if config[space[0], space[1]] == 1:
        config[space[0], space[1]] = 0
        facing = (facing + 1) % 4
        
    #else space config is white, change to black
    # then turns left
    else:
        config[space[0], space[1]] = 1
        facing = (facing - 1)
        if facing < 0:
            facing = 3
        
    move_forward()
    

# Initialize config
import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])
        
        