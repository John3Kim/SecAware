from watson_developer_cloud import VisualRecognitionV3
import json

'''
try:
    # Invoke a Visual Recognition method
    except WatsonApiException as ex:
    print "Method failed with status code " + str(ex.code) + ": " + ex.message
'''

visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    iam_apikey='0AgXfDBcMbIo26ZRKZuWAOhApEiyyBgOK-KmYXYeBhaj',
    url="https://gateway.watsonplatform.net/visual-recognition/api"
)


with open('./macos-mojave-notarized-app-alert-dark.jpg', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        threshold='0.0'#,owners=["me"]
        ).get_result()
    print(json.dumps(classes, indent=2))
