import json
import world_manager
import storage_service

wm = world_manager.WorldManager(storage_service.StorageService())

def get_area(event, context):
    try:
        area = event['queryStringParameters']['area']
    except:
        pass
    try:
        region = event['queryStringParameters']['region']
    except:
        pass
        
    areaData = wm.get_area(region, area)
    if areaData is None:
        responseCode = 404
    else:
        responseCode = 200

    body = {
        "area": areaData
    }

    response = {
        "statusCode": responseCode,
        "body": json.dumps(body)
    }

    return response
