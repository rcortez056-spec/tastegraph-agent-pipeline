import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

QLOO_API_KEY = os.getenv("QLOO_API_KEY")
QLOO_BASE_URL = "https://api.qloo.com/v1"

def query_taste_graph(entity_type: str, query_term: str):
    headers = {
        "X-API-Key": QLOO_API_KEY,
        "Accept": "application/json"
    }
    params = {
        "filter": query_term,
        "limit": 5
    }
    try:
        response = requests.get(f"{QLOO_BASE_URL}/{entity_type}", headers=headers, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
@app.route("/")
def index():
    return "TasteGraph Agent Pipeline Active", 200
@app.route("/api/recommend", methods=["POST"])
def recommend_pipeline():
    data = request.json
    entity_type = data.get("entity_type", "movies")
    query_term = data.get("query", "Sci-Fi")
    
    graph_results = query_taste_graph(entity_type, query_term)
    
    return jsonify({
        "status": "success",
        "entity_type": entity_type,
        "query": query_term,
        "results": graph_results
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
