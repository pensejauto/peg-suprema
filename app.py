from flask import Flask, render_template, jsonify
import json, os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/store")
def store():
    with open("products.json", encoding="utf-8") as f:
        products = json.load(f)
    return render_template("store.html", products=products)

@app.route("/api/products")
def api_products():
    with open("products.json", encoding="utf-8") as f:
        products = json.load(f)
    return jsonify(products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))