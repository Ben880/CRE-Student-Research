from psychopy import visual, core, event #import some libraries from PsychoPy

window = visual.Window([800,600],monitor="testMonitor", units="deg")
runSim = True

gabor = visual.GratingStim(window, tex='sin', mask='gauss', sf=5,
    name='gabor', autoLog=False)
fixation = visual.GratingStim(window, tex=None, mask='gauss', sf=0, size=0.02,
    name='fixation', autoLog=False)
frameCounter = visual.TextStim(window)
frameCounter.pos = [8,6]
frameCounter.height = .5
#frameCounter.alignText='right'

frameN = 0
while runSim:
    frameN += 1
    frameCounter.text = frameN
    frameCounter.draw()
    window.flip()
    if len(event.getKeys())>0:
        runSim = False
    if frameN>=1000:
        runSim = False
    event.clearEvents()

#cleanup
window.close()
core.quit()