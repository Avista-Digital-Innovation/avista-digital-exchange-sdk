import requests
from .common import *

class Client:

    def __init__(self, token):
        self.APPSYNC_API_ENDPOINT_URL = 'https://annsvlcb4vew7msipwjyzzvyhi.appsync-api.us-west-2.amazonaws.com/graphql'
        self.token = token
        return
    
    def performQuery(self, queryString):
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
    