import csv
import random
from flask import Flask, render_template


app = Flask(__name__)
application = app 


@app.route("/")   #This is the root URL. We can also create an absolute path @app.route("/about") or a relative one @app.route("/<user>")   
def index():
    with open("courses.csv", "r") as f:
        reader = csv.DictReader(f)
        random_course = random.choice(list(reader))
        info = ""
        for i in random_course:
            info += i + ":  " + random_course[i] + "<br>"
        return info


if __name__ == "__main__":
    app.run()
