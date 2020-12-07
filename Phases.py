import Config as Config
import KeyTracker
from StateMachine import StateMachine as StateMachine


class Practice:
    cfg = None
    currentPhase = 0
    timer = None
    practiceText = None
    twoMovesArr = None
    oneMovesArr = None
    displayLast = None
    phase = {
        "start": 0,
        "pressU": 1,
        "pressI": 2,
        "timed": 3,
        "rememberUI": 4,
        "rememberU": 5,
        "rememberI": 6,
        "targetIntro": 7,
        "2moves": 8,
        "1moves": 9,
        "practice2": 10,
        "memoryI": 11,
        "memory": 12,
        "grab2moves": 13,
        "time": 14,
        "complete": 15
    }
    movesPos = 0
    # count number of presses of [U,I]
    buttonPresses = [0, 0]
    targetPresses = 0

    def __init__(self, cfg: Config, timer):
        self.cfg = cfg
        self.targetPresses = cfg.getVal("practice_key_requierment")
        self.timer = timer
        self.practiceText = cfg.getVal("practice_text")
        self.twoMovesArr = cfg.getVal("practice-target-2m")
        self.oneMovesArr = cfg.getVal("practice-target-1m")
        self.displayLast = cfg.getVal("practic-display-last")

    def update(self, uKey: KeyTracker, iKey: KeyTracker, spaceKey: KeyTracker, sm: StateMachine):
        # update phases
        phases = self.phase
        newPhase = self.currentPhase
        if uKey.getKeyUp():
            self.buttonPresses[0] += 1
        if iKey.getKeyUp():
            self.buttonPresses[1] += 1
        if self.isPhase("start") and self.uGthan(0):
            newPhase = phases["pressI"]
        if self.isPhase("start") and self.iGthan(0):
            newPhase = phases["pressU"]
        if self.isPhases(["pressI", "pressU"]) and self.uGthan(0) and self.iGthan(0):
            newPhase = phases["timed"]
            self.timer.reset()
        if self.isPhase("timed") and self.timeUp() or (self.isPhases(["rememberUI", "rememberU", "rememberI"])):
            if self.uLthan(self.targetPresses) and self.iLthan(self.targetPresses):
                newPhase = phases["rememberUI"]
            elif self.uLthan(self.targetPresses):
                newPhase = phases["rememberU"]
            elif self.iLthan(self.targetPresses):
                newPhase = phases["rememberI"]
            else:
                newPhase = phases["targetIntro"]
        if self.isPhase("targetIntro") and spaceKey.getKeyUp():
            newPhase = phases["2moves"]
        if self.isPhase("2moves") and sm.inCorrectState() and sm.movesLeft <= 0:
            self.movesPos += 1
            if self.movesPos >= len(self.twoMovesArr):
                newPhase = phases["1moves"]
            else:
                self.resetSM(sm)
        if self.isPhase("1moves") and sm.inCorrectState() and sm.movesLeft <= 0:
            self.movesPos += 1
            if self.movesPos >= len(self.oneMovesArr):
                newPhase = phases["practice2"]
            else:
                self.resetSM(sm)
        if self.isPhase("practice2") and spaceKey.getKeyUp():
            newPhase = phases["pointGrab"]
        # phase changing
        phaseChanged = not self.currentPhase == newPhase
        self.currentPhase = newPhase
        # conditional update checks
        if self.isPhases(["2moves", "1moves"]):
            if phaseChanged:
                self.movesPos = 0
                self.resetSM(sm)
            if sm.movesLeft <= 0 and not sm.inCorrectState():
                self.resetSM(sm)

    def resetSM(self, sm: StateMachine):
        if self.isPhase("2moves"):
            sm.movesLeft = 2
            sm.currentState = self.twoMovesArr[self.movesPos][0]
            sm.practiceTargetState = self.twoMovesArr[self.movesPos][1]
        if self.isPhase("1moves"):
            sm.movesLeft = 1
            sm.currentState = self.oneMovesArr[self.movesPos][0]
            sm.practiceTargetState = self.oneMovesArr[self.movesPos][1]

    def timeUp(self):
        return self.timer.getTime() <= 0

    def uLthan(self, lessthan):
        return self.buttonPresses[0] < lessthan

    def iLthan(self, lessthan):
        return self.buttonPresses[1] < lessthan

    def uGthan(self, greaterthan):
        return self.buttonPresses[0] > greaterthan

    def iGthan(self, greaterthan):
        return self.buttonPresses[1] > greaterthan

    def isPhase(self, phase):
        return self.currentPhase == self.phase[phase]

    def isPhases(self, phases):
        for phase in phases:
            if self.isPhase(phase):
                return True
        return False

    def getPhaseText(self, sm: StateMachine):
        text = ""
        if self.currentPhase == self.phase["timed"]:
            text = text + f"move around for {round(self.timer.getTime() * 10) / 10}s"
        elif self.isPhases(["2moves", "1moves"]):
            text = text + self.cfg.getVal("practice_text")[self.currentPhase] + f"\n(moves left: {sm.movesLeft})"
        else:
            text = text +self.cfg.getVal("practice_text")[self.currentPhase]
        if self.displayLast[self.currentPhase]:
            text = text + f"\nyou scored: {sm.lastScore}"
        return text

