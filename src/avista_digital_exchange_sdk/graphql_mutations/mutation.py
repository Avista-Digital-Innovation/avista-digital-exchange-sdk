from ..exceptions import *
from ..common import *

class Mutation:
    def __init__(self, client, mutationName, resultType):
        self.client = client
        self._result = None
        self.mutationName = mutationName
        self.resultType = resultType
        return

    def _getMutationString(self):
        return f"mutation {self.mutationName} {{ {self.mutationName}() {{ {self.resultType.getQueryString(None, 4)} }} }}"
    
    
    def _processResult(self):
        if 'errors' in self._result and len(self._result['errors']) > 0:
            print('Mutation encountered error.')
            print(self._result)
            if 'errorType' in self._result['errors'][0] and ['errorType'] == "UnauthorizedException":
                raise UnauthorizedException
            elif 'message' in self._result['errors'][0]['message'] and self._result['errors'][0]['message'] == "Unauthorized":
                raise Unauthorized
            else:
                raise MutationFailed(f"Mutation {self.mutationName} failed.")
        
        if self._result['data'][self.mutationName] is None:
            raise MissingDataInResultException