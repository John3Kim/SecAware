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

print("Hello. Welcome to SecAware! What can I help you with? I can help you learn about various IT concepts.")

user_text = input("Respond, then press ENTER.")

while(user_text != "exit" or user_text != "quit"):

    response = service.message(
        assistant_id='d3bdd0a5-4f23-490b-98d4-1e258befb228',
        session_id= sessionID["session_id"],
        input={
            'message_type': 'text',
            'text': user_text
        }
    ).get_result()

    text_response = json.dumps(response)
    text_response = response["output"]["generic"][0]["text"]
    print(text_response) 

    user_text = input("Respond, then press ENTER.")

 