import random
from psychopy import logging

class StateMachine:
    # dynamic
    currentState = 0
    newState = 0
    practiceTargetState = 0
    lastScore = 0
    totalScore = 0
    movesLeft = 0
    # static
    states = 6
    negativeScores= (-70, -100, -140)
    stateMachineDeffinition = [[(1, 140), (3, 20)],
                               [(2, -20), (4, 0)],
                               [(3, -20), (5, 0)],
                               [(4, -20), (1, 20)],
                               [(5, -20), (0, 0)],
                               [(0, -20), (2, 20)]]

    def moveCircle(self):
        self.newState = self.stateMachineDeffinition[self.currentState][0][0]
        self.scoreMove(0)
        self.currentState = int(self.newState)
        self.movesLeft -= 1
        logging.exp(f"SM New State:{self.currentState}, Last Score:{self.lastScore}, Total Score:{self.totalScore}")

    def moveAcross(self):
        self.newState = self.stateMachineDeffinition[self.currentState][1][0]
        self.scoreMove(1)
        self.currentState = int(self.newState)
        self.movesLeft -= 1
        logging.exp(f"SM New State:{self.currentState}, Last Score:{self.lastScore}, Total Score:{self.totalScore}")

    def scoreMove(self, moveType):
        if self.stateMachineDeffinition[self.currentState][moveType][1] == 0:
            self.lastScore = self.negativeScores[random.randrange(0, 3)]
        else:
            self.lastScore = self.stateMachineDeffinition[self.currentState][moveType][1]
        self.totalScore += self.lastScore

    def reset(self, moves = 2):
        self.currentState = random.randrange(0,6)
        self.newState = 0
        self.lastScore = 0
        self.totalScore = 0
        self.movesLeft = moves
        self.practiceTargetState = 0
        logging.exp(f"SM Reset State:{self.currentState}, Moves:{moves}")

    def getCurrentState(self):
        return self.currentState

    def getCurrentScore(self):
        return self.totalScore

    def getLastScore(self):
        return self.lastScore

    def inCorrectState(self):
        return self.currentState == self.practiceTargetState