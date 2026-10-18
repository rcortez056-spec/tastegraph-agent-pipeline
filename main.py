import os
import requests
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

QLOO_API_KEY = os.getenv("QLOO_API_KEY", "").strip()
QLOO_BASE_URL = "https://hackathon.api.qloo.com/v2"

def query_taste_graph(entity_type: str, query_term: str):
    headers = {
        "X-Api-Key": QLOO_API_KEY,
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
        error_detail = e.response.text if e.response else str(e)
        return {"error": error_detail}

@app.route("/")
def index():
    html_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>TasteGraph Agent Pipeline</title>
            <style>
                body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 700px; margin: 60px auto; padding: 0 20px; color: #333; line-height: 1.6; background: #f9f9f9; }
                .card { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); border-top: 4px solid #0066cc; }
                h1 { color: #111; margin-top: 0; }
                .status { display: inline-block; background: #e6f4ea; color: #137333; padding: 4px 12px; border-radius: 12px; font-weight: 600; font-size: 14px; margin-bottom: 20px; }
                code { background: #f1f3f4; padding: 2px 6px; border-radius: 4px; font-family: monospace; }
                ul { padding-left: 20px; }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>TasteGraph Agent Pipeline</h1>
                <div class="status">● System Active & Healthy</div>
                <p>Welcome to the production deployment of the TasteGraph autonomous agent backend, hosted on Google Cloud Run.</p>
                <h3>Available Endpoints:</h3>
                <ul>
                    <li><code>GET /</code> - System Status & Overview (This Page)</li>
                    <li><code>POST /api/recommend</code> - Main agentic recommendation pipeline endpoint</li>
                </ul>
                <p><em>Built for hackathon evaluation. Check the GitHub Repository for full code and setup guides.</em></p>
            </div>
        </body>
    </html>
    """
    return render_template_string(html_content), 200

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
