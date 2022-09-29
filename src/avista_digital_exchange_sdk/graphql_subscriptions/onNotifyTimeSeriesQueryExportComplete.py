from time import sleep
from .subscription import *
from ..exceptions import *
from .. import globals
from ..data_types.time_series_query_export import TimeSeriesQueryExport

from threading import Thread
from queue import Queue


class onNotifyTimeSeriesQueryExportComplete(Subscription):

    def __init__(self, client, debug, queryId):
        super().__init__(client, debug,
                         "onNotifyTimeSeriesQueryExportComplete", TimeSeriesQueryExport)
        if queryId is None:
            raise MissingParameterException("Missing queryId")
        self.queryId = queryId

        self.subscriptionMessageQueue = Queue()
        self.subscriptionErrorQueue = Queue()

    def _getSubscriptionQueryString(self):
        return f'''subscription {self.subscriptionName} 
        {{ 
            {self.subscriptionName}(queryId: "{self.queryId}") {self.resultType.getQueryString()} 
        }}'''

    def initiateSubscriptionOnNewThread(self):
        print(f'Creating subscription for time series result export completion...')
        self.subscriptionClient = self._client.getSubscriptionClient(
            self.subscriptionName,
            self._getSubscriptionQueryString(),
            self.subscriptionMessageQueue,
            self.subscriptionErrorQueue)

        self.subscribedThread = Thread(
            target=self.subscriptionClient.connect)
        self.subscribedThread.start()

        return self.subscribedThread

    def endSubscription(self):
        self.subscriptionClient.stop()
        self.subscribedThread.join()

    def waitForResponse(self, maxWaitSeconds):
        i = 0
        done = False
        while not done:
            i += 1
            if self._debug:
                print('subscription message queue:')
                print(list(self.subscriptionMessageQueue.queue))
                print()

                print('subscription error queue')
                print(list(self.subscriptionErrorQueue.queue))
                print()

            if self.subscriptionMessageQueue.qsize() > 0:
                self.endSubscription()
                item = self.subscriptionMessageQueue.get()
                if self.queryId == item['payload']['data'][self.subscriptionName]['queryId']:
                    print(
                        f'Received notification that export is ready for download')
                    self._result = item['payload']
                    return self._processResult()
                else:
                    raise Exception(
                        "Missing data in export success notification")
            elif self.subscriptionErrorQueue.qsize() > 0:
                raise Exception(
                    f'Encountered error when waiting for query export file: {self.subscriptionErrorQueue.get()}')

            if i == maxWaitSeconds:
                self.endSubscription()
                raise Exception(
                    'Timed out waiting for export complete notification')
            else:
                print('waiting...')
                sleep(1)

    def _processResult(self) -> TimeSeriesQueryExport:
        super()._processResult()
        try:
            print('received export complete notification')
            self.queryExport = TimeSeriesQueryExport(
                self._result['data'][self.subscriptionName], self._client, self._debug)
            if self._debug:
                print(f'DEBUG - Result {self.queryExport}')
            return self.queryExport
        except Exception as e:
            raise e
