from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "hi, chel"

@app.route("/about")
def about():
    return "Flask #1: Что это такое? Простое WSGI-приложение"

if __name__ == "__main__":
    app.run(debug=True, port=5050)