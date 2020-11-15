from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Template, FileSystemLoader, Environment
from typing import Dict, Text
import redis

templates = FileSystemLoader('templates')
environment = Environment(loader = templates)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("tiny.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
