from watson_developer_cloud import AssistantV2
import json 

service = AssistantV2(
    version='2018-11-08',
    iam_apikey='BtmOQOR6pEBs-wtg2HyeUdLw_4lVpPech-dJ7Yte_1Cr',
    url='https://gateway-wdc.watsonplatform.net/assistant/api'
)


sessionID = service.create_session(
    assistant_id='d3bdd0a5-4f23-490b-98d4-1e258befb228'
).get_result()
print(sessionID["session_id"])

''' 
python3 watson_chat_test.py prints above
{
  "session_id": "7bc1ef4b-3bb5-4c90-91b2-9dc90debe4c4"
}
'''

response = service.message(
    assistant_id='d3bdd0a5-4f23-490b-98d4-1e258befb228',
    session_id= sessionID["session_id"],
    input={
        'message_type': 'text',
        'text': 'I want to know more about malware'
    }
).get_result()

print(json.dumps(response, indent=2))
