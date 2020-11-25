
class StateMachineDraw:
    resolution = (1920, 1080)
    boxPos = [[.1, .2],
                 [-.1, .2],
                 [-.3, 0],
                 [-.1, -.2],
                 [.1, -.2],
                 [.3, 0]]
    boxHeight = .05
    boxWidth = .09
    boxSelectedColor = [255, 255, 255]
    boxColor = [100, 100, 100]
    boxLineColor = [0, 0, 0]

    def getBoxPos(self, buttonNum):
        return (self.resolution[0] * self.boxPos[buttonNum][0], self.resolution[1] * self.boxPos[buttonNum][1])

    def setResolution(self, res):
        self.resolution = res

    def getBoxSize(self):
        tmp = [self.resolution[0] * self.boxWidth, self.resolution[0] * self.boxHeight]
        return tmp


class GUIDraw:
    resolution = (1920, 1080)
    bgColor = [150, 150, 150]

    stateMoves = ["++/+",
                  "-/--",
                  "-/--",
                  "+/-",
                  "+/-",
                  "-/--"]

    controllBoxColor = [230, 150, 5]
    controllTextColor = [0, 0, 0]
    controllPosition = (0, -.4)
    controllPositionOffset = (.05, 0)
    controllBoxSize = (.05,.05)
    controllBoxLineColor = (0, 0, 0)


    generalTextColor = [125, 200, 230]
    generalTextPosition = (0,0)
    moveTextOffset = (0, -.06)
    moveTextColor = (180, 180, 180)


    debugTextColor = [255, 0, 0]
    debugTextPos = (-.4, .4)

    practiceHeaderPos = (0, .4)
    practiceBodyPos = (0, 0)

    instructionsHeaderPos = (0, .4)
    instructionsBodyPos = (0, 0)
    instructionsBodyText = ("intruction set 1", "intruction set 2", "intruction set 3")
    instructionsContinuePos = (0, -.4)
    instructionsContinueText = "press space to continue"

    def getControllButtonPos(self, multiplier):
        return (self.resolution[0] * (self.controllPosition[0] + (multiplier* self.controllPositionOffset[0])),
                self.resolution[1] * (self.controllPosition[1] + (multiplier * self.controllPositionOffset[1])))

    def getTextPos(self, textName):
        if textName == "instructionsHeader":
            return self.instructionsHeaderPos[0] * self.resolution[0],self.instructionsHeaderPos[1] * self.resolution[1]
        if textName == "instructionsBody":
            return self.instructionsBodyPos[0] * self.resolution[0],self.instructionsBodyPos[1] * self.resolution[1]
        if textName == "instructionsContinue":
            return self.instructionsContinuePos[0] * self.resolution[0],self.instructionsContinuePos[1] * self.resolution[1]
        if textName == "practiceHeader":
            return self.practiceHeaderPos[0] * self.resolution[0],self.practiceHeaderPos[1] * self.resolution[1]
        if textName == "practiceBody":
            return self.practiceBodyPos[0] * self.resolution[0],self.practiceBodyPos[1] * self.resolution[1]

    def getMoveTextPos(self, pos):
        return pos[0] + (self.moveTextOffset[0]*self.resolution[0]), pos[1] + (self.moveTextOffset[1]*self.resolution[1])

    def getControllBoxSize(self):
        return self.resolution[0] * self.controllBoxSize[0], self.resolution[1] * self.controllBoxSize[1]

    def getContinueText(self):
        return self.instructionsContinueText

    def getBodyText(self, index):
        return self.instructionsBodyText[index]

    def lenBodyText(self):
        return len(self.instructionsBodyText)