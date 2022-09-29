from .organization import Organization
from ..exceptions import *
from .. import globals


class User:
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
        self.firstName = dict['firstName']
        self.lastName = dict['lastName']
        self.userId = dict['userId']
        self.email = dict['email']
        self.mobile = dict['mobile']
        self.userAccountState = dict['userAccountState']
        self.lastActive = dict['lastActive']
        self.userRoles = dict['userRoles']
        self.organization = Organization(
            dict['organization'], self._client, self._debug)

    def __str__(self):
        return f"""User
    name: {self.firstName + " " + self.lastName}
    userId: {self.userId}
    userRoles: {self.userRoles}
    organization name: {self.organization.name}
    organizationId: {self.organization.organizationId}
"""

    @staticmethod
    def getQueryString(tabs=1, subobjectsRemaining=4):
        tabStr = globals.getTabStr(tabs)

        return f""" {{
{tabStr}firstName
{tabStr}lastName
{tabStr}userId
{tabStr}email
{tabStr}lastActive
{tabStr}mobile
{tabStr}userAccountState
{tabStr}userRoles
{tabStr}{f"organization {Organization.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr[0:-4]}}} """
