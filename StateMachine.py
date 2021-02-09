# ==========================================================================
# By: Benjamin Wilcox (bwilcox@ltu.edu),
# CRE Student Research Project- 1/29/2021
# ==========================================================================
# Description:
# Handles execution of logic for the mini-game
# ==========================================================================
import random
from psychopy import logging

class StateMachine:
    # states used for tracking moves and scores
    currentState = 0
    newState = 0
    # target state for practice
    practiceTargetState = 0
    # scoring
    lastScore = 0
    totalScore = 0
    # moves
    movesLeft = 0
    canMove = True
    drawSM = True
    # negativeIndex should be set per user to determine ho much their negative score is
    # TODO: this needs to be set using a latin square based on size of negativeScores and participant id
    negativeIndex = 0
    # static vars
    negativeScores = (-70, -100, -140)
    stateMachineDeffinition = [[(1, 140), (3, 20)],
                               [(2, -20), (4, 0)],
                               [(3, -20), (5, 0)],
                               [(4, -20), (1, 20)],
                               [(5, -20), (0, 0)],
                               [(0, -20), (2, 20)]]

    # =====================================================================================
    # moveCircle: moves sm in a circle when 'u' key is pressed
    # =====================================================================================
    def moveCircle(self):
        if self.canMove:
            self.newState = self.stateMachineDeffinition[self.currentState][0][0]
            self.scoreMove(0)
            self.currentState = int(self.newState)
            self.movesLeft -= 1
            logging.exp(f"SM-Circle (State:{self.currentState}, Last Score:{self.lastScore}, Total Score:{self.totalScore})")

    # =====================================================================================
    # moveAcross: moves sm in a across when 'i' key is pressed
    # =====================================================================================
    def moveAcross(self):
        if self.canMove:
            self.newState = self.stateMachineDeffinition[self.currentState][1][0]
            self.scoreMove(1)
            self.currentState = int(self.newState)
            self.movesLeft -= 1
            logging.exp(f"SM-Across (State:{self.currentState}, Last Score:{self.lastScore}, Total Score:{self.totalScore})")

    # =====================================================================================
    # scoreMove: scores a move
    # =====================================================================================
    def scoreMove(self, moveType):
        if self.stateMachineDeffinition[self.currentState][moveType][1] == 0:
            self.lastScore = self.negativeScores[self.negativeIndex]
        else:
            self.lastScore = self.stateMachineDeffinition[self.currentState][moveType][1]
        self.totalScore += self.lastScore

    # =====================================================================================
    # reset: resets sm to default values
    # =====================================================================================
    def reset(self, moves = 2, canMove = True):
        self.canMove = canMove
        self.currentState = random.randrange(0, 6)
        self.newState = 0
        self.lastScore = 0
        self.totalScore = 0
        self.movesLeft = moves
        self.practiceTargetState = 0
        logging.exp(f"SM-Reset (State:{self.currentState}, Moves:{moves})")

    # =====================================================================================
    # reset: moves the target 'count' moves, used in training
    # =====================================================================================
    def moveTarget(self, count: int):
        self.practiceTargetState = self.currentState
        for i in range(count):
            if random.randint(0,1):
                self.practiceTargetState = self.stateMachineDeffinition[self.practiceTargetState][0][0]
            else:
                self.practiceTargetState = self.stateMachineDeffinition[self.practiceTargetState][1][0]

    # =====================================================================================
    # lock/unlock: sets weather or not the sm is allowed to be controlled/move states
    # =====================================================================================
    def lock(self):
        self.canMove = False

    def unlock(self):
        self.canMove = True

    # =====================================================================================
    # doDrawSM/dontDrawSM: sets weather or not the sm should draw, only used externally
    # =====================================================================================
    def doDrawSM(self):
        self.drawSM = True

    def dontDrawSM(self):
        self.drawSM = False

    # =====================================================================================
    # getters: get a value
    # =====================================================================================
    def getCurrentState(self):
        return self.currentState

    def getCurrentScore(self):
        return self.totalScore

    def getLastScore(self):
        return self.lastScore

    # =====================================================================================
    # inCorrectState: is the sm in the target state
    # =====================================================================================
    def inCorrectState(self):
        return self.currentState == self.practiceTargetState