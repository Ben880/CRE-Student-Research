import Config as Config
import KeyTracker
from StateMachine import StateMachine as StateMachine
from psychopy import logging, core


class PracticeHandler:
    cfg = None
    currentPhase = 0
    practiceText = None
    twoMovesArr = None
    oneMovesArr = None
    displayLast = None
    complete = False
    startedRound = False
    roundFinished = False
    scoredRound = False
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
        "grab": 13,
        "grab2movesI": 14,
        "grab2moves": 15,
        "timeI": 16,
        "time": 17,
        "complete": 18
    }
    movesPos = 0
    # count number of presses of [U,I]
    buttonPresses = [0, 0]
    targetPresses = 0
    targetPresses2 = 0
    pointRequirement = 0
    successful2moves = 0
    successfulTime = 0
    successes = 0
    thinkTimer = None
    moveTimer = None
    practiceTimer = None
    devModeOn = False
    deveModePhase = 0

    def __init__(self, cfg: Config):
        self.cfg = cfg
        self.targetPresses = cfg.getVal("practice_key_requirement")
        self.practiceText = cfg.getVal("practice_text")
        self.twoMovesArr = cfg.getVal("practice_target_2m")
        self.oneMovesArr = cfg.getVal("practice_target_1m")
        self.displayLast = cfg.getVal("practice_display_last")
        self.targetPresses2 = cfg.getVal("practice_key_requirement2")
        self.pointRequirement = cfg.getVal("points_requirement")
        self.successful2moves = cfg.getVal("successful_2moves")
        self.successfulTime = cfg.getVal("successful_timed")
        self.thinkTimer = core.CountdownTimer(cfg.getVal("think_timer"))
        self.moveTimer = core.CountdownTimer(cfg.getVal("move_timer"))
        self.practiceTimer = core.CountdownTimer(cfg.getVal("practice_timer"))
        self.devModeOn = cfg.getVal("devMode")
        if self.devModeOn:
            print("Phases dev mode set")
            logging.exp("Phases dev mode set")

    def update(self, uKey: KeyTracker, iKey: KeyTracker, spaceKey: KeyTracker, sm: StateMachine):
        phases = self.phase
        newPhase = self.currentPhase
        if uKey.getKeyUp():
            self.buttonPresses[0] += 1
        if iKey.getKeyUp():
            self.buttonPresses[1] += 1
        # ======================================================================
        # ===================== phase change logic =============================
        # ======================================================================
        # === 0->2 =============================================================
        if self.isPhase("start") and self.uGthan(0):
            newPhase = phases["pressI"]
        # === 0->1 =============================================================
        if self.isPhase("start") and self.iGthan(0):
            newPhase = phases["pressU"]
        # === 1,2->3 ===========================================================
        if self.isPhases(["pressI", "pressU"]) and self.uGthan(0) and self.iGthan(0):
            newPhase = phases["timed"]
            self.practiceTimer.reset()
        # === 3,4,5,6->7 =======================================================
        isRememberUIPhase = self.isPhases(["rememberUI", "rememberU", "rememberI"])
        if self.isPhase("timed") and self.isTimerUp("practice") or isRememberUIPhase:
            if self.uLthan(self.targetPresses) and self.iLthan(self.targetPresses):
                newPhase = phases["rememberUI"]
            elif self.uLthan(self.targetPresses):
                newPhase = phases["rememberU"]
            elif self.iLthan(self.targetPresses):
                newPhase = phases["rememberI"]
            else:
                newPhase = phases["targetIntro"]
                sm.lock()
        # === 7->8 =============================================================
        if self.isPhase("targetIntro") and spaceKey.getKeyUp():
            newPhase = phases["2moves"]
            sm.unlock()
        # === 8->9 =============================================================
        if self.isPhase("2moves") and sm.inCorrectState() and sm.movesLeft <= 0:
            self.movesPos += 1
            if self.movesPos >= len(self.twoMovesArr):
                newPhase = phases["1moves"]
            else:
                self.resetSM(sm)
        # === 9->10 ============================================================
        if self.isPhase("1moves") and sm.inCorrectState() and sm.movesLeft <= 0:
            self.movesPos += 1
            if self.movesPos >= len(self.oneMovesArr):
                newPhase = phases["practice2"]
                sm.lock()
            else:
                self.resetSM(sm)
        # === 10->11 ===========================================================
        if self.isPhase("practice2") and spaceKey.getKeyUp():
            newPhase = phases["memoryI"]
            sm.lock()
        # === 11->12 ===========================================================
        if self.isPhase("memoryI") and spaceKey.getKeyUp():
            newPhase = phases["memory"]
            self.buttonPresses = [0,0]
            sm.unlock()
        # === 11->12 ===========================================================
        if self.isPhase("memory") and (self.buttonPresses[0] + self.buttonPresses[1]) >= self.targetPresses2:
            newPhase = phases["grab"]
            sm.reset()
        # === 12->13 ===========================================================
        if self.isPhase("grab") and sm.totalScore >= self.pointRequirement:
            newPhase = phases["grab2movesI"]
            self.successes = 0
            sm.lock()
        # === 13->14 ===========================================================
        if self.isPhase("grab2movesI") and spaceKey.getKeyUp():
            newPhase = phases["grab2moves"]
            sm.reset()
            sm.unlock()
        # === 14->15 ===========================================================
        if self.isPhase("grab2moves") and self.successes >= self.successful2moves:
            newPhase = phases["timeI"]
            self.successes = 0
            sm.lock()
        # === 16->17 ===========================================================
        if self.isPhase("timeI") and spaceKey.getKeyUp():
            newPhase = phases["time"]
            sm.reset()
            sm.unlock()
            self.moveTimer.reset()
            self.thinkTimer.reset()
        # === 17->complete ===========================================================
        if self.isPhase("time") and self.successes >= self.successfulTime:
            newPhase = phases["complete"]
            sm.unlock()
        # ======================================================================
        # ===================== phase changing =================================
        # ======================================================================
        phaseChanged = not self.currentPhase == newPhase
        if self.devModeOn:
            if uKey.getKeyUp() or iKey.getKeyUp():
                self.devModeOn = False
                logging.exp(f"dev mode off")
                print(f"dev mode off")
            if not phaseChanged and spaceKey.getKeyUp():
                self.deveModePhase += 1
                newPhase = self.deveModePhase
                logging.exp(f"Debug mode override new Practice Phase: {newPhase}")
                print(f"Debug mode override new Practice Phase: {newPhase}")
        if phaseChanged:
            logging.exp(f"New Practice Phase: {newPhase}")
        self.currentPhase = newPhase
        # ======================================================================
        # ===================conditional update checks==========================
        # ======================================================================
        if self.isPhases(["2moves", "1moves"]):
            if phaseChanged:
                self.movesPos = 0
                self.resetSM(sm)
            if sm.movesLeft <= 0 and not sm.inCorrectState():
                self.resetSM(sm)
        if self.isPhase("grab2moves"):
            if sm.movesLeft == 0:
                sm.lock()
                if spaceKey.getKeyUp():
                    if sm.totalScore >= 0:
                        self.successes += 1
                        logging.exp(f"pp: {newPhase} succeed timed practice")
                    else:
                        logging.exp(f"pp: {newPhase} failed timed practice")
                    sm.reset()
        if self.isPhase("time"):
            if spaceKey.getKeyUp() and self.roundFinished:
                sm.reset()
                sm.unlock()
                self.startedRound = False
                self.roundFinished = False
                self.scoredRound = False
                self.thinkTimer.reset()
            if not self.startedRound:
                if self.isTimerUp("think") or uKey.getKeyUp() or iKey.getKeyUp():
                    self.startedRound = True
                    self.moveTimer.reset()
            if self.startedRound and (sm.movesLeft == 0 or self.isTimerUp("move")):
                sm.lock()
                self.roundFinished = True
                if sm.totalScore >= 0 and not self.scoredRound:
                    self.successes +=1
                    self.scoredRound = True
                    logging.exp(f"pp: {newPhase} succeed timed practice")
                else:
                    logging.exp(f"pp: {newPhase} failed timed practice")
        # ======================================================================
        # ===================== complete condition =============================
        # ======================================================================
        if self.isPhase("complete") and not self.complete:
            self.complete = True
            logging.exp(f"Practice complete")

    def resetSM(self, sm: StateMachine):
        if self.isPhase("2moves"):
            sm.movesLeft = 2
            sm.currentState = self.twoMovesArr[self.movesPos][0]
            sm.practiceTargetState = self.twoMovesArr[self.movesPos][1]
        if self.isPhase("1moves"):
            sm.movesLeft = 1
            sm.currentState = self.oneMovesArr[self.movesPos][0]
            sm.practiceTargetState = self.oneMovesArr[self.movesPos][1]



    def isTimerUp(self, timer: str):
        if timer == "practice":
            return self.practiceTimer.getTime() <= 0
        if timer == "move":
            return self.moveTimer.getTime() <= 0
        if timer == "think":
            return self.thinkTimer.getTime() <= 0

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
        if self.isPhase("timed"):
            text = text + f"move around for {round(self.practiceTimer.getTime() * 10) / 10}s"
        elif self.isPhases(["2moves", "1moves"]):
            text = text + self.cfg.getVal("practice_text")[self.currentPhase] + f"\n(moves left: {sm.movesLeft})"
        else:
            text = text +self.cfg.getVal("practice_text")[self.currentPhase]
        if self.isPhase("grab"):
            text = text + f"\nyou scored: {sm.totalScore}"
        if self.isPhase("grab2moves"):
            if sm.movesLeft == 0:
                text = f"You scored: {sm.getCurrentScore()}\n({self.successes}/{self.successful2moves})\npress space to start new round"
            else:
                text = text + f"moves left: {sm.movesLeft}"
        if self.isPhase("time"):
            if not self.startedRound:
                text = f"think time {round(self.thinkTimer.getTime() * 10) / 10}s"
            elif self.isTimerUp("move") and sm.movesLeft > 0:
                text = f"You ran out of time\npress space to start new round"
            elif sm.movesLeft == 0:
                text = f"You scored {sm.getCurrentScore()}\n({self.successes}/{self.successfulTime})\npress space to start new round"
            elif self.startedRound and not self.isTimerUp("move"):
                text = f"time left {round(self.moveTimer.getTime() * 10) / 10}s"
        if self.isPhase("complete"):
            text = f"practice complete\npress space to continue"
        # ================== appending ===========================================
        if self.currentPhase in self.displayLast:
            text = text + f"\nyou scored: {sm.lastScore}"
        return text


