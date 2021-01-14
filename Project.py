#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://run.pavlovia.org/fdelogu/covid_game/html/?fbclid=IwAR0NzZPE0JAG2ROZsL8yE1dIFH2Glm7-sMfZWgmVRpgUdDxirExBeZQ-Y_c
# ==========================================================================
# ============================= Imports ====================================
# ==========================================================================
from __future__ import absolute_import, division
from psychopy import sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, FINISHED)
import os  # handy system and path functions
from psychopy.hardware import keyboard
# ==========================================================================
# ============================= Config File ================================
# ==========================================================================
from Config import Config as Config
cfg = Config(configFile="cfg.json")
cfg.load()
pos = Config(configFile="positions.json")
pos.load()
colors = Config(configFile="colors.json")
colors.load()
diaDir = os.path.join(cfg.getVal("assetDir"), "Diagrams//ArrowsNumbered.png")
from StateMachine import StateMachine as StateMachine
from UISettings import GUIDraw as GUIDraw

sm = StateMachine()
guid = GUIDraw(pos, colors, cfg)
# ==========================================================================
# ==========================Project Config =================================
# ==========================================================================
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2020.2.5'
expName = cfg.getVal("projectName")
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
# ==========================================================================
# =============================== Config 2 =================================
# ==========================================================================
# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

from KeyTracker import KeyTracker as KeyTracker
spaceKey = KeyTracker("space", defaultKeyboard)
uKey = KeyTracker("u", defaultKeyboard)
iKey = KeyTracker("i", defaultKeyboard)

from UISettings import UIComponents as UIComponents
comp = UIComponents(win, cfg.getVal("winRes"))
# ==========================================================================
# =========================== Instruction Objs =============================
# ==========================================================================
InstructionsClock = core.Clock()
# create components
header = comp.createText(name='header', text='Instructions', pos=guid.cfgTRes("i_header_pos"), height=100, color=colors.getVal("i_text"))
body = comp.createText(name='body', text=guid.instructionsText[0], pos=guid.cfgTRes("i_body_pos"),
                       color=colors.getVal("i_text"), height=40)
continueText = comp.createText(name='continueText', text=guid.continueText, pos=guid.cfgTRes("i_continue_pos"), color=colors.getVal("i_text"))
# set word wrap width
body.wrapWidth = guid.cfgTRes("i_wrap")[0]
continueText.wrapWidth = guid.cfgTRes("i_wrap")[0]
# turn off auto draw
header.setAutoDraw(False)
body.setAutoDraw(False)
body.setAutoLog(False)
continueText.setAutoDraw(False)
# ==========================================================================
# ============================== Practice Objs =============================
# ==========================================================================
PracticeClock = core.Clock()
numBoxes = 6
boxes = []
pBoxText = []
# create ui components
for i in range(numBoxes):
    boxes.append(comp.createBox(name="pbox" + str(i), size=guid.cfgTRes("box_size"), pos=guid.getBoxPos(i),
                                lcolor=guid.c("box_line"), fcolor=guid.c("box")))
    pBoxText.append(comp.createText(name='pBoxText', text=guid.stateMoves[i], pos=guid.getMovePos(guid.getBoxPos(i)),
                                    color=guid.c("control_text"), height=25))
    boxes[i].setAutoDraw(False)
    pBoxText[i].setAutoDraw(False)
    boxes[i].setAutoLog(False)
uBox = comp.createBox(name='ubox', size=guid.cfgTRes("control_size"), pos=guid.getControlPos(-1),
                      lcolor=guid.c("control_line"), fcolor=guid.c("control_box"))
iBox = comp.createBox(name='ibox', size=guid.cfgTRes("control_size"), pos=guid.getControlPos(+1),
                      lcolor=guid.c("control_line"), fcolor=guid.c("control_box"))
uText = comp.createText(name='utext', text='U', pos=guid.getControlPos(-1), height=50,color=guid.c("control_text"))
iText = comp.createText(name='itext', text='I', pos=guid.getControlPos(+1), height=50,color=guid.c("control_text"))
# set auto draw to false
uBox.setAutoDraw(False)
iBox.setAutoDraw(False)
uText.setAutoDraw(False)
iText.setAutoDraw(False)
# ==========================================================================
# ================================ Trial Objs ==============================
# ==========================================================================
TrialClock = core.Clock()
# temporary sound 'A'
tsound = sound.Sound('A', secs=-1, stereo=True, hamming=True, name='tsound')
tbeep = sound.Sound('A', secs=-1, stereo=True, hamming=True, name='tbeep')
tsound.setVolume(1)
tbeep.setVolume(1)
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
instructionsIndex = 0
continueRoutine = True
# keep track of which components have finished
InstructionsComponents = [body, continueText, header]
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
# ==========================================================================
# ========================= Run Instructions ===============================
# ==========================================================================
while continueRoutine:
    if cfg.getVal("skip_instructions"):
        continueRoutine = False;
    # -------------get current time---------------
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # ------------------draw----------------------
    header.draw()
    body.draw()
    continueText.draw()
    # -------------- key checks ------------------
    spaceKey.update()
    if spaceKey.getKeyUp():
        instructionsIndex += 1
        if instructionsIndex >= len(guid.instructionsText):
            continueRoutine = False
        else:
            body.setText(guid.instructionsText[instructionsIndex])
    # -------------- Wrap Up -------------------------
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
thisExp.addData('Iphase end', globalClock.getTime())
# check responses
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# ==========================================================================
# ===================== Prepare Practice ===================================
# ==========================================================================
from PracticeHandler import PracticeHandler as PracticeHandler
practiceHandler = PracticeHandler(cfg)
# end phase variables
continueRoutine = True
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
# set up state machine
smState = sm.getCurrentState()
boxes[smState].setFillColor((guid.c("box_selected")))
# set up text
header.setText('Practice')
body.setText(cfg.getVal("practice_text")[0])
header.setColor(guid.c("general_text"))
body.setColor(guid.c("general_text"))

# ==========================================================================
# ===================== Run Practice =======================================
# ==========================================================================
while continueRoutine:
    if cfg.getVal("skip_practice"):
        continueRoutine = False
    # -----------get current time------------
    t = PracticeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PracticeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # --------------updates--------------------
    uKey.update()
    iKey.update()
    spaceKey.update()
    practiceHandler.update(uKey, iKey, spaceKey, sm)
    body.setText(practiceHandler.getPhaseText(sm))
    if uKey.getKeyUp():
        sm.moveCircle()
    if iKey.getKeyUp():
        sm.moveAcross()
    # -------------prepare draw -----------------
    for box in boxes:
        box.setFillColor(guid.c("box"))
        box.setLineColor(guid.c("box_line"))
    boxes[sm.getCurrentState()].setFillColor(guid.c("box_selected"))
    if practiceHandler.isPhases(["1moves", "2moves"]):
        boxes[sm.practiceTargetState].setLineColor(guid.c("box_target"))
    # ----------------draw-----------------------
    uBox.draw()
    iBox.draw()
    iText.draw()
    uText.draw()
    body.draw()
    header.draw()
    for box in boxes:
        box.draw()
    for t in pBoxText:
        t.draw()
    # =================== key checks ===================
    if practiceHandler.complete and spaceKey.getKeyUp():
        continueRoutine = False
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
# ==========================================================================
# ========================== End Practice ==================================
# ==========================================================================
# the Routine "Practice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
thisExp.nextEntry()
# ==========================================================================
# ===================== Prepare Training ===================================
# ==========================================================================
from TrainingHandler import TrainingHandler as TrainingHandler
trainingHandler = TrainingHandler(cfg)
# end phase variables
continueRoutine = True
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
# set up state machine
smState = sm.getCurrentState()
boxes[smState].setFillColor((guid.c("box_selected")))
# set up text
header.setText('Training')
body.setText(cfg.getVal("practice_text")[0])
header.setColor(guid.c("general_text"))
body.setColor(guid.c("general_text"))
# ==========================================================================
# ===================== Run Training =======================================
# ==========================================================================
while continueRoutine:
    # -----------get current time------------
    t = PracticeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PracticeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # --------------updates--------------------
    uKey.update()
    iKey.update()
    spaceKey.update()
    trainingHandler.update(uKey, iKey, spaceKey, sm)
    body.setText(trainingHandler.getPhaseText(sm))
    if uKey.getKeyUp():
        sm.moveCircle()
    if iKey.getKeyUp():
        sm.moveAcross()
    # -------------prepare draw -----------------
    for box in boxes:
        box.setFillColor(guid.c("box"))
        box.setLineColor(guid.c("box_line"))
    boxes[sm.getCurrentState()].setFillColor(guid.c("box_selected"))
    if trainingHandler.isPhase("phaseOne") or trainingHandler.isPhase("phaseTwo"):
        boxes[sm.practiceTargetState].setLineColor(guid.c("box_target"))
    # ----------------draw-----------------------
    uBox.draw()
    iBox.draw()
    iText.draw()
    uText.draw()
    body.draw()
    header.draw()
    for box in boxes:
        box.draw()
    for t in pBoxText:
        t.draw()
    # =================== key checks ===================
    if trainingHandler.complete and spaceKey.getKeyUp():
        continueRoutine = False
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
# ==========================================================================
# ========================== End Training ==================================
# ==========================================================================
# the Routine "Practice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
thisExp.nextEntry()
# ==========================================================================
# ========================== Trial Loop ====================================
# ==========================================================================
from TrialHandler import TrialHandler as TrialHandler
for thisTrial in range(cfg.getVal("trial_exp_blocks")):
    logging.exp(f"Trial new block: {thisTrial}")
    trialHandler = TrialHandler(cfg, thisTrial)
    # ==========================================================================
    # ============================ Prepare Trial ===============================
    # ==========================================================================
    continueRoutine = True
    # update component parameters for each repeat
    tsound.setSound('A', hamming=True)
    tsound.setVolume(1, log=False)
    TrialComponents = [tsound]
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
        # -----------get current time------------
        t = TrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # ---------------sound-------------------
        if tsound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tsound.frameNStart = frameN  # exact frame index
            tsound.tStart = t  # local t and not account for scr refresh
            tsound.tStartRefresh = tThisFlipGlobal  # on global time
            tsound.play(when=win)  # sync with win flip
        # --------------updates--------------------
        uKey.update()
        iKey.update()
        spaceKey.update()
        trialHandler.update(uKey, iKey, spaceKey, sm)
        body.setText(trialHandler.getPhaseText(sm))
        if uKey.getKeyUp():
            sm.moveCircle()
        if iKey.getKeyUp():
            sm.moveAcross()
        # -------------prepare draw -----------------
        for box in boxes:
            box.setFillColor(guid.c("box"))
            box.setLineColor(guid.c("box_line"))
        boxes[sm.getCurrentState()].setFillColor(guid.c("box_selected"))
        # ----------------draw-----------------------
        uBox.draw()
        iBox.draw()
        iText.draw()
        uText.draw()
        body.draw()
        header.draw()
        for box in boxes:
            if sm.drawSM:
                box.draw()
        for t in pBoxText:
            if sm.drawSM:
                t.draw()
        # --------------key checks-----------------------
        if trialHandler.complete and spaceKey.getKeyUp():
            continueRoutine = False
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
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
    tbeep.stop()
    # store data for trials (TrialHandler)

    # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
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
