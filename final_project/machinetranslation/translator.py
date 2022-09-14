import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

language_translator.set_disable_ssl_verification(True)

def englishToFrench(englishText):
    '''
    Translating English text to French
    '''
    french_text_trans = language_translator.translate(text=englishText, model_id='en-fr').get_result()
    #frenchText0 = json.dumps(french_text_trans)
    #frenchText1 = json.loads(frenchText0)
    #frenchText = frenchText1['translations'][0]['translation']
    return french_text_trans.get('translations')[0].get('translation')

def frenchToEnglish(frenchText):
    '''
    Translating French text to English
    '''
    english_text_trans = language_translator.translate(text=frenchText,model_id='fr-en').get_result()
    englishText0 = json.dumps(english_text_trans,indent=2)
    englishText1 = json.loads(englishText0)
    englishText = englishText1['translations'][0]['translation']
    return englishText
