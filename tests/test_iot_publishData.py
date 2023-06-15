
from src.avista_digital_exchange_sdk import AvistaDigitalExchange
import math
import random
import time
import datetime


async def runTest(dxInstance: AvistaDigitalExchange, iotEndpointId: str):
    i = 0

    temp = random.uniform(40.0, 50.0)
    humidity = random.uniform(40.0, 45.0)
    pm = random.uniform(5.0, 15.0)
    while i < 100000:
        curTimeMs = int(math.floor(time.time() * 1000))
        temp = round(random.uniform(temp - .5, temp + .5), 3)
        if temp > 100.0:
            temp = 95.0
        if temp < -10.0:
            temp = -5.0
        humidity = round(abs(random.uniform(humidity - .5, humidity + .5)), 3)
        if humidity > 60.0:
            humidity = 55.0
        if humidity < 30.0:
            humidity = 35.0
        pm = round(abs(random.uniform(pm - .5, pm + .5)), 3)
        if pm > 30.0:
            pm = 25.0
        if pm < 1.0:
            pm = 3.0
        inputData = [{
            "timestamp": f'{curTimeMs}',
            "timeUnit": "MILLISECONDS",
            "attributes": {
                "Temperature": f'{temp}',
                "Humidity": f'{humidity}',
                "PM2_5": f'{pm}'
            }
        }
        ]

        result = dxInstance.iot.publish(
            iotEndpointId, inputData)
        print(result)
        result = dxInstance.iot.updateEndpointProperties(
            iotEndpointId, {
                'LastReading': {
                    'value': f'{datetime.datetime.now()}'
                }
            })
        print(result)

        time.sleep(1)
