import random


class StateMachine:
    # dynamic
    currentState = 0
    targetState = 0
    lastScore = 0
    totalScore = 0
    # static
    states = 6
    negativeScores= (-70, -100, -140)
    stateMachineDeffinition = [[(1, 140), (3, 20)],
                               [(2, -20), (4, 0)],
                               [(3, -20), (5, 0)],
                               [(4, -20), (1, 20)],
                               [(5, -20), (0, 0)],
                               [(0, -20), (2, 20)]]

    # move type is 0
    def moveCircle(self):
        self.targetState = self.stateMachineDeffinition[self.currentState][0][0]
        self.scoreMove(0)
        self.currentState = int(self.targetState)

    # move type is 1
    def moveAcross(self):
        self.targetState = self.stateMachineDeffinition[self.currentState][1][0]
        self.scoreMove(1)
        self.currentState = int(self.targetState)

    def scoreMove(self, moveType):
        if self.stateMachineDeffinition[self.currentState][moveType][1] == 0:
            self.lastScore = self.negativeScores[random.randrange(0, 3)]
        else:
            self.lastScore = self.stateMachineDeffinition[self.currentState][moveType][1]
        self.totalScore += self.lastScore

    def reset(self):
        self.currentState = 0
        self.targetState =0
        self.lastScore = 0
        self.totalScore = 0

    def getCurrentState(self):
        return self.currentState

    def getCurrentScore(self):
        return self.totalScore

    def getLastScore(self):
        return self.lastScore