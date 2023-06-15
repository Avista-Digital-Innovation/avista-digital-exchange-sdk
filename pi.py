queryResult = [{'id': '1234', 'value': 'hello'}]
queryResultDict = {}

for record in queryResult:
    queryResultDict[record["id"]] = record["value"]

pointsList = [
    'iotEndpointId.1234',
    'edoid1234',
    'attributeName'
]

# pointsDict = {
#     endpointId: [{'edoid': '111', 'attributeName': name},{'edoid': '1112': 'attributeName': 'another'}]
# }

pointsDict = {}
for i in range(len(pointsList)):
    iotEndpointId = pointsList[i][0]
    edoId = pointsList[i][1]
    attributeName = pointsList[i][2]

    if iotEndpointId in pointsDict:
        pointsDict[iotEndpointId].append({
            'edoId': edoId,
            'attributeName': attributeName
        })
    else:
        pointsDict[iotEndpointId] = [{
            'edoId': edoId,
            'attributeName': attributeName
        }]

publishData = []

for endpointId, attributes in pointsDict:
    newPublishData = {iotEndpointId: endpointId, attributes: []}
    for i in range(len(attributes)):
        if attributes[i]["edoId"] in queryResultDict:
