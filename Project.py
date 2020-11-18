#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
from Config import Config as config
cfg = config()
cfg.load()
diaDir = os.path.join(cfg.getVal("assetDir"), "Diagrams//ArrowsNumbered.png")
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
# =========================== Instruction Objs =============================
# ==========================================================================
InstructionsClock = core.Clock()
itext = visual.TextStim(win=win, name='itext', text='press space to continue', font='Arial', pos=(0, 0), height=0.05,
                        wrapWidth=None, ori=0, color='white', colorSpace='rgb', opacity=1, languageStyle='LTR',
                        depth=0.0);
iheader = visual.TextStim(win=win, name='iheader', text='Instructions', font='Arial', pos=(0, .1), height=0.1,
                        wrapWidth=None, ori=0, color='white', colorSpace='rgb', opacity=1, languageStyle='LTR',
                        depth=0.0);
iconfirm = keyboard.Keyboard()
# ==========================================================================
# ============================== Practice Objs =============================
# ==========================================================================
PracticeClock = core.Clock()
pnumBoxes = 6
pboxes = []
for i in range(pnumBoxes):
    pboxes.append(visual.Rect(win=win, name=('pbox' + str(i)), size= [100,100], ori=0, pos=((110*i)-330, 0),
                    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb', fillColor=[255,1,1], fillColorSpace='rgb255',
                    opacity=.2, depth=0.0, interpolate=True, units= 'pix'))

pmouse = event.Mouse(win=win)
x, y = [None, None]
pmouse.mouseClock = core.Clock()
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
                    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb', fillColor=[1,1,1], fillColorSpace='rgb',
                    opacity=1, depth=0.0, interpolate=True))
tmouse = event.Mouse(win=win)
x, y = [None, None]
tmouse.mouseClock = core.Clock()
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
continueRoutine = True
# update component parameters for each repeat
iconfirm.keys = []
iconfirm.rt = []
_iconfirm_allKeys = []
# keep track of which components have finished
InstructionsComponents = [itext, iconfirm, iheader]
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
    # update/draw components on each frame

    # *iheader* updates
    if iheader.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        iheader.frameNStart = frameN  # exact frame index
        iheader.tStart = t  # local t and not account for scr refresh
        iheader.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iheader, 'tStartRefresh')  # time at next scr refresh
        iheader.setAutoDraw(True)

    # *itext* updates
    if itext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        itext.frameNStart = frameN  # exact frame index
        itext.tStart = t  # local t and not account for scr refresh
        itext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(itext, 'tStartRefresh')  # time at next scr refresh
        itext.setAutoDraw(True)
    
    # *iconfirm* updates
    waitOnFlip = False
    if iconfirm.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        iconfirm.frameNStart = frameN  # exact frame index
        iconfirm.tStart = t  # local t and not account for scr refresh
        iconfirm.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(iconfirm, 'tStartRefresh')  # time at next scr refresh
        iconfirm.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(iconfirm.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(iconfirm.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if iconfirm.status == STARTED and not waitOnFlip:
        theseKeys = iconfirm.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        _iconfirm_allKeys.extend(theseKeys)
        if len(_iconfirm_allKeys):
            iconfirm.keys = _iconfirm_allKeys[-1].name  # just the last key pressed
            iconfirm.rt = _iconfirm_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
thisExp.addData('itext.started', itext.tStartRefresh)
thisExp.addData('itext.stopped', itext.tStopRefresh)
# check responses
if iconfirm.keys in ['', [], None]:  # No response was made
    iconfirm.keys = None
thisExp.addData('iconfirm.keys',iconfirm.keys)
if iconfirm.keys != None:  # we had a response
    thisExp.addData('iconfirm.rt', iconfirm.rt)
thisExp.addData('iconfirm.started', iconfirm.tStartRefresh)
thisExp.addData('iconfirm.stopped', iconfirm.tStopRefresh)
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
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the pmouse
    pmouse.clicked_pclicked = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    PracticeComponents = [pboxes[0], pboxes[1], pboxes[2], pboxes[3], pboxes[4], pboxes[5], pmouse, pdiagram]
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
    # ==========================================================================
    # ===================== Run Practice =======================================
    # ==========================================================================
    while continueRoutine:
        # get current time
        t = PracticeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PracticeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame


        # *pdiagram* updates
        if pdiagram.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pdiagram.frameNStart = frameN  # exact frame index
            pdiagram.tStart = t  # local t and not account for scr refresh
            pdiagram.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pdiagram, 'tStartRefresh')  # time at next scr refresh
            pdiagram.setAutoDraw(False)
            pdiagram.draw()
        # *pbox0* updates
        for box in pboxes:
            if box.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                box.frameNStart = frameN  # exact frame index
                box.tStart = t  # local t and not account for scr refresh
                box.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(box, 'tStartRefresh')  # time at next scr refresh
                box.setAutoDraw(False)
                box.draw()


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
    practices.addData('pbox0.started', pboxes[0].tStartRefresh)
    practices.addData('pbox0.stopped', pboxes[0].tStopRefresh)
    practices.addData('pbox1.started', pboxes[1].tStartRefresh)
    practices.addData('pbox1.stopped', pboxes[1].tStopRefresh)
    practices.addData('pbox2.started', pboxes[2].tStartRefresh)
    practices.addData('pbox2.stopped', pboxes[2].tStopRefresh)
    practices.addData('pbox3.started', pboxes[3].tStartRefresh)
    practices.addData('pbox3.stopped', pboxes[3].tStopRefresh)
    practices.addData('pbox4.started', pboxes[4].tStartRefresh)
    practices.addData('pbox4.stopped', pboxes[4].tStopRefresh)
    practices.addData('pbox5.started', pboxes[5].tStartRefresh)
    practices.addData('pbox5.stopped', pboxes[5].tStopRefresh)
    # store data for practices (TrialHandler)
    x, y = pmouse.getPos()
    buttons = pmouse.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in pboxes:
            if obj.contains(pmouse):
                gotValidClick = True
                pmouse.clicked_pclicked.append(obj.pclicked)
    practices.addData('pmouse.x', x)
    practices.addData('pmouse.y', y)
    practices.addData('pmouse.leftButton', buttons[0])
    practices.addData('pmouse.midButton', buttons[1])
    practices.addData('pmouse.rightButton', buttons[2])
    if len(pmouse.clicked_pclicked):
        practices.addData('pmouse.clicked_pclicked', pmouse.clicked_pclicked[0])
    practices.addData('pmouse.started', pmouse.tStart)
    practices.addData('pmouse.stopped', pmouse.tStop)
    practices.addData('pdiagram.started', pdiagram.tStartRefresh)
    practices.addData('pdiagram.stopped', pdiagram.tStopRefresh)
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
    # setup some python lists for storing info about the tmouse
    tmouse.clicked_tclicked = []
    gotValidClick = False  # until a click is received
    tmouse.mouseClock.reset()
    # keep track of which components have finished
    TrialComponents = [tsound, tdiagram, tboxes[0], tboxes[1], tboxes[2], tboxes[3], tboxes[4], tboxes[5], tmouse]
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
        
        # *tdiagram* updates
        if tdiagram.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tdiagram.frameNStart = frameN  # exact frame index
            tdiagram.tStart = t  # local t and not account for scr refresh
            tdiagram.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tdiagram, 'tStartRefresh')  # time at next scr refresh
            tdiagram.setAutoDraw(True)


        for box in tboxes:
            if box.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                box.frameNStart = frameN  # exact frame index
                box.tStart = t  # local t and not account for scr refresh
                box.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(box, 'tStartRefresh')  # time at next scr refresh
                box.setAutoDraw(True)
        # *tmouse* updates
        if tmouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tmouse.frameNStart = frameN  # exact frame index
            tmouse.tStart = t  # local t and not account for scr refresh
            tmouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tmouse, 'tStartRefresh')  # time at next scr refresh
            tmouse.status = STARTED
            prevButtonState = tmouse.getPressed()  # if button is down already this ISN'T a new click
        if tmouse.status == STARTED:  # only update if started and not finished!
            buttons = tmouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in tboxes:
                        if obj.contains(tmouse):
                            gotValidClick = True
                            tmouse.clicked_tclicked.append(obj.tclicked)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
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
    trials.addData('tsound.started', tsound.tStartRefresh)
    trials.addData('tsound.stopped', tsound.tStopRefresh)
    trials.addData('tdiagram.started', tdiagram.tStartRefresh)
    trials.addData('tdiagram.stopped', tdiagram.tStopRefresh)
    trials.addData('box0.started', tboxes[0].tStartRefresh)
    trials.addData('box0.stopped', tboxes[0].tStopRefresh)
    trials.addData('box1.started', tboxes[1].tStartRefresh)
    trials.addData('box1.stopped', tboxes[1].tStopRefresh)
    trials.addData('box2.started', tboxes[2].tStartRefresh)
    trials.addData('box2.stopped', tboxes[2].tStopRefresh)
    trials.addData('box3.started', tboxes[3].tStartRefresh)
    trials.addData('box3.stopped', tboxes[3].tStopRefresh)
    trials.addData('box4.started', tboxes[4].tStartRefresh)
    trials.addData('box4.stopped', tboxes[4].tStopRefresh)
    trials.addData('box5.started', tboxes[5].tStartRefresh)
    trials.addData('box5.stopped', tboxes[5].tStopRefresh)
    # store data for trials (TrialHandler)
    x, y = tmouse.getPos()
    buttons = tmouse.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in pboxes:
            if obj.contains(tmouse):
                gotValidClick = True
                tmouse.clicked_tclicked.append(obj.tclicked)
    trials.addData('tmouse.x', x)
    trials.addData('tmouse.y', y)
    trials.addData('tmouse.leftButton', buttons[0])
    trials.addData('tmouse.midButton', buttons[1])
    trials.addData('tmouse.rightButton', buttons[2])
    if len(tmouse.clicked_tclicked):
        trials.addData('tmouse.clicked_tclicked', tmouse.clicked_tclicked[0])
    trials.addData('tmouse.started', tmouse.tStart)
    trials.addData('tmouse.stopped', tmouse.tStop)
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
    
    # *etext* updates
    if etext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        etext.frameNStart = frameN  # exact frame index
        etext.tStart = t  # local t and not account for scr refresh
        etext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(etext, 'tStartRefresh')  # time at next scr refresh
        etext.setAutoDraw(True)
    if etext.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > etext.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            etext.tStop = t  # not accounting for scr refresh
            etext.frameNStop = frameN  # exact frame index
            win.timeOnFlip(etext, 'tStopRefresh')  # time at next scr refresh
            etext.setAutoDraw(False)
    
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
thisExp.addData('etext.started', etext.tStartRefresh)
thisExp.addData('etext.stopped', etext.tStopRefresh)
# check responses
if econfirm.keys in ['', [], None]:  # No response was made
    econfirm.keys = None
thisExp.addData('econfirm.keys',econfirm.keys)
if econfirm.keys != None:  # we had a response
    thisExp.addData('econfirm.rt', econfirm.rt)
thisExp.addData('econfirm.started', econfirm.tStartRefresh)
thisExp.addData('econfirm.stopped', econfirm.tStopRefresh)
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
