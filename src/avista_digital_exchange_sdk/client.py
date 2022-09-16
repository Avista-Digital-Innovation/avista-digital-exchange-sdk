import requests
from . import globals


class Client:

    def __init__(self, token):
        APPSYNC_API_ENDPOINT_URL_dev = 'https://annsvlcb4vew7msipwjyzzvyhi.appsync-api.us-west-2.amazonaws.com/graphql'
        APPSYNC_API_ENDPOINT_URL_prod = 'https://rrfs7pb7ancybo7bom7uxcsaxq.appsync-api.us-west-2.amazonaws.com/graphql'
        self.token = token
        if globals.stage == "PRODUCTION":
            self.APPSYNC_API_ENDPOINT_URL = APPSYNC_API_ENDPOINT_URL_prod
        else:
            self.APPSYNC_API_ENDPOINT_URL = APPSYNC_API_ENDPOINT_URL_dev
        return

    def performQuery(self, queryString):
        print(queryString)
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
        print(mutationString)
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
