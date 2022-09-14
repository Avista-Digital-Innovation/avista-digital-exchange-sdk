from ..exceptions import *
from ..common import *
from .service import Service
from .collaborative_member_organization import CollaborativeMemberOrganization

class Collaborative:
    def __init__(self, dict, client):
        self.client = client
        if dict is None:
            raise MissingDataInResultException
        else:
            self.buildFromDictionary(dict)
    
    def __str__(self):
        return f"""Collaborative: {self.collaborativeId}
   name: {self.name}
   description: {self.description}
   {self._printMembers()}"""

    def _printMembers(self):
        if self.memberOrganizations is not None and len(self.memberOrganizations) > 0:
            result = "members: \n"
        else:
            return ""
        for org in self.memberOrganizations:
            if org.memberState == "APPROVED" or org.memberState == "HOST_ORGANIZATION":
                result += f"    - {org.organization.name} | {len(org.usersInCollaborative)} user{'s' if len(org.usersInCollaborative) > 1 else ''}\n"
        return result


    def buildFromDictionary(self, dict):
        if dict is None:
            raise MissingDataInResultException
        self.collaborativeId = dict['collaborativeId']
        self.name = dict['name']
        self.description = dict['description']
        self.hostOrganizationId = dict['hostOrganizationId']
        self.memberOrganizations = []
        for org in dict['memberOrganizations']:
            self.memberOrganizations.append(CollaborativeMemberOrganization(org, self.client))

    @staticmethod
    def getQueryString(tabs = 1, subobjectsRemaining = 4):
        tabStr = getTabStr(tabs)

        return f""" {{
{tabStr}collaborativeId
{tabStr}hostOrganizationId
{tabStr}description
{tabStr}name
{tabStr}{f"memberOrganizations {CollaborativeMemberOrganization.getQueryString(tabs + 1, subobjectsRemaining - 1)}" if subobjectsRemaining > 0 else ""}
{tabStr[0:-4]}}} """

    def listSharedServices(self):
        # TODO
        return

    def shareService(self, serviceId, serviceType):
        # TODO
        return

    def removeService(self, serviceId, serviceType):
        # TODO
        return
