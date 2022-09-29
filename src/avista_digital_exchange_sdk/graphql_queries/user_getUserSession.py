from .query import *
from ..exceptions import *
from .. import globals
from ..data_types.user import User


class user_getUserSession(Query):

    def __init__(self, client, debug):
        super().__init__(client, debug, "user_getUserSession", User)

    def _getQueryString(self):
        tabs = "    "
        return f"""
query {self.queryName} {{ {self.queryName} {{ 
{tabs}user {self.resultType.getQueryString(2)} 
}}}}"""

    def performQuery(self):
        print('Getting your user information...')
        self._result = self._client.performQuery(self._getQueryString())
        return self._processResult()

    def _processResult(self):
        super()._processResult()
        try:
            self.user = User(
                self._result['data'][self.queryName]['user'], self._client, self._debug)
            print(self.user)
            return self.user
        except Exception as e:
            raise e
            raise Exception(
                f"Error processing result of query {self.queryName}")
