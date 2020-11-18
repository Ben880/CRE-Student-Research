import random


class StateMachine:
    # dynamic
    currentState = 0
    targetState = 0
    lastScore = 0
    totalScore = 0
    # static
    states = 6
    baseAmount = 20
    baseDeviant = 10
    ### big - 70 100 140
    # wins and small losses fixed
    #
    stateDeffinition = [[7, 1],
                        [-1, -7],
                        [-1, -7],
                        [+1, -1],
                        [-1, -7],
                        [+1, -1]]

    # move type is 0
    def moveCircle(self):
        self.targetState = self.currentState + 1
        self.modCheck()
        self.generateScore(0)

    # move type is 1
    def moveAcross(self):
        self.targetState = self.currentState + (self.states /2)
        self.modCheck()
        self.generateScore(1)

    def modCheck(self):
        if self.targetState > self.states - 1:
            self.targetState = self.targetState % 6

    def generateScore(self, moveType):
        rnum = random.randrange(self.baseAmount - self.baseDeviant, self.baseAmount + self.baseDeviant)
        self.lastScore = rnum * self.stateDeffinition[self.currentState][moveType]
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