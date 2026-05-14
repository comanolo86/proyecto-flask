from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Recibe el texto de la interfaz web, lo procesa mediante el detector de emociones
    y maneja los casos de error para entradas inválidas o en blanco.
    """
    # Obtener el texto a analizar de los parámetros de la consulta
    text_to_analyze = request.args.get('textToAnalyze')

    # Pasar el texto a la función emotion_detector
    response = emotion_detector(text_to_analyze)

    # Extraer la emoción dominante y las puntuaciones
    dominant_emotion = response['dominant_emotion']
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']

    # Lógica de manejo de errores: Si la emoción dominante es None, la entrada fue inválida
    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    # Retornar la respuesta formateada si la entrada fue válida
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is <b>{dominant_emotion}</b>."
    )

@app.route("/")
def render_index_page():
    """
    Renderiza la página de inicio de la aplicación Flask.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Ejecución de la aplicación en el host y puerto especificados
    app.run(host="0.0.0.0", port=5000)
