# Full screen 

#%%Imports 
import psychopy
from psychopy import visual, core
import glob
import matplotlib.pyplot as plt
import numpy as np

#%% Define experiment parameters
info = dict(image_dir='/Users/mark/Teaching/PSY427_627/datasets/fLoc_stimuli/',
)
            
# Here, we will 
conditions = ['adult', 'body', 'corridor']
image_files = {}
for condition in conditions: 
    image_files[condition] = sorted(list(glob.glob(info['image_dir'] + f'*{condition}*')))

block_order = [0, 2, 1] # ...
#%%
fps = 60
ifi = 1/fps
# Timing demo in python 

#%% Set up screen

# Create a full screen window
screen_size = [800,600]
win = visual.Window(size=screen_size, 
                    color=(0.5,0.5,0.5),
                    fullscr=False, 
                    units='pix')
#%%
n_trials = 10
locations_x = np.random.randint(low=-200, high=200, size=n_trials)

time_to_wait = 1
im_time = .1
f0 = win.flip()
condition = 'adult'
exp_start = win.flip()
exp_clock = psychopy.clock.Clock()
t0 = exp_clock.getTime()
print('t0:', t0)
iti = 1
t_last = t0
circ_pos = (0, 0) # Center of screen
print(circ_pos)
circ_stim = visual.Circle(win, radius=4,
                          units='pix',
                          fillColor=(1.0, 0.5, 0.0),
                          pos=circ_pos)

win.flip()

for trial in range(n_trials):
    img = visual.ImageStim(win, image=image_files[condition][trial], 
                           units='pix', size=(300,300),
                           pos=[locations_x[trial], 0])    
    img.draw()
    circ_stim.draw()
    core.wait(iti - ifi * .1)
    f1 = win.flip()
    t_up = exp_clock.getTime()
    core.wait(im_time - ifi * .1)    
    circ_stim.draw()
    x = win.flip()
    t_down = exp_clock.getTime()
    print(t_down - t_up)
    t_last = t_down
    
win.close()
core.quit()