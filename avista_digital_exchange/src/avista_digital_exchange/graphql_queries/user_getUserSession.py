from .query import *
from exceptions import *
from common import *
from data_types.user import User

class user_getUserSession(Query):

    def __init__(self, client):
        super().__init__(client, "user_getUserSession")
    
    def _getQueryString(self):
        tabs = "    "
        return f"""
query {self.queryName} {{ {self.queryName} {{ 
{tabs}user {self.resultType.getQueryString(2)} 
}}}}"""

    def performQuery(self):
        self._result = self.client.performQuery(self._getQueryString())
        return self._processResult()
    
    def _processResult(self):
        super()._processResult()
        try:
            self.user = User(self._result['data'][self.queryName]['user'], self.client)
            return self.user
        except Exception as e:
            raise e
            raise Exception(f"Error processing result of query {self.queryName}")
