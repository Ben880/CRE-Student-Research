from psychopy.hardware import keyboard
from psychopy import logging


class KeyTracker:
    keyCode = None
    defaultKeyboard = None
    keyDown = False
    keyPressed = False
    keyUp = False

    def __init__(self, keyCode: str, defaultKeyboard: keyboard):
        self.keyCode = keyCode
        self.defaultKeyboard = defaultKeyboard

    def update(self):
        current = self.getKeyState()
        self.keyDown = not self.keyPressed and current
        self.keyUp = self.keyPressed and not current
        self.keyPressed = current
        if self.getKeyDown():
            logging.data(f"Key down: {self.keyCode}")

    def getKeyState(self):
        return self.defaultKeyboard.getKeys(self.keyCode)

    def getKeyDown(self):
        return self.keyDown

    def getKeyPressed(self):
        return self.keyPressed

    def getKeyUp(self):
        return self.keyUp

    def getKeyCode(self):
        return self.keyCode
