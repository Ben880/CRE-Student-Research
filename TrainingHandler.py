import Config as Config
import KeyTracker
from StateMachine import StateMachine as StateMachine
from psychopy import logging, core
import random


class TrainingHandler:

    trainingMoves = [1,4];
    trainingTrials = 40
    trainingRequirementSize = 10
    trainingRequirementCorrect = 9
    instructionsStr = ""
    instructionsStrTwo = ""
    correctStr = ""
    incorrectStr = ""


    currentPhase = 0
    phase = {
        "init": 0,
        "phaseOneI": 1,
        "phaseOne": 2,
        "phaseTwoI": 3,
        "phaseTwo": 4,
        "done": 5,
        "final": 6
    }

    skipOne = False
    skipTwo = False
    complete = False
    correct = 0
    attempts = 0
    waitForSpace = False
    partTwoAttempts = 0
    partTwoFailed = False


    def __init__(self, cfg: Config):
        self.trainingMoves = cfg.getVal("training_moves")
        self.trainingTrials = cfg.getVal("training_trials")
        self.trainingRequirementSize = cfg.getVal("training_requirement_size")
        self.trainingRequirementCorrect = cfg.getVal("training_requirement_correct")
        self.instructionsStr = cfg.getVal("training_instructions")
        self.instructionsStrTwo = cfg.getVal("training_instructions2")
        self.correctStr = cfg.getVal("training_correct")
        self.incorrectStr = cfg.getVal("training_incorrect")
        self.skipOne = cfg.getVal("skip_training1")
        self.skipTwo = cfg.getVal("skip_training2")

    def update(self, uKey: KeyTracker, iKey: KeyTracker, spaceKey: KeyTracker, sm: StateMachine):
        phases = self.phase
        newPhase = self.currentPhase
        # ======================================================================
        # ===================== phase changing =================================
        # ======================================================================
        if self.isPhase("init"):
            if self.skipOne:
                newPhase = phases["phaseTwoI"]
                logging.exp(f"Debug skip training phase 1")
                print(f"Debug skip training phase 1")
            else:
                newPhase = phases["phaseOneI"]
            sm.lock()
        if self.isPhase("phaseOneI") and spaceKey.getKeyUp():
            newPhase = phases["phaseOne"]
            self.resetSM(sm)
            sm.unlock()
        if self.isPhase("phaseOne") and self.correct > self.trainingTrials:
            newPhase = phases["phaseTwoI"]
        if self.isPhase("phaseTwoI") and self.skipTwo:
            newPhase = phases["done"]
        if self.isPhase("phaseTwoI") and spaceKey.getKeyUp():
            self.correct = 0
            self.resetSM(sm)
            sm.unlock()
            newPhase = phases["phaseTwo"]
        if self.isPhase("phaseTwo") and self.correct > self.trainingRequirementCorrect:
            newPhase = phases["done"]
        if self.isPhase("done") and spaceKey.getKeyUp():
            newPhase = phases["final"]
            self.complete = True
        # ======================================================================
        # ===================== phase changing =================================
        # ======================================================================
        if self.currentPhase != newPhase:
            logging.exp(f"New training Phase: {newPhase}")
            print(f"New training Phase: {newPhase}")
        self.currentPhase = newPhase
        # ======================================================================
        # ===================conditional update checks==========================
        # ======================================================================
        if self.isPhase("phaseOne"):
            if sm.movesLeft == 0 and not self.waitForSpace:
                self.waitForSpace = True
                self.correct += 1
                sm.lock()
                if sm.practiceTargetState == sm.currentState:
                    logging.exp(f"Training1 user correct {self.correct}/{self.trainingTrials}")
                else:
                    logging.exp(f"Training1 user incorrect {self.correct}/{self.trainingTrials}")
            if spaceKey.getKeyUp() and self.waitForSpace:
                self.waitForSpace = False
                self.resetSM(sm)
                sm.unlock()
        if self.isPhase("phaseTwo"):
            if sm.movesLeft == 0 and not self.waitForSpace:
                self.waitForSpace = True
                self.attempts += 1
                sm.lock()
                if sm.practiceTargetState == sm.currentState:
                    self.correct += 1
                    logging.exp(f"Training2 user correct {self.correct}/{self.trainingTrials}")
                    print("correct, await response")
                else:
                    logging.exp(f"Training2 user incorrect {self.correct}/{self.trainingTrials}")
                    print("incorrect, await response")
            if spaceKey.getKeyUp() and self.waitForSpace:
                self.resetSM(sm)
                self.waitForSpace = False
                sm.unlock()
                print("response, sm reset")
            if self.attempts - self.correct > self.trainingRequirementSize - self.trainingRequirementCorrect and not self.partTwoFailed:
                self.partTwoFailed = True
                sm.lock()
                logging.exp(f"Training2 user failed on attempt {self.partTwoAttempts}")
                print("failed, await response")
            if self.partTwoFailed and spaceKey.getKeyUp():
                self.partTwoFailed = False
                print("response, reset part 2")
                self.partTwoAttempts += 1
                self.attempts = 0
                self.correct = 0
                self.resetSM(sm)
                sm.unlock()


    def end(self):
        logging.exp(f"Traininghndler end called use on attempt: {self.attempts} (zero is first)")


    def getPhaseText(self, sm: StateMachine):
        if self.isPhase("phaseOneI"):
            return self.instructionsStr;
        if self.isPhase("phaseOne"):
            if sm.movesLeft > 0:
                return f"Moves left: {sm.movesLeft}\nRemaining: {self.correct}/{self.trainingTrials}"
            if sm.practiceTargetState == sm.currentState:
                return self.correctStr+f"\nRemaining: {self.correct}/{self.trainingTrials}\npress space to continue"
            else:
                return self.incorrectStr+f"\nRemaining: {self.correct}/{self.trainingTrials}\npress space to continue"
        if self.isPhase("phaseTwoI"):
            return self.instructionsStrTwo;
        if self.isPhase("phaseTwo"):
            if sm.movesLeft > 0:
                return f"Moves left: {sm.movesLeft}\n Remaining: {self.correct}/{self.trainingRequirementSize}"
            if self.partTwoFailed:
                return f"\nYou failed \npress space to try again"
            if sm.practiceTargetState == sm.currentState:
                return self.correctStr + f"\nRemaining: {self.correct}/{self.trainingRequirementSize}\npress space to continue"
            else:
                return self.incorrectStr+f"\nRemaining: {self.correct}/{self.trainingRequirementSize}\npress space to continue"
        if self.isPhase("done"):
            return "Training Complete\npress space when ready to continue to trial"

    def isPhase(self, phase):
        return self.currentPhase == self.phase[phase]

    def resetSM(self, sm: StateMachine):
        sm.reset(moves=random.randrange(self.trainingMoves[0], self.trainingMoves[1]+1), canMove=True)
        sm.moveTarget(sm.movesLeft)