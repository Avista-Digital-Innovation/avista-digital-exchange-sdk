import json
from base64 import b64encode, decode
import requests
from . import globals
from .subscriptionClient import Subscription
from .async_graphql_client.client import Client as GeneratedGraphqlClient


class Client:
    updatedGqlClient: GeneratedGraphqlClient

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

        self.APPSYNC_API_WS_URL = self.APPSYNC_API_ENDPOINT_URL.replace(
            'https', 'wss').replace('appsync-api', 'appsync-realtime-api')
        self.APPSYNC_HOST = self.APPSYNC_API_ENDPOINT_URL.replace(
            'https://', '').replace('/graphql', '')
        self.setupUpdatedGqlClient()
        return

    def setupUpdatedGqlClient(self):
        import httpx
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json',
                   'Authorization': self.token, }
        wsHeaders = {
            'Authorization': self.token,
            'HOST': self.APPSYNC_HOST}
        wsExtensions = {'authorization': {
            'host': self.APPSYNC_HOST,
            'Authorization': self.token
        }}

        # ssl._create_default_https_context = ssl._create_unverified_context
        print(self.APPSYNC_API_ENDPOINT_URL)
        print(self.APPSYNC_API_WS_URL)
        self.updatedGqlClient = GeneratedGraphqlClient(url=self.APPSYNC_API_ENDPOINT_URL,
                                                       ws_url="wss://annsvlcb4vew7msipwjyzzvyhi.appsync-realtime-api.us-west-2.amazonaws.com/graphql"
                                                       + '?header=' +
                                                       headerEncode(
                                                         wsHeaders) + '&payload=e30=',
                                                       #  ws_headers=wsHeaders,
                                                       #  ws_origin=self.APPSYNC_HOST,
                                                       ws_extensions=wsExtensions,
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


def headerEncode(header_obj):
    return b64encode(json.dumps(header_obj).encode('utf-8')).decode('utf-8')
