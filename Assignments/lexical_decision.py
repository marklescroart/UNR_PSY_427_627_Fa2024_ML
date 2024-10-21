# Import the modules we’ll need
from psychopy import core, visual, event
import random

# Initialize an empty string that will accumulate our results of each trial
results = ''

# Define our conditions
conditions = [
    ['cat', 1],
    ['tea', 1],
    ['bar', 1],
    ['ool',0],
    ['jul',0],
    ['pok',0]
]

# Randomize the conditions
random.shuffle(conditions)

# Define the window
window = visual.Window(size=(800, 700), color='black')

# Define the instructions
welcome = '''
Welcome to the lexical decision task.

You are about to see a series of characters. 

If the characters make up a word, 
press the RIGHT arrow key.

If the characters do not make up a word, 
press the LEFT arrow key.

Press SPACE to begin.
'''

instructions = visual.TextStim(window, color='white', text=welcome, units='pix', height=20)

# Display the instructions and wait for the space bar to be hit to start
instructions.draw()
window.flip()
event.waitKeys(keyList=['space'])

# Begin trials
for condition in conditions:
    
    characters = condition[0] 
    isWord = condition[1] 

    # Define the stimulus (word text)
    word = visual.TextStim(window, color='white', text=characters, units='pix', height=40)
    
    # Display the stimulus
    word.draw()
    window.flip()

    # Listen for a left or right key response
    response = event.waitKeys(keyList=['right', 'left'])
       
    # Check response accuracy
    if(isWord == 1 and response[0] == 'right'):
        correct = 1
    elif(isWord == 0 and response[0] == 'left'):
        correct = 1
    else:
        correct = 0
    
    # Append the results as an CSV string
    results += characters + ',' + str(isWord) + ',' + str(correct) + '\n'

# Output the results to the console
print(results)    

# The next two lines ensure the PsychoPy application is properly terminated. 
# If you omit these lines, the window will still close when the script is done, but these
# lines that system resources associated with the window are released properly.
window.close()
core.quit()