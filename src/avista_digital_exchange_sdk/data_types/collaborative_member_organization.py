from ..exceptions import *
from ..common import *
from .collaborative_member_user import CollaborativeMemberUser
from .user import User
from .organization import Organization

class CollaborativeMemberOrganization:
    def __init__(self, dict, client):
        self.client = client
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)

    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException
        self.organization = Organization(dict['organization'], self.client)
        self.collaborativeId = dict['collaborativeId']
        self.memberState = dict['memberState']
        self.usersInCollaborative = []
        for user in dict['usersInCollaborative']:
            self.usersInCollaborative.append(CollaborativeMemberUser(user, self.client))

    @staticmethod
    def getQueryString(tabs = 1, subobjectsRemaining = 4):
        tabStr = getTabStr(tabs)

        return f""" {{
{tabStr}collaborativeId
{tabStr}{f"organization {Organization.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr}memberState
{tabStr}accessApprovedByUserId
{tabStr}{f"submittedByUser {User.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr}submittedTimestamp
{tabStr}{f"usersInCollaborative {CollaborativeMemberUser.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr[0:-4]}}} """