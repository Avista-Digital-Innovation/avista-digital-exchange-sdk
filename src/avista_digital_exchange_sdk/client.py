import requests
from . import globals
import json
import base64
import websocket
from .subscriptionClient import Subscription


class Client:

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
        return

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

    def performMutation(self, mutationString):
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
        return response.json()

    def getSubscriptionClient(self, subscriptionName, subscriptionQueryString, subscriptionMessageQueue, subscriptionErrorQueue):
        if self._debug:
            print(f'subscribing to {subscriptionQueryString}...')
        subscription = Subscription(
            self._debug, subscriptionName, subscriptionQueryString, self.APPSYNC_API_ENDPOINT_URL, self.token, subscriptionMessageQueue, subscriptionErrorQueue)
        return subscription
