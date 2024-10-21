# # Mouse drawing

# Setting things up
from psychopy import visual, event, core
import numpy as np
import copy

# The crucial controls for performance. Adjust to your system/liking.
distance_to_record = 2  # number of pixels between coordinate recordings
max_vector_length = 180  # number of coordinate recordings before shifting to a new ShapeStim

# Stimuli
myWin = visual.Window(units='pix', fullscr=False)
ms = event.Mouse()
myclock = core.Clock()

# The initial ShapeStim in the "stimuli" list. We can refer to the latest
# as stimuli[-1] and will do that throughout the script. The others are 
# "finished" and will only be used for draw.
my_line = visual.ShapeStim(myWin,
        lineColor='white',
        closeShape=False,
        vertices=np.empty((0, 2)))
flip_times = []
# Wait for a key, then start with this mouse position
event.waitKeys()
my_line.vertices = np.array([ms.getPos()])
myclock.reset()
tx = myclock.getTime()
while not event.getKeys():
    last = copy.copy(tx)
    # Get mouse position
    new_pos = ms.getPos()

    # Calculating distance moved since last. Pure pythagoras.
    # Index -1 is the last row.index
    x_old, y_old = my_line.vertices[-1]
    x_new, y_new = new_pos
    distance_moved = np.sqrt((x_old - x_new)**2+(y_old-y_new)**2)
    # If mouse has moved the minimum required distance, add the new vertex to the ShapeStim.
    if distance_moved > distance_to_record:
        n_vertices = len(my_line.vertices)
        if n_vertices == max_vector_length:
            my_line.vertices = np.append(my_line.vertices[1:], np.array([new_pos]), axis=0)
        else:
            my_line.vertices = np.append(my_line.vertices, np.array([new_pos]), axis=0)
        print(len(my_line.vertices))
    # ... and show it (along with any "full" ShapeStims
    my_line.draw()
    myWin.flip()
    tx = myclock.getTime()
    flip_times.append(tx-last)

myWin.close()
core.quit()

# import psychopy
# from psychopy import visual, core, event

# fullscr = False
# screen_size = [1440,900]
# max_wait = 3 

# def quit_wait(duration):
#     t0 = core.getTime()    
#     quit = False
#     while core.getTime() < (t0+duration):
#         key_out = event.getKeys(keyList=['q'], timeStamped=True)
#         if len(key_out) > 0:
#             quit = True
#             break
#     return quit




# try:
#     # Open window
#     win = visual.Window(size=screen_size, 
#                         color=(0.5,0.5,0.5),
#                         fullscr=fullscr, 
#                         units='pix',)
    
#     # Display message:
#     my_str = 'Click and drag with the mouse to draw!\n(press any key to continue)'
#     txt_stim = visual.TextStim(win, text=my_str)
#     txt_stim.draw()
#     win.flip()
#     _ = event.waitKeys()
#     t0 = core.getTime()
    
#     circ_stim = visual.Circle(win, radius=dot_size,
#                               units='pix',
#                               fillColor=(1.0, 0.0, 0.0),
#                               pos=circ_pos)
#     circ_stim.draw()
#     win.flip()

    
#     # Exercise: change this to print buttons and reaction times to file!
#     print('\n\n\n')
#     if (key_out is not None) and (len(key_out) > 0):
#         print(key_out)
#     else:
#         print('Reponse timed out!')
#     print('\n\n\n')
    
    
# except:
#     win.close()
#     # Raise last error
#     raise 
# win.close()
# core.quit()
