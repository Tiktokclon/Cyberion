from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Clé API privée (insérée ici)
API_KEY = "msOkIKsYs5ChIdDO8UW9Fi_oBTA5vuvxyXMNGF1SNiA"

@app.route('/v1/completions', methods=['POST'])
def completions():
    auth = request.headers.get("Authorization", "")
    if auth != f"Bearer {API_KEY}":
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    prompt = data.get("prompt", "")
    max_tokens = data.get("max_tokens", 100)

    # Exemple simple de réponse (à remplacer par ton modèle)
    response_text = f"Réponse simulée à : {prompt}"

    return jsonify({
        "id": "chatcmpl-123",
        "object": "text_completion",
        "choices": [{"text": response_text}],
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
