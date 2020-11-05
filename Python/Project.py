#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.5),
    on November 05, 2020, at 15:24
If you publish work using this script the most relevant publication is:
    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y
"""

from __future__ import absolute_import, division
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
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
cfg = config
cfg.load()
# ==========================================================================
# ============================= Window =====================================
# ==========================================================================
win = visual.Window(
    size=cfg.getVal("winRes"), fullscr=True, screen=0,
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()
# ==========================================================================
# =========================== Instructions =================================
# ==========================================================================
# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
itext = visual.TextStim(win=win, name='itext', text='Instructions', font='Arial', pos=(0, 0), height=0.1,
                        wrapWidth=None, ori=0, color='white', colorSpace='rgb', opacity=1, languageStyle='LTR',
                        depth=0.0);
iconfirm = keyboard.Keyboard()
# Initialize components for Routine "Practice"
PracticeClock = core.Clock()
pbox0 = visual.Rect(win=win, name='pbox0', width=(0.5, 0.5)[0], height=(0.5, 0.5)[1], ori=0, pos=(0, 0),
                    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb', fillColor=[1,1,1], fillColorSpace='rgb',
                    opacity=1, depth=0.0, interpolate=True)
pbox1 = visual.Rect(
    win=win, name='pbox1',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
pbox2 = visual.Rect(
    win=win, name='pbox2',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
pbox3 = visual.Rect(
    win=win, name='pbox3',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
pbox4 = visual.Rect(
    win=win, name='pbox4',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
pbox5 = visual.Rect(
    win=win, name='pbox5',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
pmouse = event.Mouse(win=win)
x, y = [None, None]
pmouse.mouseClock = core.Clock()
pdiagram = visual.ImageStim(
    win=win,
    name='pdiagram', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)

# Initialize components for Routine "Trial"
TrialClock = core.Clock()
tsound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='tsound')
tsound.setVolume(1)
tdiagram = visual.ImageStim(
    win=win,
    name='tdiagram', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
box0 = visual.Rect(
    win=win, name='box0',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
box1 = visual.Rect(
    win=win, name='box1',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
box2 = visual.Rect(
    win=win, name='box2',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
box3 = visual.Rect(
    win=win, name='box3',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
box4 = visual.Rect(
    win=win, name='box4',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
box5 = visual.ShapeStim(
    win=win, name='box5',
    vertices=[[-(0.5, 0.5)[0]/2.0,-(0.5, 0.5)[1]/2.0], [+(0.5, 0.5)[0]/2.0,-(0.5, 0.5)[1]/2.0], [0,(0.5, 0.5)[1]/2.0]],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
tmouse = event.Mouse(win=win)
x, y = [None, None]
tmouse.mouseClock = core.Clock()

# Initialize components for Routine "Exit"
ExitClock = core.Clock()
etext = visual.TextStim(win=win, name='etext',
    text='Any text\n\nincluding line breaks',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
econfirm = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
iconfirm.keys = []
iconfirm.rt = []
_iconfirm_allKeys = []
# keep track of which components have finished
InstructionsComponents = [itext, iconfirm]
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

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *itext* updates
    if itext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        itext.frameNStart = frameN  # exact frame index
        itext.tStart = t  # local t and not account for scr refresh
        itext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(itext, 'tStartRefresh')  # time at next scr refresh
        itext.setAutoDraw(True)
    if itext.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > itext.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            itext.tStop = t  # not accounting for scr refresh
            itext.frameNStop = frameN  # exact frame index
            win.timeOnFlip(itext, 'tStopRefresh')  # time at next scr refresh
            itext.setAutoDraw(False)
    
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

# -------Ending Routine "Instructions"-------
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
    
    # ------Prepare to start Routine "Practice"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the pmouse
    pmouse.clicked_pclicked = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    PracticeComponents = [pbox0, pbox1, pbox2, pbox3, pbox4, pbox5, pmouse, pdiagram]
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
    
    # -------Run Routine "Practice"-------
    while continueRoutine:
        # get current time
        t = PracticeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PracticeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pbox0* updates
        if pbox0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pbox0.frameNStart = frameN  # exact frame index
            pbox0.tStart = t  # local t and not account for scr refresh
            pbox0.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pbox0, 'tStartRefresh')  # time at next scr refresh
            pbox0.setAutoDraw(True)
        
        # *pbox1* updates
        if pbox1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pbox1.frameNStart = frameN  # exact frame index
            pbox1.tStart = t  # local t and not account for scr refresh
            pbox1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pbox1, 'tStartRefresh')  # time at next scr refresh
            pbox1.setAutoDraw(True)
        
        # *pbox2* updates
        if pbox2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pbox2.frameNStart = frameN  # exact frame index
            pbox2.tStart = t  # local t and not account for scr refresh
            pbox2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pbox2, 'tStartRefresh')  # time at next scr refresh
            pbox2.setAutoDraw(True)
        
        # *pbox3* updates
        if pbox3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pbox3.frameNStart = frameN  # exact frame index
            pbox3.tStart = t  # local t and not account for scr refresh
            pbox3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pbox3, 'tStartRefresh')  # time at next scr refresh
            pbox3.setAutoDraw(True)
        
        # *pbox4* updates
        if pbox4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pbox4.frameNStart = frameN  # exact frame index
            pbox4.tStart = t  # local t and not account for scr refresh
            pbox4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pbox4, 'tStartRefresh')  # time at next scr refresh
            pbox4.setAutoDraw(True)
        
        # *pbox5* updates
        if pbox5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pbox5.frameNStart = frameN  # exact frame index
            pbox5.tStart = t  # local t and not account for scr refresh
            pbox5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pbox5, 'tStartRefresh')  # time at next scr refresh
            pbox5.setAutoDraw(True)
        
        # *pdiagram* updates
        if pdiagram.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pdiagram.frameNStart = frameN  # exact frame index
            pdiagram.tStart = t  # local t and not account for scr refresh
            pdiagram.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pdiagram, 'tStartRefresh')  # time at next scr refresh
            pdiagram.setAutoDraw(True)
        
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
    
    # -------Ending Routine "Practice"-------
    for thisComponent in PracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practices.addData('pbox0.started', pbox0.tStartRefresh)
    practices.addData('pbox0.stopped', pbox0.tStopRefresh)
    practices.addData('pbox1.started', pbox1.tStartRefresh)
    practices.addData('pbox1.stopped', pbox1.tStopRefresh)
    practices.addData('pbox2.started', pbox2.tStartRefresh)
    practices.addData('pbox2.stopped', pbox2.tStopRefresh)
    practices.addData('pbox3.started', pbox3.tStartRefresh)
    practices.addData('pbox3.stopped', pbox3.tStopRefresh)
    practices.addData('pbox4.started', pbox4.tStartRefresh)
    practices.addData('pbox4.stopped', pbox4.tStopRefresh)
    practices.addData('pbox5.started', pbox5.tStartRefresh)
    practices.addData('pbox5.stopped', pbox5.tStopRefresh)
    # store data for practices (TrialHandler)
    x, y = pmouse.getPos()
    buttons = pmouse.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [pbox0,pbox1,pbox2,pbox3,pbox4,pbox5]:
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
    
    # ------Prepare to start Routine "Trial"-------
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
    TrialComponents = [tsound, tdiagram, box0, box1, box2, box3, box4, box5, tmouse]
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
    
    # -------Run Routine "Trial"-------
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
        
        # *box0* updates
        if box0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            box0.frameNStart = frameN  # exact frame index
            box0.tStart = t  # local t and not account for scr refresh
            box0.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(box0, 'tStartRefresh')  # time at next scr refresh
            box0.setAutoDraw(True)
        
        # *box1* updates
        if box1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            box1.frameNStart = frameN  # exact frame index
            box1.tStart = t  # local t and not account for scr refresh
            box1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(box1, 'tStartRefresh')  # time at next scr refresh
            box1.setAutoDraw(True)
        
        # *box2* updates
        if box2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            box2.frameNStart = frameN  # exact frame index
            box2.tStart = t  # local t and not account for scr refresh
            box2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(box2, 'tStartRefresh')  # time at next scr refresh
            box2.setAutoDraw(True)
        
        # *box3* updates
        if box3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            box3.frameNStart = frameN  # exact frame index
            box3.tStart = t  # local t and not account for scr refresh
            box3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(box3, 'tStartRefresh')  # time at next scr refresh
            box3.setAutoDraw(True)
        
        # *box4* updates
        if box4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            box4.frameNStart = frameN  # exact frame index
            box4.tStart = t  # local t and not account for scr refresh
            box4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(box4, 'tStartRefresh')  # time at next scr refresh
            box4.setAutoDraw(True)
        
        # *box5* updates
        if box5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            box5.frameNStart = frameN  # exact frame index
            box5.tStart = t  # local t and not account for scr refresh
            box5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(box5, 'tStartRefresh')  # time at next scr refresh
            box5.setAutoDraw(True)
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
                    for obj in [box0,box1,box2,box3,box4,box5]:
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
    
    # -------Ending Routine "Trial"-------
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    tsound.stop()  # ensure sound has stopped at end of routine
    trials.addData('tsound.started', tsound.tStartRefresh)
    trials.addData('tsound.stopped', tsound.tStopRefresh)
    trials.addData('tdiagram.started', tdiagram.tStartRefresh)
    trials.addData('tdiagram.stopped', tdiagram.tStopRefresh)
    trials.addData('box0.started', box0.tStartRefresh)
    trials.addData('box0.stopped', box0.tStopRefresh)
    trials.addData('box1.started', box1.tStartRefresh)
    trials.addData('box1.stopped', box1.tStopRefresh)
    trials.addData('box2.started', box2.tStartRefresh)
    trials.addData('box2.stopped', box2.tStopRefresh)
    trials.addData('box3.started', box3.tStartRefresh)
    trials.addData('box3.stopped', box3.tStopRefresh)
    trials.addData('box4.started', box4.tStartRefresh)
    trials.addData('box4.stopped', box4.tStopRefresh)
    trials.addData('box5.started', box5.tStartRefresh)
    trials.addData('box5.stopped', box5.tStopRefresh)
    # store data for trials (TrialHandler)
    x, y = tmouse.getPos()
    buttons = tmouse.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        for obj in [box0,box1,box2,box3,box4,box5]:
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


# ------Prepare to start Routine "Exit"-------
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

# -------Run Routine "Exit"-------
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

# -------Ending Routine "Exit"-------
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
