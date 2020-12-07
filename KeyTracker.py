from psychopy.hardware import keyboard


class KeyTracker:
    keyCode = None
    defaultKeyboard = None
    keyDown = False
    keyPressed = False
    keyUp = False

    def __init__(self, keyCode, defaultKeyboard: keyboard):
        self.keyCode = keyCode
        self.defaultKeyboard = defaultKeyboard

    def update(self):
        current =  self.getKeyState()
        self.keyDown = not self.keyPressed and current
        self.keyUp = self.keyPressed and not current
        self.keyPressed = current

    def getKeyState(self):
        return self.defaultKeyboard.getKeys(keyList=[self.keyCode])

    def getKeyDown(self):
        return self.keyDown

    def getKeyPressed(self):
        return self.keyPressed

    def getKeyUp(self):
        return self.keyUp
