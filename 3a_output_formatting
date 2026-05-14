import requests
import json

def emotion_detector(text_to_analyze):
    # URL del servicio de Watson NLP
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Encabezados
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Cuerpo de la solicitud
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Envío de la petición POST
    response = requests.post(url, json = myobj, headers = headers)
    
    # Conversión de la respuesta de texto a JSON (diccionario)
    formatted_response = json.loads(response.text)

    # Lógica para manejar la respuesta exitosa
    if response.status_code == 200:
        # Extraer las puntuaciones de las emociones
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']
        
        # Determinar la emoción dominante basándose en la puntuación más alta
        dominant_emotion = max(emotions, key=emotions.get)
        
        # Formato de salida requerido por la Actividad 1
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    
    # Manejo de error (por ejemplo, entrada vacía) según las instrucciones del curso
    elif response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
