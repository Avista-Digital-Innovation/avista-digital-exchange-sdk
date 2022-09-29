from ..exceptions import *
from .. import globals
from .user import User


class CollaborativeMemberUser:
    def __init__(self, dict, client, debug):
        self._client = client
        self._debug = debug
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)

    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException
        self.permission = dict['permission']
        self.user = User(dict['user'], self._client, self._debug)

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{
{tabStr}permission
{tabStr}{f"user {User.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr[0:-4]}}} """
