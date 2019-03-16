from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EmotionOptions


def analyze_emotions(emotion_dict):
    emotions_namings = ['sadness', 'joy', 'disgust', 'anger', 'fear']
    sad, joy, disgust, anger, fear = emotion_dict['sadness'], emotion_dict['joy'], emotion_dict['disgust'],\
                                     emotion_dict['anger'], emotion_dict['fear']
    emotion_list = [sad, joy, disgust, anger, fear]
    for emotion in emotion_list:
        if not 0.4 < emotion < 0.7:
            break
        return "pokerface"
    conflicts = [0]*5
    if sad >= 0.7:
        return "sadness"
    elif sad <= 0.4:
        if joy >= 0.7:
            return "joy"
        elif joy <= 0.4:
            if disgust >= 0.7:
                return "disgust"
            elif disgust <= 0.4:
                if anger >= 0.7:
                    return "anger"
                elif anger <= 0.4:
                    if fear >= 0.7:
                        return "fear"
                    elif fear <= 0.4:
                        return "smile"
                    else:
                        conflicts[4] = fear
                else:
                    conflicts[3] = anger
            else:
                conflicts[2] = disgust
        else:
            conflicts[1] = joy
    else:
        conflicts[0] = sad
    maximun = max(conflicts)
    for i in range(5):
        if conflicts[i] == maximun:
            return emotions_namings[i]


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


print(get_emotions(''))