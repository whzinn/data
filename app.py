from flask import Flask, render_template, request, redirect, url_for
import os
import time

app = Flask(__name__)

@app.route('/clique')
def clique():
    return f"Pagina Online"
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
