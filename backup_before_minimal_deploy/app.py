from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.get("/")
def home():
    return "UVA SDS GPT Echo App is running!"

@app.post("/api/echo")
def echo():
    data = request.get_json(silent=True) or {}
    text = (data.get("text") or "").strip()
    return jsonify({"reply": (text + "?") if text else "?"}), 200

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
