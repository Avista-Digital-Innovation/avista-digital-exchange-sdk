from .organization import Organization
from ..exceptions import *
from ..common import *

class User:
    def __init__(self, dict, client):
        self.client = client
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
        self.organization = Organization(dict['organization'], self.client)

    def __str__(self):
        return f"""User
    name: {self.firstName + " " + self.lastName}
    userId: {self.userId}
    userRoles: {self.userRoles}
    organization name: {self.organization.name}
    organizationId: {self.organization.organizationId}
"""

    @staticmethod
    def getQueryString(tabs = 1, subobjectsRemaining = 4):
        tabStr = getTabStr(tabs)

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