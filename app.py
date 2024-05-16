from flask import Flask, render_template, request, redirect, url_for
import os
import time
from db import incrementa_acesso

app = Flask(__name__)

@app.route('/')
def main():
    return "ok"


@app.route('/clique/<ip>')
def clique(ip):
    d = incrementa_acesso(ip)
    return d
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
