
# debug = True
# stage = "PRODUCTION"

# class GlobalVariables:
#     def __init__(self, debug, stage):
#         self.debug = debug
#         self.stage = stage

#         self.tab = "    "

#     def getTabStr(self, tabs=1):
#         tabStr = ""
#         for i in range(tabs):
#             tabStr += self.tab
#         return tabStr

tab = "    "


def getTabStr(tabs=1):
    tabStr = ""
    for i in range(tabs):
        tabStr += tab
    return tabStr
