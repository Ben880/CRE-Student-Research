from psychopy import visual, core


win = visual.Window([400,400])
message = visual.TextStim(win, text='hello')
message.autoDraw = True  # Automatically draw every frame
win.flip()
core.wait(2.0)
message.text = 'world'  # Change properties of existing stim
win.flip()
core.wait(2.0)

from psychopy import visual, core

# Setup stimulus
win = visual.Window([400, 400])
gabor = visual.GratingStim(win, tex='sin', mask='gauss', sf=5, name='gabor')
gabor.autoDraw = True  # Automatically draw every frame
gabor.autoLog = False  # Or we'll get many messages about phase change

# Let's draw a stimulus for 2s, drifting for middle 0.5s
clock = core.Clock()
while clock.getTime() < 2.0:  # Clock times are in seconds
    if 0.5 <= clock.getTime() < 1.0:
        gabor.phase += 0.1  # Increment by 10th of cycle
    win.flip()

from psychopy import visual, core

# Setup stimulus
win = visual.Window([400, 400])
gabor = visual.GratingStim(win, tex='sin', mask='gauss', sf=5,
    name='gabor', autoLog=False)
fixation = visual.GratingStim(win, tex=None, mask='gauss', sf=0, size=0.02,
    name='fixation', autoLog=False)

# Let's draw a stimulus for 200 frames, drifting for frames 50:100
for frameN in range(200):   # For exactly 200 frames
    if 10 <= frameN < 150:  # Present fixation for a subset of frames
        fixation.draw()
    if 50 <= frameN < 100:  # Present stim for a different subset
        gabor.phase += 0.1  # Increment by 10th of cycle
        gabor.draw()
    win.flip()