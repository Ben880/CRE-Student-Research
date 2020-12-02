from psychopy import visual
from Config import Config as Config


class GUIDraw:
    resolution = (1920, 1080)
    pos = None
    color = None
    stateMoves = None
    boxPos = None
    instructionsText = ("intruction set 1", "intruction set 2", "intruction set 3")
    continueText = "press space to continue"

    def __init__(self, pos: Config, color: Config, cfg: Config):
        self.pos = pos
        self.color = color
        self.stateMoves = cfg.getVal("state_moves")
        self.instructionsText = cfg.getVal("instructions_text")
        self.continueText = cfg.getVal("continue_text")
        self.boxPos = pos.getVal("box_pos")

    def getBoxPos(self, buttonNum):
        return self.scaleToRes(self.boxPos[buttonNum])

    def getControlPos(self, multiplier):
        pos = self.cfgTRes("control_pos")
        off = self.cfgTRes("control_offset")
        return (pos[0] + (multiplier * off[0])), (pos[1] + (multiplier * off[1]))

    def getMovePos(self, pos):
        off = self.cfgTRes("move_offset")
        return pos[0] + off[0], pos[1] + off[1]

    def scaleToRes(self, vec2):
        return vec2[0] * self.resolution[0], vec2[1] * self.resolution[1]

    def cfgTRes(self, item: str):
        return self.scaleToRes(self.pos.getVal(item))

    def c(self, item: str):
        return self.color.getVal(item)


class UIComponents:

    font = 'Arial'
    win = None
    resolution = (1920, 1080)
    colorSpace = 'rgb255'

    def __init__(self, win, resolution):
        self.win = win
        self.resolution = resolution

    def createText(self, name="default", text="default text", pos=(0, 0), color=[255, 255, 255], height=50):
        return visual.TextStim(win=self.win, name=name, text=text, font=self.font,
                               pos=pos, height=height, wrapWidth=None, ori=0, color=color,
                               colorSpace='rgb255', opacity=1, languageStyle='LTR', depth=0.0, units='pix')

    def createBox(self, name="default", size=(10,10), pos=(0,0), lcolor = [255,255,255], fcolor=[100, 100, 100]):
        return visual.Rect(win=self.win, name=name, size=size, ori=0,pos=pos,lineWidth=1,
                           lineColor=lcolor, lineColorSpace='rgb255',
                           fillColor=fcolor, fillColorSpace='rgb255', opacity=1, depth=0.0,
                           interpolate=True, units='pix')