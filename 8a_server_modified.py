"""
Módulo del servidor Flask para el Detector de Emociones.
Proporciona una interfaz web para analizar las emociones en un texto dado
utilizando el servicio Watson NLP.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analiza el texto proporcionado por el usuario y devuelve un mensaje
    con las puntuaciones de las emociones y la emoción dominante.
    Maneja entradas inválidas devolviendo un mensaje de error.
    """
    # Obtener el texto de los parámetros de la solicitud
    text_to_analyze = request.args.get('textToAnalyze')

    # Obtener la respuesta del detector de emociones
    response = emotion_detector(text_to_analyze)

    # Extraer los valores del diccionario de respuesta
    dominant_emotion = response['dominant_emotion']
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']

    # Verificar si la entrada es válida
    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    # Retornar la respuesta formateada según los requisitos
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is <b>{dominant_emotion}</b>."
    )

@app.route("/")
def render_index_page():
    """
    Renderiza la página de inicio (interfaz de usuario) de la aplicación.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Iniciar la aplicación Flask
    app.run(host="0.0.0.0", port=5000)
