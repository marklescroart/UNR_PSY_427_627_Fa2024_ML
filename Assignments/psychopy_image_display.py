# psychopy image display

# Create a screen onto which to render. 
# Note that this is NOT a full screen! It may be hiddne behind your 
from psychopy import visual, core
import pathlib

# Setup stimulus
win = visual.Window([400, 400])

fdir = pathlib.Path('/Users/mark/pomsync/mark/Teaching/PSY427_627/datasets/fLoc_stimuli')

images = sorted(list(fdir.glob('*jpg')))

image = visual.ImageStim(win, image=str(images[0]))
fixation = visual.GratingStim(win,
                              tex=None,
                              mask='gauss',
                              sf=0, size=0.02, name='fixation', autoLog=False)

# Let's draw a stimulus for 200 frames, drifting for frames 50:100
for frameN in range(200):   # For exactly 200 frames
    if 10 <= frameN < 150:  # Present fixation for a subset of frames
        fixation.draw()
    if 50 <= frameN < 100:  # Present stim for a different subset
        gabor.phase += 0.1  # Increment by 10th of cycle
        gabor.draw()
    win.flip()

win.close()
