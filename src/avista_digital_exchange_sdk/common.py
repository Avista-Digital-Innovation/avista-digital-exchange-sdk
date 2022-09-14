
debug = False
stage = "PRODUCTION"

tab = "    "


def getTabStr(tabs=1):
    tabStr = ""
    for i in range(tabs):
        tabStr += tab
    return tabStr
