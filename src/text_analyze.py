from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EmotionOptions


def analyze_emotions(emotion_dict):
    if emotion_dict['anger'] > 0.5:
        return "triggered"
    elif emotion_dict['joy'] > 0.5:
        return "joy"


def get_emotions(text):
    text = f'<i>{text}</i>'
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2018-11-16',
        iam_apikey='vcfJHb4lqz67pevf5vnqdOqVe-bOtFefMqUG5Q3c4ha2',
        url='https://gateway-lon.watsonplatform.net/natural-language-understanding/api'
    )
    response = natural_language_understanding.analyze(
        html=text,
        features=Features(emotion=EmotionOptions())).get_result()

    emotions = analyze_emotions(response['emotion']['document']['emotion'])
    return emotions