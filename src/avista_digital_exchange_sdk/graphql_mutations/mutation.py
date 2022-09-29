from ..exceptions import *
from .. import globals


class Mutation:
    def __init__(self, client, debug, mutationName, resultType):
        self._client = client
        self._debug = debug
        self._result = None
        self.mutationName = mutationName
        self.resultType = resultType
        return

    def _getMutationString(self):
        return f"mutation {self.mutationName} {{ {self.mutationName}() {{ {self.resultType.getQueryString(None, 4)} }} }}"

    def _processResult(self):
        if self._debug:
            print(f'DEBUG - processing mutation result: {self.mutationName}')
            print(f'DEBUG - Result object: {self._result}')
        if 'errors' in self._result and len(self._result['errors']) > 0:
            print('ERROR - Mutation encountered error.')
            print(f'ERROR - Mutation Response/Error: {self._result}')
            if 'errorType' in self._result['errors'][0] and ['errorType'] == "UnauthorizedException":
                raise UnauthorizedException
            elif 'message' in self._result['errors'][0]['message'] and self._result['errors'][0]['message'] == "Unauthorized":
                raise Unauthorized
            else:
                raise MutationFailed(
                    f"Mutation {self.mutationName} failed.", self._result)

        if self._result['data'][self.mutationName] is None:
            raise MissingDataInResultException
