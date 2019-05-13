import csv
import random
from flask import Flask, render_template


app = Flask(__name__)
application = app

@app.route('/<department>')
def by_subject(department):
    with open('courses.csv','r') as f:
        reader = csv.DictReader(f) 
        info = ""
        for row in reader:
            if department in row['department']:
                for i in row:
                    info += "<tr>" + "<th>"+ i +"</th>" + "<td>" + row[i] + "</td>" + "</tr>"
        return render_template('index.html', course_info=info)

@app.route("/")
def index():
    with open("courses.csv", "r") as f:
        reader = csv.DictReader(f)
        random_course = random.choice(list(reader))
        info = ""
        for i in random_course:
            info += "<tr>" + "<th>" + i + "</th>" + "<td>" + random_course[i] + "</td>" + "</tr>"
        return render_template('index.html', course_info=info)


if __name__ == "__main__":
    app.run()
