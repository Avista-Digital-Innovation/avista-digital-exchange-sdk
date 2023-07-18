
from logging import Logger
from typing import AsyncIterator, List
from .async_graphql_client import exceptions, input_types
from .client import Client as DxClient
from . import DxTypes


class DataCaptureUtil(object):
    _debug: bool
    _client: DxClient
    _logger: Logger

    def __init__(self, debug: bool, client: DxClient, logger: Logger):
        self._debug = debug
        self._client = client
        self._logger = logger

    async def listenForCaptureData(self, captureId: str) -> AsyncIterator[DxTypes.PublishCaptureDataResult]:
        if self._debug:
            print("Subscribing to capture data....")
        async for item in self._client.updatedGqlClient.on_capture_publish_data(
                capture_id=captureId):
            if self._debug:
                print("DataCapture.listenForCaptureData: Data received.")
            result = DxTypes.PublishCaptureDataResult.fromCapturePublishResult(
                item.on_capture_publish_data)
            yield result

    async def publishData(self, captureId: str, data: List[DxTypes.CaptureDataRecordInput]) -> DxTypes.PublishCaptureDataResult:
        if self._debug:
            print("DataCapture.publishData: - processing data input")

        # Format data records argument
        dataRecords: List[input_types.DataCaptureDataRecordInput] = []
        for record in data:
            attributeValues: List[input_types.DataCaptureAttributeValueInput] = [
            ]

            # Create attributeValues array
            for attributeId, attributeValue in record.attributeValues.items():
                attrValue: input_types.DataCaptureAttributeValueInput = input_types.DataCaptureAttributeValueInput(
                    userDefinedId=attributeId, value=f'{attributeValue}')
                attributeValues.append(attrValue)

            dataRecord = input_types.DataCaptureDataRecordInput(
                attributeValues=attributeValues, timestamp=f'{record.timestamp}')
            dataRecords.append(dataRecord)

        result: DxTypes.PublishCaptureDataResult
        try:
            if self._debug:
                print("DataCapture.publishData - performing publish")

            mutationResult = await self._client.updatedGqlClient.data_capture_publish_data(
                capture_id=captureId, data=dataRecords)
            if self._debug:
                print(
                    f'DataCapture.publishData - publish result: {mutationResult.data_capture_publish_data}')
            result = DxTypes.PublishCaptureDataResult.fromCapturePublishResult(
                mutationResult.data_capture_publish_data)
        except exceptions.GraphQLClientHttpError as err:
            if self._debug:
                print(
                    f"ERROR: DataCapture.publishData.ClientError: '{err}'")
            # result = DxTypes.PublishCaptureDataResult(
            #     captureId=captureId, success=False, error=f"Client error: '{err}'")
            raise err
        except exceptions.GraphQLClientGraphQLMultiError as err:
            if self._debug:
                print(
                    f"ERROR: DataCapture.publishData.MultiError: '{err}'")
            # result = DxTypes.PublishCaptureDataResult(
            #     captureId=captureId, success=False, error=f"{err}")
            raise err
        except Exception as err:
            if self._debug:
                print(f"ERROR: DataCapture.publishData.Error: '{err}'")
            # result = DxTypes.PublishCaptureDataResult(
            #     captureId=captureId, success=False, error=f"Unknown error: '{err}'")
            raise err
        if self._debug:
            print(
                f'''DataCapture.publishData result: {result}''')

        return result

    async def startCapture(self, captureId: str) -> DxTypes.StartCaptureResult:
        result: DxTypes.StartCaptureResult
        try:
            if self._debug:
                print("Calling dataCapture_startCapture mutation")

            mutationResult = await self._client.updatedGqlClient.data_capture_start_capture(
                capture_id=captureId)
            if self._debug:
                print(
                    f'Mutation raw result: {mutationResult.data_capture_start_capture}')
            result = DxTypes.StartCaptureResult(
                captureId=captureId, success=True, startedAt=mutationResult.data_capture_start_capture.time_settings.actual_start_time)
        except exceptions.GraphQLClientHttpError as err:
            if self._debug:
                print(
                    f"ERROR: DataCapture.startCapture.ClientError: '{err}'")
            result = DxTypes.StartCaptureResult(
                captureId=captureId, success=False, error=f"Client error: '{err}'")
            raise err
        except exceptions.GraphQLClientGraphQLMultiError as err:
            if self._debug:
                print(
                    f"ERROR: DataCapture.startCapture.MultiError: '{err}'")
            result = DxTypes.StartCaptureResult(
                captureId=captureId, success=False, error=f"{err}")
            raise err
        except Exception as err:
            if self._debug:
                print(f"ERROR: DataCapture.startCapture.Error: '{err}'")
            result = DxTypes.StartCaptureResult(
                captureId=captureId, success=False, error=f"Unknown error: '{err}'")
            raise err
        if self._debug:
            print(
                f'''DataCapture.startCapture result: {result}''')

        return result

    async def stopCapture(self, captureId: str) -> DxTypes.StopCaptureResult:
        if self._debug:
            print("DataCapture.stopCapture")
        result: DxTypes.StopCaptureResult
        try:
            if self._debug:
                print("Calling dataCapture_stopCapture mutation")

            mutationResult = await self._client.updatedGqlClient.data_capture_stop_capture(
                capture_id=captureId)
            if self._debug:
                print(
                    f'Mutation raw result: {mutationResult.data_capture_stop_capture}')
            result = DxTypes.StopCaptureResult(
                captureId=captureId, success=True, stoppedAt=mutationResult.data_capture_stop_capture.time_settings.actual_stop_time)
        except exceptions.GraphQLClientHttpError as err:
            if self._debug:
                print(
                    f"ERROR: DataCapture.stopCapture.ClientError: '{err}'")
            result = DxTypes.StopCaptureResult(
                captureId=captureId, success=False, error=f"Client error: '{err}'")
            raise err
        except exceptions.GraphQLClientGraphQLMultiError as err:
            if self._debug:
                print(
                    f"ERROR: DataCapture.stopCapture.MultiError: '{err}'")
            result = DxTypes.StopCaptureResult(
                captureId=captureId, success=False, error=f"{err}")
            raise err
        except Exception as err:
            if self._debug:
                print(f"ERROR: DataCapture.stopCapture.Error: '{err}'")
            result = DxTypes.StopCaptureResult(
                captureId=captureId, success=False, error=f"Unknown error: '{err}'")
            raise err

        if self._debug:
            print(
                f'''DataCapture.stopCapture result: {result}''')

        return result
