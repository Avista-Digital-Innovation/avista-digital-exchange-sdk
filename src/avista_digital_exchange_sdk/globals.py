
debug = True
stage = "PRODUCTION"
# def init(debugParam, stageParam):
#     self.debug = debugParam
#     self.stage = stageParam

tab = "    "


def getTabStr(tabs=1):
    tabStr = ""
    for i in range(tabs):
        tabStr += tab
    return tabStr
