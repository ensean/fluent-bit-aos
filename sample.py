import base64
import json
import requests
from requests.auth import HTTPBasicAuth

host = 'https://vpc-xxxxxx.ap-northeast-1.es.amazonaws.com' # the OpenSearch Service domain, e.g. https://search-mydomain.us-west-1.es.amazonaws.com
index = 'tickit'    # index name
url = host + '/_bulk'

basic = HTTPBasicAuth('admin', 'xxxxx')    # AOS username & password
headers = { "Content-Type": "application/json" }

def lambda_handler(event, context):
    count = 0
    payloads = '\n'
    for record in event['Records']:
        id = record['eventID']
        timestamp = record['kinesis']['approximateArrivalTimestamp']
        # Kinesis data is base64-encoded, so decode here
        message = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        
        # if message is json, then parse it
        message = json.loads(message)
        # Create the JSON document
        document = { "id": id, "timestamp": timestamp, "message": message }

        # construct bulk operations
        payloads += json.dumps({"index": {"_index": index, "_id": id}}) + '\n'
        payloads += json.dumps(document) + '\n'
        count += 1
    r = requests.put(url, auth=basic, data=payloads, headers=headers)
    return 'Processed ' + str(count) + ' items.'
