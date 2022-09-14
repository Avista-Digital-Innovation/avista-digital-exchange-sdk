from ..data_types.user import User
from ..exceptions import *
from ..common import *

class Query:
    def __init__(self, client, queryName, resultType):
        self.client = client
        self._result = None
        self.queryName = queryName
        self.resultType = resultType
        return

    def _getQueryString(self):
        return f"query {self.queryName} {{ {self.queryName} {self.resultType.getQueryString()} }}"
    
    def _processResult(self):
        if 'errors' in self._result and len(self._result['errors']) > 0:
            print('Query encountered error.')
            print(self._result)
            if 'errorType' in self._result['errors'][0] and self._result['errors'][0]['errorType'] == "UnauthorizedException":
                raise UnauthorizedException
            elif 'message' in self._result['errors'][0]['message'] and self._result['errors'][0]['message'] == "Unauthorized":
                raise Unauthorized
            else:
                raise QueryFailed(f"Query {self.queryName} failed.")
        
        if self._result['data'][self.queryName] is None:
            raise MissingDataInResultException