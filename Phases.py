import Config as Config



class Practice:
    cfg = None
    currentPhase = 0
    timer = None
    phase = {
        "start": 0,
        "pressU": 1,
        "pressI": 2,
        "timed": 3,
        "rememberUI": 4,
        "rememberU": 5,
        "rememberI": 6,
        "complete": 7
    }

    # count number of presses of [U,I]
    buttonPresses = [0, 0]
    targetPresses = 0

    def __init__(self, cfg: Config, timer):
        self.cfg = cfg
        self.targetPresses = cfg.getVal("practice_key_requierment")
        self.timer = timer

    def update(self):
        phases = self.phase
        newPhase = self.currentPhase
        if self.isPhase("start") and self.uGthan(0):
            newPhase = phases["pressI"]
        if self.isPhase("start") and self.iGthan(0):
            newPhase = phases["pressU"]
        if self.isPhases(["pressI", "pressU"]) and self.uGthan(1) and self.iGthan(0):
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
                newPhase = phases["complete"]
        self.currentPhase = newPhase

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
    
    def buttonPress(self, pressedButton: str):
        if pressedButton == "u":
            self.buttonPresses[0] += 1
        if pressedButton == "i":
            self.buttonPresses[0] += 1
