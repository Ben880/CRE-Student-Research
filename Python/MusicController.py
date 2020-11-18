from Config import Config as config
from LatinSquare import LatinSquareGenerator
import os

def getSong(cfg: config, index):
    stimDir = os.path.join(cfg.getVal("assetDir"), "SoundStim")
    stim = []
    for fname in os.listdir(stimDir):
        stim.append(os.path.join(stimDir, fname))
    songIndex = LatinSquareGenerator(len(stim), index)
    return stim[songIndex]


###  https://spotipy.readthedocs.io/en/2.16.1/

################## https://pypi.org/project/pyspotify/
"""
# test code
cfg = config()
cfg.load()
for i in range(0,50):
    print(getSong(cfg, i))
"""