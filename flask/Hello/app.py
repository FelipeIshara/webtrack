from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello")
def hello():
    name = request.form.get("name")
    if not name:
        return render_template("error.html")
    else:
        return render_template("hello.html", name=name)

if __name__ == "__main__":
    app.run()