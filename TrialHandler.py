# ==========================================================================
# By: Benjamin Wilcox (bwilcox@ltu.edu),
# CRE Student Research Project- 1/29/2021
# ==========================================================================
# Description:
# Handles execution of logic for the trial phase
# ==========================================================================
from psychopy.data import ExperimentHandler

import Config as Config
import KeyTracker
from StateMachine import StateMachine as StateMachine
from psychopy import logging, core
import random


class TrialHandler:
    # cfg items
    instructions = ""
    instructionsBlock = ""
    musicInBlock = [1, 2]
    instructionsHeader = ""
    header = ""
    showBlock = True
    episodes = 25
    smMoves = [2, 8]
    episodeEndStr = ""
    movesLeftStr = ""
    blocks = 2
    # other cfg
    trialNum = 0
    episodeNum = 0
    # phase stuff
    firstFrame = True
    welcomedMsg = False
    endEpisode = False
    complete = False
    episodeTimer = None
    TrialScores = []
    TrialTimes = []

    # =====================================================================================
    # init: load cfg values
    # =====================================================================================
    def __init__(self, cfg: Config, trialNum: int):
        self.trialNum  = trialNum
        print(f"Trial init called phase{self.trialNum}")
        logging.exp(f"Trial init phase{self.trialNum}")
        self.instructions = cfg.getVal("trial_instructions")
        self.instructionsBlock = cfg.getVal("trial_instructions_block")
        self.musicInBlock = cfg.getVal("trial_music_in_block")
        self.instructionsHeader = cfg.getVal("trial_header_instructions")
        self.header = cfg.getVal("trial_header")
        self.showBlock = cfg.getVal("trial_header_show_block")
        self.headerBlock = cfg.getVal("trial_header_block")
        self.episodes = cfg.getVal("trial_exp_episodes")
        self.smMoves = cfg.getVal("trial_sm_moves")
        self.episodeEndStr = cfg.getVal("trial_episode_end")
        self.movesLeftStr = cfg.getVal("trial_moves_left")
        self.blocks = cfg.getVal("trial_exp_blocks")
        logging.exp(f"Trial cfg loaded")
        self.TrialTimes = []
        self.TrialScores = []

    # =====================================================================================
    # update: called in main loop once per frame, handles updating of logic
    # =====================================================================================
    def update(self, uKey: KeyTracker, iKey: KeyTracker, spaceKey: KeyTracker, sm: StateMachine, thisExp: ExperimentHandler):
        if self.firstFrame:
            logging.exp(f"Trial first frame")
            sm.lock()
            sm.dontDrawSM()
            self.firstFrame = False
        if not self.welcomedMsg and spaceKey.getKeyUp():
            logging.exp(f"Trial user confirmed welcome, begin episode: {self.episodeNum}")
            self.welcomedMsg = True
            self.resetSM(sm)
            sm.unlock()
            sm.doDrawSM()
            self.episodeTimer = core.Clock()
        if self.welcomedMsg and not self.endEpisode:
            if sm.movesLeft == 0:
                logging.exp(f"Trial user finished episode")
                self.TrialScores.append(sm.totalScore)
                self.TrialTimes.append(self.episodeTimer.getTime())
                self.endEpisode = True
                sm.dontDrawSM()
                sm.lock()
        if self.endEpisode and spaceKey.getKeyUp():
            self.endEpisode = False
            self.episodeNum += 1
            logging.exp(f"Trial user confirmed end episode, begin episode: {self.episodeNum}")
            self.episodeTimer = core.Clock()
            self.resetSM(sm)
            sm.unlock()
            sm.doDrawSM()
        if not self.complete and self.episodes <= self.episodeNum:
            self.complete = True
            thisExp.addData('Trial Scores', self.TrialScores)
            thisExp.addData('Trial Times', self.TrialTimes)
            self.TrialTimes = []
            self.TrialScores = []

    # =====================================================================================
    # getPhaseText: returns proper body for current phase
    # =====================================================================================
    def getPhaseText(self, sm: StateMachine):
        if not self.welcomedMsg:
            if self.trialNum == 0:
                return self.instructions
            else:
                return self.instructionsBlock
        if self.endEpisode:
            return str(self.episodeEndStr).format(episode=self.episodeNum + 1, totalEpisode=self.episodes, score=sm.totalScore)
        return str(self.movesLeftStr).format(movesLeft=sm.movesLeft)

    # =====================================================================================
    # getPhaseHeader: returns proper header for current phase
    # =====================================================================================
    def getPhaseHeader(self):
        if not self.welcomedMsg and self.trialNum == 0:
            return self.instructionsHeader
        if self.showBlock:
            return str(self.header) + str(self.headerBlock).format(blockNum=self.trialNum+1, totalBlocks=self.blocks)
        return self.header

    # =====================================================================================
    # resetSM: called to reset state machine with needed values
    # =====================================================================================
    def resetSM(self, sm: StateMachine):
        sm.reset(moves=random.randrange(self.smMoves[0], self.smMoves[1]+1), canMove=True)
        logging.exp(f"Trial SM reset")