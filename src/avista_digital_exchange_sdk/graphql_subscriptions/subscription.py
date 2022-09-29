from ..exceptions import *
from .. import globals


class Subscription:
    def __init__(self, client, debug, subscriptionName, resultType):
        self._client = client
        self._debug = debug
        self._result = None
        self.subscriptionName = subscriptionName
        self.resultType = resultType
        return

    def _getSubscriptionQueryString(self):
        return f"subscription {self.subscriptionName} {{ {self.subscriptionName} {self.resultType.getQueryString()} }}"

    def _processResult(self):
        if self._debug:
            print(
                f'DEBUG - processing subscription result: {self.subscriptionName}')
            print(f'DEBUG - {self._result}')
        if 'errors' in self._result and len(self._result['errors']) > 0:
            print('ERROR - Subscription encountered error.')
            print(f'ERROR - Response/Error: {self._result}')
            if 'errorType' in self._result['errors'][0] and self._result['errors'][0]['errorType'] == "UnauthorizedException":
                raise UnauthorizedException
            elif 'message' in self._result['errors'][0]['message'] and self._result['errors'][0]['message'] == "Unauthorized":
                raise Unauthorized
            else:
                raise SubscriptionFailed(
                    f"ERROR - Subscription {self.subscriptionName} failed.", self._result)

        if self._result['data'][self.subscriptionName] is None:
            raise MissingDataInResultException
