import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)



language_translator = LanguageTranslatorV3(
    version='2022-01-17',
    authenticator=authenticator
)
language_translator.set_service_url(url)




def english_to_french(eng_text):
    frenchtext = None
    if eng_text is not None:
        frenchtext = language_translator.translate(
        text=eng_text,
        model_id='en-fr').get_result()['translations'][0]['translation']
    return frenchtext

def french_to_english(fre_text):
    englishtext = None
    if fre_text is not None:
        englishtext = language_translator.translate(
        text=fre_text,
        model_id='fr-en').get_result()['translations'][0]['translation']
    return englishtext
