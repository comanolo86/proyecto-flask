from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Recibe el texto de la interfaz web, lo analiza y devuelve
    una respuesta formateada al usuario.
    """
    # Obtener el texto a analizar desde los parámetros de la URL
    text_to_analyze = request.args.get('textToAnalyze')

    # Llamar a la función de detección de emociones
    response = emotion_detector(text_to_analyze)

    # Si la respuesta es nula (error 400), mostrar mensaje de error
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    # Formatear la respuesta según los requisitos del proyecto
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is "
        f"<b>{response['dominant_emotion']}</b>."
    )

@app.route("/")
def render_index_page():
    """
    Renderiza la página principal de la aplicación.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
