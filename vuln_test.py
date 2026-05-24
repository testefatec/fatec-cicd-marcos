from flask import Flask

app = Flask(__name2__)

@app.route("/")
def hello():
    return "ok"

if __name2__ == "__main__":
    app.run(debug=True)
