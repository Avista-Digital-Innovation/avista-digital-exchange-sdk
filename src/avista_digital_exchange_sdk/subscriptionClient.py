# subscription_client.py

from base64 import b64encode, decode
from datetime import datetime
# from lib2to3.pgen2 import token
from uuid import uuid4

import websocket
import threading

import json
import ssl

global globToken
global SUB_ID
global timeoutTimer
global timeout_interval
global graphqlSubscription
global HOST
global subscriptionOperationName


class Subscription:
    def __init__(self, debug, subscriptionName, subscriptionQueryString, API_URL, token, subscriptionMessageQueue, subscriptionErrorQueue, onMessage=None, onOpen=None, onClose=None, onError=None):
        """GraphQL subscription Registration object"""
        self._debug = debug
        self.subscriptionName = subscriptionName
        self.subscriptionQueryString = subscriptionQueryString
        self._API_URL = API_URL
        self._token = token
        self.subscriptionMessageQueue = subscriptionMessageQueue
        self.subscriptionErrorQueue = subscriptionErrorQueue

        self.graphqlSubscription = json.dumps({
            "query": self.subscriptionQueryString,
            "variables": {}
        })

        # Discovered values from the AppSync endpoint (API_URL)
        self.WSS_URL = self._API_URL.replace('https', 'wss').replace(
            'appsync-api', 'appsync-realtime-api')
        self.HOST = self._API_URL.replace(
            'https://', '').replace('/graphql', '')

        self.SUB_ID = str(uuid4())
        self.timeoutTimer = None
        self.timeout_interval = 10

        self.headers = {'HOST': self.HOST,
                        'Authorization': self._token}

        # Set up the connection URL, which includes the Authentication Header
        #   and a payload of '{}'.  All info is base 64 encoded
        self.connectionUrl = self.WSS_URL + '?header=' + \
            headerEncode(self.headers) + '&payload=e30='

        # self.performSubscribe(self)

        global globToken
        global SUB_ID
        global timeoutTimer
        global timeout_interval
        global graphqlSubscription
        global HOST
        global subscriptionOperationName

        globToken = self._token
        SUB_ID = self.SUB_ID
        timeoutTimer = self.timeoutTimer
        timeout_interval = self.timeout_interval
        graphqlSubscription = self.graphqlSubscription
        HOST = self.HOST
        subscriptionOperationName = self.subscriptionName

    def connect(self):
        # Create the websocket connection to AppSync's real-time endpoint
        #  also defines callback functions for websocket events
        #  NOTE: The connection requires a subprotocol 'graphql-ws'

        # Uncomment to see socket bytestreams
        # websocket.enableTrace(True)
        if self._debug:
            print('Connecting to: ' + self.connectionUrl)
        self.ws = websocket.WebSocketApp(self.connectionUrl,
                                         subprotocols=['graphql-ws'],
                                         on_open=self.onOpen,
                                         on_message=self.onMessage,
                                         on_error=self.onError,
                                         on_close=self.onClose)
        # ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
        self.ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

    def stop(self):
        self.ws.close()

    def onMessage(self, ws, message):
        """Socket Event Callbacks, used in WebSocketApp Constructor"""

        global globToken
        global SUB_ID
        global timeoutTimer
        global timeout_interval
        global graphqlSubscription
        global HOST
        global subscriptionOperationName

        if self._debug:
            print('### message ###')
            print(f'<<  {message}')

        message_object = json.loads(message)
        message_type = message_object['type']

        if (message_type == 'ka'):
            resetTimer(ws)

        elif (message_type == 'connection_ack'):
            timeout_interval = int(json.dumps(
                message_object['payload']['connectionTimeoutMs']))
            register = {
                'id': SUB_ID,
                'payload': {
                    'data': graphqlSubscription,
                    # 'query': graphqlSubscription.query,
                    # 'variables': graphqlSubscription.variables,
                    'operationName': subscriptionOperationName,
                    'extensions': {
                        'authorization': {
                            'host': HOST,
                            'Authorization': globToken,
                            'Content-Type': 'application/graphql'
                        }
                    }
                },
                'type': 'start'
            }
            start_sub = json.dumps(register)
            if self._debug:
                print(f'>> {start_sub}')
            ws.send(start_sub)
        # elif (message_type == 'start_ack'):
        #     print
        elif (message_type == 'data'):
            deregister = {
                'type': 'stop',
                'id': SUB_ID
            }
            end_sub = json.dumps(deregister)
            if self._debug:
                print(f'>> {end_sub}')
            ws.send(end_sub)
            self.subscriptionMessageQueue.put(message_object)

        elif (message_object['type'] == 'error'):
            print(f"Error from AppSync: {message_object['payload']}")
            self.subscriptionErrorQueue.put(message_object)

    def onError(self, ws, error):
        if self._debug:
            print('### subscription websocket error ###')
            print(error)
            print()
        self.subscriptionErrorQueue.put(error)

    def onClose(self, ws, sec=None, thir=None, forth=None):
        if self._debug:
            print('### subscription websocket closed ###')
            print()

    def onOpen(self, ws):
        init = {
            'type': 'connection_init'
        }
        init_conn = json.dumps(init)
        if self._debug:
            print('### subscription websocket opened ###')
            print(f'>> {init_conn}')
            print()
        ws.send(init_conn)


def resetTimer(ws):
    """reset the keep alive timeout daemon thread"""
    global globToken
    global SUB_ID
    global timeoutTimer
    global timeout_interval
    global graphqlSubscription
    global HOST

    if (timeoutTimer):
        timeoutTimer.cancel()
    timeoutTimer = threading.Timer(
        timeout_interval, lambda: ws.close())
    timeoutTimer.daemon = True
    timeoutTimer.start()


# Calculate UTC time in ISO format (AWS Friendly): YYYY-MM-DDTHH:mm:ssZ


def headerTime():
    return datetime.utcnow().isoformat(sep='T', timespec='seconds') + 'Z'

# Encode Using Base 64


def headerEncode(header_obj):
    return b64encode(json.dumps(header_obj).encode('utf-8')).decode('utf-8')
