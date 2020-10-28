import json
import os


class Config:
    appData = os.getcwd()
    appFolder = os.path.join(appData, "config")
    cfgName = "cfg.json"
    data = {
        "val1": "1",
        "val2": "2"
    }

    def load(self):
        if not os.path.isdir(self.appFolder):
            print("No app folder: Making one")
            os.mkdir(self.appFolder)
        if not os.path.isfile(os.path.join(self.appFolder, self.cfgName)):
            print("No app cfg: Making one {}".format(os.path.join(self.appFolder, self.cfgName)))
            self.write(self)
        cfg = open(os.path.join(self.appFolder, self.cfgName), "r")
        lines = cfg.readline()
        cfg.close()
        self.data = json.loads(lines)

    def write(self):
        with open(os.path.join(self.appFolder, self.cfgName), 'w+') as fp:
            fp.write(json.dumps(self.data))

    def setVal(self, key, val):
        self.data[key] = val

    def getVal(self, key):
        return self.data[key]

    def contains(self, key):
        return key in self.data

    def addVal(self, key, value):
        self.data[key] = value


x = Config
x.load(x)
print(x.data)
print(x.contains(x,"val1"))
print(x.contains(x,"val5"))
x.addVal(x, "hia", "test")
x.write(x)
print(x.data)
