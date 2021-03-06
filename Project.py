﻿# ==========================================================================
# By: Benjamin Wilcox (bwilcox@ltu.edu),
# CRE Student Research Project- 1/29/2021
# ==========================================================================
# Description:
# Handles primary execution of experiment and base logic for phases and
# creation for ui and other project components
# ==========================================================================
# ==============================================================================================
# Psychopy Imports: Psychopy generated imports
# ==============================================================================================
from __future__ import absolute_import, division
from psychopy import sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, FINISHED)
import os  # handy system and path functions
from psychopy.hardware import keyboard
from psychopy.sound.backend_pygame import SoundPygame
# ==============================================================================================
# Imports: custom imports
# ==============================================================================================
from Config import Config as Config
from StateMachine import StateMachine as StateMachine
from UISettings import GUIDraw as GUIDraw
from KeyTracker import KeyTracker as KeyTracker
from UISettings import UIComponents as UIComponents
from PracticeHandler import PracticeHandler as PracticeHandler
from TrainingHandler import TrainingHandler as TrainingHandler
from TrialHandler import TrialHandler as TrialHandler
from LatinSquare import LatinSquareGenerator as LatinSquareGenerator
# ==============================================================================================
# Config Files: load config files and helper classes
# ==============================================================================================
cfg = Config(configFile="cfg.json")
cfg.load()
pos = Config(configFile="positions.json")
pos.load()
colors = Config(configFile="colors.json")
colors.load()
sm = StateMachine()
guid = GUIDraw(pos, colors, cfg)
# ==============================================================================================
# Project Config: Psychopy generated config
# ==============================================================================================
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2020.2.5'
expName = cfg.getVal("projectName")
expInfo = {'participant': '', 'session': '001'}
if cfg.getVal("devMode"):
    expInfo = {'participant': '001', 'session': '001'}
else:
    dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
    if not dlg.OK:
        core.quit()  # user pressed cancel
if expInfo["participant"] == "":
    expInfo["participant"] = 0
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion
# ==============================================================================================
# Sound: Selecting sound type and getting dir and file list
# ==============================================================================================
assetDir = os.path.join(os.getcwd(), cfg.getVal("dir_assets"))
soundStimDir = os.path.join(assetDir, cfg.getVal("dir_sound"))
musicArr = cfg.getVal("dir_music")
squareRes = int(LatinSquareGenerator(len(musicArr), int(expInfo["participant"])))
logging.exp(f"Selected music type {musicArr[squareRes]}")
print(f"Selected music type {musicArr[squareRes]}")
musicStimDir = os.path.join(soundStimDir, musicArr[squareRes])
musicStimFiles = os.listdir(musicStimDir)
# ==============================================================================================
# Negative Selection: Selecting negative amount in sm
# ==============================================================================================
squareNegRes = int(LatinSquareGenerator(len(sm.negativeScores), int(expInfo["participant"])))
sm.negativeIndex = squareNegRes
logging.exp(f"Selected negative amount {sm.negativeScores[squareNegRes]}")
print(f"Selected negative amount {sm.negativeScores[squareNegRes]}")
# ==============================================================================================
# Data: Psychopy generated for creating data files
# ==============================================================================================
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
thisExp.addData('date', expInfo['date'])
thisExp.addData('participant', expInfo['participant'])
thisExp.addData('negative', sm.negativeScores[squareNegRes])
thisExp.addData('sound', musicArr[squareRes])
# ==============================================================================================
# Window: Psychopy generated for creating window
# ==============================================================================================
win = visual.Window(size=cfg.getVal("winRes"), fullscr=True, screen=0, winType='pyglet', allowGUI=False,
                    allowStencil=False,monitor='testMonitor', color=[0,0,0], colorSpace='rgb', blendMode='avg',
                    useFBO=True, units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# ==============================================================================================
# Config 2: set up keys and other components
# ==============================================================================================
defaultKeyboard = keyboard.Keyboard()
spaceKey = KeyTracker("space", defaultKeyboard)
uKey = KeyTracker("u", defaultKeyboard)
iKey = KeyTracker("i", defaultKeyboard)
comp = UIComponents(win, cfg.getVal("winRes"))
# ==============================================================================================
# Instruction Objects: Creation of Instruction Objects and general use Header, Body
# ==============================================================================================
InstructionsClock = core.Clock()
# create components
header = comp.createText(name='header', text='Instructions', pos=guid.cfgTRes("i_header_pos"), height=80, color=colors.getVal("i_text"))
header.wrapWidth = 1000
body = comp.createText(name='body', text=guid.instructionsText[0], pos=guid.cfgTRes("i_body_pos"),
                       color=colors.getVal("i_text"), height=40)
continueText = comp.createText(name='continueText', text=guid.continueText, pos=guid.cfgTRes("i_continue_pos"), color=colors.getVal("i_text"))
# set word wrap width
body.wrapWidth = guid.cfgTRes("i_wrap")[0]
continueText.wrapWidth = guid.cfgTRes("i_wrap")[0]
# turn off auto draw
header.setAutoDraw(False)
header.setAutoLog(False)
body.setAutoDraw(False)
body.setAutoLog(False)
continueText.setAutoDraw(False)
# ==============================================================================================
# Practice Objects: Creation of Practice Objects and general use mini-game ui components
# ==============================================================================================
PracticeClock = core.Clock()
numBoxes = 6
smBoxes = []
smBoxText = []
# create ui components
for i in range(numBoxes):
    smBoxes.append(comp.createBox(name="pbox" + str(i), size=guid.cfgTRes("box_size"), pos=guid.getBoxPos(i),
                                  lcolor=guid.c("box_line"), fcolor=guid.c("box")))
    smBoxText.append(comp.createText(name='smBoxText', text=guid.stateMoves[i], pos=guid.getMovePos(guid.getBoxPos(i)),
                                     color=guid.c("control_text"), height=25))
    smBoxes[i].setAutoDraw(False)
    smBoxText[i].setAutoDraw(False)
    smBoxes[i].setAutoLog(False)
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
# ==============================================================================================
# Trial Objects: Creation of Trail Objects and sounds
# ==============================================================================================
TrialClock = core.Clock()
pyGamSound = SoundPygame(value='A')
# ==============================================================================================
# Exit Objects: Creation of Exit Objects
# ==============================================================================================
ExitClock = core.Clock()
# ==============================================================================================
# Timers: Create some handy timers
# ==============================================================================================
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine
# ==============================================================================================
# Prepare Instructions: Set up Instructions
# ==============================================================================================
instructionsIndex = 0
continueRoutine = not cfg.getVal("skip_instructions")
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
# config ui elements
header.setText(cfg.getVal("instructions_header"))
header.setColor(guid.c("general_text"))
body.setColor(guid.c("general_text"))
# ==============================================================================================
# Run Instructions: Loop for running instructions phase
# ==============================================================================================
while continueRoutine:
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
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    if not continueRoutine:
        break
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
# ==============================================================================================
# End Instructions: Wrap up and add some data
# ==============================================================================================
thisExp.addData('Iphase end', globalClock.getTime())
logging.exp(f"Iphase end {globalClock.getTime()}")
# check responses
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# ==============================================================================================
# Prepare Practice: Set up variables for practice phase
# ==============================================================================================
practiceHandler = PracticeHandler(cfg)
continueRoutine = not cfg.getVal("skip_practice")
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
# set up text
header.setText(cfg.getVal("practice_header"))
body.setText(cfg.getVal("practice_text")[0])
# ==============================================================================================
# Run Practice: Loop for practice logic and rendering, uses PracticeHandler for assistance with logic
# ==============================================================================================
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
    practiceHandler.update(uKey, iKey, spaceKey, sm)
    body.setText(practiceHandler.getPhaseText(sm))
    if uKey.getKeyUp():
        sm.moveCircle()
    if iKey.getKeyUp():
        sm.moveAcross()
    # -------------prepare draw -----------------
    for box in smBoxes:
        box.setFillColor(guid.c("box"))
        box.setLineColor(guid.c("box_line"))
    smBoxes[sm.getCurrentState()].setFillColor(guid.c("box_selected"))
    if practiceHandler.isPhases(["1moves", "2moves"]):
        smBoxes[sm.practiceTargetState].setLineColor(guid.c("box_target"))
    # ----------------draw-----------------------
    uBox.draw()
    iBox.draw()
    iText.draw()
    uText.draw()
    body.draw()
    header.draw()
    if sm.drawSM:
        for box in smBoxes:
            box.draw()
        for t in smBoxText:
            t.draw()
    # ---------------- checks ----------------
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
# ==============================================================================================
# End Practice: Wrap up
# ==============================================================================================
# the Routine "Practice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
thisExp.nextEntry()
thisExp.addData('Practice end', globalClock.getTime())
logging.exp(f"Practice end {globalClock.getTime()}")
# ==============================================================================================
# Prepare Training: Set up training phase
# ==============================================================================================
trainingHandler = TrainingHandler(cfg)
continueRoutine = not (cfg.getVal("skip_training1") and cfg.getVal("skip_training2"))
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
# set up state machine
smState = sm.getCurrentState()
smBoxes[smState].setFillColor((guid.c("box_selected")))
# set up text
header.setText(cfg.getVal("training_header"))
body.setText(cfg.getVal("practice_text")[0])
# ==============================================================================================
# Run Training: loop for training logic and rendering, uses TrainingHandler for assistance with logic
# ==============================================================================================
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
    for box in smBoxes:
        box.setFillColor(guid.c("box"))
        box.setLineColor(guid.c("box_line"))
    smBoxes[sm.getCurrentState()].setFillColor(guid.c("box_selected"))
    if trainingHandler.isPhase("phaseOne") or trainingHandler.isPhase("phaseTwo"):
        smBoxes[sm.practiceTargetState].setLineColor(guid.c("box_target"))
    # ----------------draw-----------------------
    uBox.draw()
    iBox.draw()
    iText.draw()
    uText.draw()
    body.draw()
    header.draw()
    if sm.drawSM:
        for box in smBoxes:
            box.draw()
        for t in smBoxText:
            t.draw()
    # ---------------- checks ----------------
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
# ==============================================================================================
# End Training: wrap up training
# ==============================================================================================
# the Routine "Practice" was not non-slip safe, so reset the non-slip timer
trainingHandler.end()
routineTimer.reset()
thisExp.nextEntry()
thisExp.addData('Training end', globalClock.getTime())
logging.exp(f"Training end {globalClock.getTime()}")
# ==============================================================================================
# Trial Loop: trial has multiple phases and needs to fully reset between phases which requires
# running the setup and end portions multiple times, uses TrialHandler for assistance with logic
# ==============================================================================================
musicIndex = 0
for thisTrial in range(cfg.getVal("trial_exp_blocks")):
    # ==============================================================================================
    # Prepare Trial: setup trial
    # ==============================================================================================
    logging.exp(f"Trial new block: {thisTrial}")
    trialHandler = TrialHandler(cfg, thisTrial)
    header.setText(trialHandler.getPhaseHeader())
    continueRoutine = not cfg.getVal("skip_trial")
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    # sound setup
    soundDir = os.path.join(musicStimDir, musicStimFiles[musicIndex])
    pyGamSound = SoundPygame(value=soundDir)
    songTimer = core.CountdownTimer(pyGamSound.getDuration())
    musicPlaying = False
    # ==============================================================================================
    # Run Trial: loop for trial logic and rendering
    # ==============================================================================================
    while continueRoutine:
        # -----------get current time------------
        t = TrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # ---------------sound-------------------
        if trialHandler.welcomedMsg and not musicPlaying:
            pyGamSound.play()
            musicPlaying = True
        if musicPlaying and trialHandler.complete:
            pyGamSound.stop()
            musicPlaying = False
        if songTimer.getTime() <= 0:
            musicIndex += 1
            if musicIndex >= len(musicStimFiles):
                musicIndex = 0
            soundDir = os.path.join(musicStimDir, musicStimFiles[musicIndex])
            pyGamSound.stop()
            pyGamSound = SoundPygame(value=soundDir)
            songTimer = core.CountdownTimer(pyGamSound.getDuration())
            pyGamSound.play()
        # --------------updates--------------------
        uKey.update()
        iKey.update()
        spaceKey.update()
        trialHandler.update(uKey, iKey, spaceKey, sm, thisExp)
        body.setText(trialHandler.getPhaseText(sm))
        header.setText(trialHandler.getPhaseHeader())
        if uKey.getKeyUp():
            sm.moveCircle()
        if iKey.getKeyUp():
            sm.moveAcross()
        # -------------prepare draw -----------------
        for box in smBoxes:
            box.setFillColor(guid.c("box"))
            box.setLineColor(guid.c("box_line"))
        smBoxes[sm.getCurrentState()].setFillColor(guid.c("box_selected"))
        # ----------------draw-----------------------
        uBox.draw()
        iBox.draw()
        iText.draw()
        uText.draw()
        body.draw()
        header.draw()
        if sm.drawSM:
            for box in smBoxes:
                box.draw()
            for t in smBoxText:
                t.draw()
        # --------------checks-----------------------
        if trialHandler.complete:
            continueRoutine = False
            pyGamSound.stop()
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    # ==============================================================================================
    # End Trial: wrap up trial phase and prepare for next trial or end phase
    # ==============================================================================================
    pyGamSound.stop()
    musicPlaying = False  # ensure sound has stopped at end of routine
    # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    thisExp.addData('Trial end', globalClock.getTime())
    logging.exp(f"Trial end {globalClock.getTime()}")
# ==============================================================================================
# Prepare Exit: set up exit phase, very similar to instructions phase
# ==============================================================================================
continueRoutine = not cfg.getVal("skip_exit")
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ExitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
# set stuff
header.setText(cfg.getVal("exit_header"))
exitIndex = 0
# ==============================================================================================
# Run Exit: run exit phase, very similar to instructions phase
# ==============================================================================================
while continueRoutine:
    # ----------- get current time----------------
    t = ExitClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ExitClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # ------------------draw----------------------
    body.setText(guid.exitText[exitIndex])
    header.draw()
    body.draw()
    continueText.draw()
    # -------------- key checks ------------------
    spaceKey.update()
    if spaceKey.getKeyUp():
        exitIndex += 1
    # -------------- wrap up ------------------
    if exitIndex >= len(guid.exitText):
        continueRoutine = False
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
# ==============================================================================================
# End Exit: finish up phase
# ==============================================================================================
thisExp.nextEntry()
# the Routine "Exit" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
thisExp.addData('Exit end', globalClock.getTime())
logging.exp(f"Exit end {globalClock.getTime()}")
# ==============================================================================================
# End Program: wrap up the entire program
# ==============================================================================================
# Flip one final time so any remaining win.callOnFlip() and win.timeOnFlip() tasks get executed before quitting
win.flip()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
