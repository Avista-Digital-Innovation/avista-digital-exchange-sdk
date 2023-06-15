import requests
from . import globals
from .subscriptionClient import Subscription
from .graphql_codegen.ariadne.graphql_client.client import Client as AriadneGraphqlClient


class Client:
    updatedGqlClient: AriadneGraphqlClient

    def __init__(self, token, stage, debug):
        APPSYNC_API_ENDPOINT_URL_dev = 'https://annsvlcb4vew7msipwjyzzvyhi.appsync-api.us-west-2.amazonaws.com/graphql'
        APPSYNC_API_ENDPOINT_URL_prod = 'https://rrfs7pb7ancybo7bom7uxcsaxq.appsync-api.us-west-2.amazonaws.com/graphql'
        self.token = token
        self._debug = debug
        self._stage = stage
        if self._stage == "PRODUCTION":
            self.APPSYNC_API_ENDPOINT_URL = APPSYNC_API_ENDPOINT_URL_prod
        else:
            self.APPSYNC_API_ENDPOINT_URL = APPSYNC_API_ENDPOINT_URL_dev
        self.setupUpdatedGqlClient()
        return

    def setupUpdatedGqlClient(self):
        import httpx
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json',
                   'Authorization': self.token}
        self.updatedGqlClient = AriadneGraphqlClient(url=self.APPSYNC_API_ENDPOINT_URL,
                                                     headers=headers,
                                                     http_client=httpx.AsyncClient(headers=headers, timeout=60))

    def performQuery(self, queryString):
        if self._debug:
            print(f'DEBUG - {queryString}')
        response = None

        try:
            with requests.Session() as session:
                response = session.request(
                    url=self.APPSYNC_API_ENDPOINT_URL,
                    method='POST',
                    headers={'Accept': 'application/json',
                             'Content-Type': 'application/json',
                             'Authorization': self.token},
                    json={'query': queryString}
                )
        except Exception as e:
            raise e
        return response.json()

    def performMutation(self, mutationString, jsonResult=True):
        if self._debug:
            print(f'DEBUG - {mutationString}')
        response = None

        try:
            with requests.Session() as session:
                # Now we can simply post the request...
                response = session.request(
                    url=self.APPSYNC_API_ENDPOINT_URL,
                    method='POST',
                    headers={'Accept': 'application/json',
                             'Content-Type': 'application/json',
                             'Authorization': self.token},
                    json={'query': mutationString}
                )
        except Exception as error:
            raise error
        if jsonResult:
            return response.json()
        else:
            return response

    def getSubscriptionClient(self, subscriptionName, subscriptionQueryString, subscriptionMessageQueue, subscriptionErrorQueue):
        if self._debug:
            print(f'subscribing to {subscriptionQueryString}...')
        subscription = Subscription(
            self._debug, subscriptionName, subscriptionQueryString, self.APPSYNC_API_ENDPOINT_URL, self.token, subscriptionMessageQueue, subscriptionErrorQueue)
        return subscription
