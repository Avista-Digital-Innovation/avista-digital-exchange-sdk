from ..exceptions import *
from .. import globals
from .collaborative_member_user import CollaborativeMemberUser
from .user import User
from .organization import Organization


class CollaborativeMemberOrganization:
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
        self.organization = Organization(
            dict['organization'], self._client, self._debug)
        self.collaborativeId = dict['collaborativeId']
        self.memberState = dict['memberState']
        self.usersInCollaborative = []
        for user in dict['usersInCollaborative']:
            self.usersInCollaborative.append(
                CollaborativeMemberUser(user, self._client, self._debug))

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{
{tabStr}collaborativeId
{tabStr}{f"organization {Organization.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr}memberState
{tabStr}accessApprovedByUserId
{tabStr}{f"submittedByUser {User.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr}submittedTimestamp
{tabStr}{f"usersInCollaborative {CollaborativeMemberUser.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr[0:-4]}}} """
