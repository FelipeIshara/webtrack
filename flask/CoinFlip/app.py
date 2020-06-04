import random
from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def index():
    number = random.randint(0,1)
    return render_template("coinflip.html", number=number)

if __name__ == "__main__":
    app.run()
