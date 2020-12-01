#!/usr/bin/env python
# -*- coding: utf-8 -*-
## https://run.pavlovia.org/fdelogu/covid_game/html/?fbclid=IwAR0NzZPE0JAG2ROZsL8yE1dIFH2Glm7-sMfZWgmVRpgUdDxirExBeZQ-Y_c
# ==========================================================================
# ============================= Imports ====================================
# ==========================================================================
from __future__ import absolute_import, division
from psychopy import sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, FINISHED)
import os  # handy system and path functions
from psychopy.hardware import keyboard
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2020.2.5'
expName = 'Project'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion
# ==========================================================================
# ============================= Data =======================================
# ==========================================================================
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\Dev\\Python\\CRE Student Research\\Python\\Editor\\Project.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame
# ==========================================================================
# ============================= Config =====================================
# ==========================================================================
from Config import Config as Config
cfg = Config()
cfg.load()
diaDir = os.path.join(cfg.getVal("assetDir"), "Diagrams//ArrowsNumbered.png")

colors = Config(configFile="colors.json")
colors.load()
from StateMachine import StateMachine as StateMachine
from UISettings import StateMachineDraw as StateMachineDraw
from UISettings import GUIDraw as GUIDraw
from UISettings import UIComponents as UIComponents
sm = StateMachine()
smd = StateMachineDraw()
guid = GUIDraw()
smd.setResolution(cfg.getVal("winRes"))
# ==========================================================================
# ============================= Window =====================================
# ==========================================================================
win = visual.Window(size=cfg.getVal("winRes"), fullscr=True, screen=0, winType='pyglet', allowGUI=False,
                    allowStencil=False,monitor='testMonitor', color=[0,0,0], colorSpace='rgb', blendMode='avg',
                    useFBO=True, units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()
# ==========================================================================
# =============================== Config 2 =================================
# ==========================================================================
comp = UIComponents(win, cfg.getVal("winRes"), colors)
# ==========================================================================
# =========================== Instruction Objs =============================
# ==========================================================================

InstructionsClock = core.Clock()
iheader = comp.createText('iheader', text='Instructions', pos=guid.getTextPos("instructionsHeader"), height=100, color=colors.getVal("i_text"))
ibody = comp.createText('ibody', text=guid.instructionsBodyText[0], pos=guid.getTextPos("instructionsBody"), color=colors.getVal("i_text"))
icontinue = comp.createText('icontinue', text=guid.instructionsContinueText, pos=guid.getTextPos("instructionsContinue"), color=colors.getVal("i_text"))
# ==========================================================================
# ============================== Practice Objs =============================
# ==========================================================================
PracticeClock = core.Clock()
pnumBoxes = 6
pboxes = []
pBoxText = []
for i in range(pnumBoxes):
    pboxes.append(visual.Rect(win=win, name=('pbox' + str(i)), size= smd.getBoxSize(), ori=0, pos=smd.getBoxPos(i),
                              lineWidth=1, lineColor=smd.boxLineColor, lineColorSpace='rgb255', fillColor=smd.boxColor,
                              fillColorSpace='rgb255',opacity=1, depth=0.0, interpolate=True, units='pix'))
    pBoxText.append(visual.TextStim(win=win, name='pBoxText', text=guid.stateMoves[i], font='Arial',
                                    pos=guid.getMoveTextPos(smd.getBoxPos(i)),
                                    height=25, wrapWidth=None, ori=0, color=guid.controllTextColor,
                                    colorSpace='rgb255', opacity=1, languageStyle='LTR', depth=0.0, units='pix'))

pUBox = visual.Rect(win=win, name='pubox', size= guid.getControllBoxSize(), ori=0, pos=guid.getControllButtonPos(-1),
                              lineWidth=1, lineColor=guid.controllBoxLineColor, lineColorSpace='rgb255',
                              fillColor=guid.controllBoxColor,fillColorSpace='rgb255',opacity=1, depth=0.0,
                              interpolate=True, units='pix')
pIBox = visual.Rect(win=win, name='iubox', size= guid.getControllBoxSize(), ori=0, pos=guid.getControllButtonPos(1),
                              lineWidth=1, lineColor=guid.controllBoxLineColor, lineColorSpace='rgb255',
                              fillColor=guid.controllBoxColor,fillColorSpace='rgb255',opacity=1, depth=0.0,
                              interpolate=True, units='pix')
pUtext = visual.TextStim(win=win, name='putext', text='U', font='Arial',
                          pos=guid.getControllButtonPos(-1), height=50, wrapWidth=None, ori=0, color=guid.controllTextColor,
                          colorSpace='rgb255', opacity=1, languageStyle='LTR', depth=0.0, units='pix')
pItext = visual.TextStim(win=win, name='pitext', text='I', font='Arial',
                          pos=guid.getControllButtonPos(1), height=50, wrapWidth=None, ori=0, color=guid.controllTextColor,
                          colorSpace='rgb255', opacity=1, languageStyle='LTR', depth=0.0, units='pix')


pheader = visual.TextStim(win=win, name='pheader', text='Practice', font='Arial',
                          pos=guid.getTextPos("practiceHeader"), height=100, wrapWidth=None, ori=0, color=guid.generalTextColor,
                          colorSpace='rgb255', opacity=1, languageStyle='LTR', depth=0.0, units='pix')
pbody = visual.TextStim(win=win, name='pbody', text="body text", font='Arial',
                        pos=guid.getTextPos("practiceBody"), height=50, wrapWidth=None, ori=0, color=guid.generalTextColor,
                        colorSpace='rgb255', opacity=1, languageStyle='LTR', depth=0.0, units='pix')
pdiagram = visual.ImageStim(win=win,name='pdiagram', image=diaDir, mask=None,ori=0, pos=(0, 0), size=(1136, 536),
                            color=[1,1,1], colorSpace='rgb', opacity=1, flipHoriz=False, flipVert=False, texRes=128,
                            interpolate=True, depth=-7.0, units='pix')
# ==========================================================================
# ================================ Trial Objs ==============================
# ==========================================================================
TrialClock = core.Clock()
tsound = sound.Sound('A', secs=-1, stereo=True, hamming=True, name='tsound')
tsound.setVolume(1)
tdiagram = visual.ImageStim(win=win,name='tdiagram', image=diaDir, mask=None,ori=0, pos=(0, 0), size=(0.5, 0.5),
                            color=[1,1,1], colorSpace='rgb', opacity=1, flipHoriz=False, flipVert=False, texRes=128,
                            interpolate=True, depth=-7.0)
tnumBoxes = 6
tboxes = []
for i in range(tnumBoxes):
    tboxes.append(visual.Rect(win=win, name=('box' + str(i)), width=(0.5, 0.5)[0], height=(0.5, 0.5)[1], ori=0, pos=(0, 0),
                              lineWidth=1, lineColor=smd.boxLineColor, lineColorSpace='rgb255', fillColor=smd.boxColor,
                              fillColorSpace='rgb255', opacity=1, depth=0.0, interpolate=True))
# ==========================================================================
# ================================ Exit Objs ===============================
# ==========================================================================
ExitClock = core.Clock()
etext = visual.TextStim(win=win, name='etext',
    text='Any text\n\nincluding line breaks',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
econfirm = keyboard.Keyboard()
# ==========================================================================
# =======================Create some handy timers==========================
# ==========================================================================
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine
# ==========================================================================
# ===================== Prepare Instructions ===============================
# ==========================================================================
iheader.setAutoDraw(False)
ibody.setAutoDraw(False)
icontinue.setAutoDraw(False)

instructionsIndex = 0
spacePressed = False

continueRoutine = True
# keep track of which components have finished
InstructionsComponents = [ibody, icontinue, iheader]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
# ==========================================================================
# ========================= Run Instructions ===============================
# ==========================================================================
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # ------------------draw----------------------
    iheader.draw()
    ibody.draw()
    icontinue.draw()
    # -------------- key checks ------------------
    spaceIsDown = defaultKeyboard.getKeys(keyList=["space"])
    # check if space bar was released
    if not spaceIsDown and spacePressed:
        spacePressed = False
        instructionsIndex += 1
        if instructionsIndex >= guid.lenBodyText():
            continueRoutine = False
        else:
            ibody.setText(guid.getBodyText(instructionsIndex))
    # check if space is down
    spacePressed = spaceIsDown
    # ================== Wrap Up =================================
    waitOnFlip = False
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
# ==========================================================================
# ========================= End Instructions ===============================
# ==========================================================================
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Iphase end', globalClock.getTime())

# check responses
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practices = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='practices')
thisExp.addLoop(practices)  # add the loop to the experiment
thisPractice = practices.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
if thisPractice != None:
    for paramName in thisPractice:
        exec('{} = thisPractice[paramName]'.format(paramName))

for thisPractice in practices:
    currentLoop = practices
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice:
            exec('{} = thisPractice[paramName]'.format(paramName))

    # ==========================================================================
    # ===================== Prepare Practice ===================================
    # ==========================================================================
    uPressed = False
    iPressed = False
    pItext.setAutoDraw(False)
    pUtext.setAutoDraw(False)
    pIBox.setAutoDraw(False)
    pUBox.setAutoDraw(False)
    pheader.setAutoDraw(False)
    pbody.setAutoDraw(False)
    for t in pBoxText:
        t.setAutoDraw(False)


    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the pmouse
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    PracticeComponents = [pboxes[0], pboxes[1], pboxes[2], pboxes[3], pboxes[4], pboxes[5], pdiagram]
    for thisComponent in PracticeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    smState = sm.getCurrentState()
    pboxes[smState].setFillColor((smd.boxSelectedColor), colorSpace='rgb255')
    # ==========================================================================
    # ===================== Run Practice =======================================
    # ==========================================================================
    while continueRoutine:
        # get current time
        t = PracticeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PracticeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)

        # -------draw-----
        pUBox.draw()
        pIBox.draw()
        pItext.draw()
        pUtext.draw()
        pbody.draw()
        pheader.draw()
        for box in pboxes:
            box.draw()
        for t in pBoxText:
            t.draw()
        # =================== key checks ===================
        uIsDown = defaultKeyboard.getKeys(keyList=["u"])
        iIsDown = defaultKeyboard.getKeys(keyList=["i"])
        # check U was released
        if not uIsDown and uPressed:
            pboxes[sm.getCurrentState()].setFillColor(smd.boxColor, colorSpace='rgb255')
            uPressed = False
            sm.moveCircle()
            pboxes[sm.getCurrentState()].setFillColor(smd.boxSelectedColor, colorSpace='rgb255')
            pbody.setText(f"last score: {sm.lastScore}\ntotal score: {sm.totalScore}")
        # check I was released
        if not iIsDown and iPressed:
            iPressed = False
            pboxes[sm.getCurrentState()].setFillColor(smd.boxColor, colorSpace='rgb255')
            sm.moveAcross()
            pboxes[sm.getCurrentState()].setFillColor(smd.boxSelectedColor, colorSpace='rgb255')
            pbody.setText(f"last score: {sm.lastScore}\ntotal score: {sm.totalScore}")
        uPressed = uIsDown
        iPressed = iIsDown

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # ==========================================================================
    # ========================== End Practice ==================================
    # ==========================================================================
    for thisComponent in PracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)


    # the Routine "Practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5 repeats of 'practices'


# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))

    # ==========================================================================
    # ============================ Prepare Trial ===============================
    # ==========================================================================
    continueRoutine = True
    # update component parameters for each repeat
    tsound.setSound('A', hamming=True)
    tsound.setVolume(1, log=False)
    tdiagram.setImage('None')
    TrialComponents = [tsound, tdiagram, tboxes[0], tboxes[1], tboxes[2], tboxes[3], tboxes[4], tboxes[5]]
    for thisComponent in TrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    # ==========================================================================
    # ============================= Run Trial ==================================
    # ==========================================================================
    while continueRoutine:
        # get current time
        t = TrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop tsound
        if tsound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tsound.frameNStart = frameN  # exact frame index
            tsound.tStart = t  # local t and not account for scr refresh
            tsound.tStartRefresh = tThisFlipGlobal  # on global time
            tsound.play(when=win)  # sync with win flip

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # ==========================================================================
    # ============================= End Trial ==================================
    # ==========================================================================
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    tsound.stop()  # ensure sound has stopped at end of routine
    # store data for trials (TrialHandler)

    # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5 repeats of 'trials'

# ==========================================================================
# =========================== Prepare Exit =================================
# ==========================================================================
continueRoutine = True
# update component parameters for each repeat
econfirm.keys = []
econfirm.rt = []
_econfirm_allKeys = []
# keep track of which components have finished
ExitComponents = [etext, econfirm]
for thisComponent in ExitComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ExitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# ==========================================================================
# ============================== Run Exit ==================================
# ==========================================================================
while continueRoutine:
    # get current time
    t = ExitClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ExitClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    

    
    # *econfirm* updates
    waitOnFlip = False
    if econfirm.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        econfirm.frameNStart = frameN  # exact frame index
        econfirm.tStart = t  # local t and not account for scr refresh
        econfirm.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(econfirm, 'tStartRefresh')  # time at next scr refresh
        econfirm.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(econfirm.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(econfirm.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if econfirm.status == STARTED and not waitOnFlip:
        theseKeys = econfirm.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        _econfirm_allKeys.extend(theseKeys)
        if len(_econfirm_allKeys):
            econfirm.keys = _econfirm_allKeys[-1].name  # just the last key pressed
            econfirm.rt = _econfirm_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ExitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
# ==========================================================================
# ============================= End Exit ===================================
# ==========================================================================
for thisComponent in ExitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if econfirm.keys in ['', [], None]:  # No response was made
    econfirm.keys = None
thisExp.addData('econfirm.keys',econfirm.keys)
if econfirm.keys != None:  # we had a response
    thisExp.addData('econfirm.rt', econfirm.rt)
thisExp.nextEntry()
# the Routine "Exit" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# ==========================================================================
# ============================ End Program =================================
# ==========================================================================
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
