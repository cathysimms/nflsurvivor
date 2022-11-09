from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Home page"

@app.route("/<username>")
def user(username):
    return f"Hi {username}"

if __name__ == "__main__":
    app.run()

