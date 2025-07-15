'''function to analyse a string using ibm watson.
'''
import json
import requests

def sentiment_analyzer(text_to_analyse):
    '''Function named sentiment_analyzer that takes a string input (text_to_analyse)
    '''
    # URL of the sentiment analysis service
    url = ('https://sn-watson-sentiment-bert.labs.skills.network/'
    'v1/watson.runtime.nlp.v1/NlpService/SentimentPredict')
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header, timeout=60)
    formatted_response = json.loads(response.text)
    label = None
    score = None
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    print((label, score))
    # Return the response text from the API
    return {'label': label, 'score': score}
