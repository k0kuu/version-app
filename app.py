import os
from flask import Flask, jsonify

app = Flask(__name__)
VERSION = os.environ.get("APP_VERSION", "unknown")

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/version")
def version():
    return {
        "version": VERSION,
        "hostname": os.environ.get("HOSTNAME", "?"),
        "build": "ci",   # ← add this line
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8000")))
