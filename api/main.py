from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({
        "message": "BNRA API v1.0",
        "status": "running",
        "endpoints": {
            "health": "/api/health",
            "threat_detection": "/api/threat/detect"
        }
    })

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": "2024-01-29T10:00:00Z",
        "version": "1.0.0"
    })

@app.route('/api/threat/detect', methods=['POST'])
def detect_threat():
    data = request.json
    return jsonify({
        "is_threat": False,
        "confidence": 0.85,
        "message": "Threat analysis completed"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
