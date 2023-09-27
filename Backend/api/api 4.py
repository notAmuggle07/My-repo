#http://localhost:5000/detect?text=こんにちは
#Used the above link to get output. Not sure if this is the required output, but this is my attempt.
from flask import Flask, request, jsonify
from googletrans import Translator
from langdetect import detect

app = Flask(__name__)

translator = Translator()

@app.route('/detect', methods=['GET'])
def language_detection():
    text = request.args.get('text')

    if not text:
        return jsonify({"error": "Text parameter is required."})

    try:
        detected_language = detect(text)

        # Use Google Translate to get the language name
        language_info = translator.translate(detected_language, src='auto', dest='en')

        response_data = {
            "detected-lang": detected_language,
            "lang-name": language_info.text,
            "source-text": text
        }

        return jsonify(response_data)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run()