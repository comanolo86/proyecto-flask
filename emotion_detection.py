import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analiza un texto para detectar emociones y maneja errores de entrada vacía.
    """
    # URL del servicio de Watson NLP
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Encabezados
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Cuerpo de la solicitud
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Envío de la petición POST
    response = requests.post(url, json = myobj, headers = headers)
    
    # Lógica para manejar el código de estado 400 (Error de solicitud/Entrada vacía)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Conversión de la respuesta exitosa
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        # Extraer las puntuaciones de las emociones
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        
        # Determinar la emoción dominante
        dominant_emotion = max(emotions, key=emotions.get)
        
        return {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }
