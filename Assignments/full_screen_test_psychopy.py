# Fullscreen test

#%%Imports 
import psychopy
from psychopy import visual, core
from psychopy.hardware import keyboard
import glob
import matplotlib.pyplot as plt

kb = keyboard.Keyboard()
t0 = core.getTime()
wait_time = 3
full_screen = True
if full_screen:
    screen_size = (1440, 900)
else: 
    screen_size = (600, 600)

win = visual.Window(screen_size, fullscr=full_screen, screen=0, color=(0.5, 0.5, 0.5))


keys = []
kb.clock.reset()
while (len(keys) == 0) and (core.getTime() < t0 + wait_time):
    keys = kb.getKeys(keyList=['left','right', 'q'])     

print('\n\n\n')
if len(keys) > 0:
    print(f"You pressed {keys[0].name}")
else:
    print("Response timed out!")

print('\n\n\n')
win.close()