## Part II 

Now that we have some data to work with, we can start working on a web application. We'll start by creating a simple "course of the day" application that will randomly pick a course from our dataset and display information in the browser.  Later, we're going to publish the application to the web using [sites.haverford.edu](sites.haverford.edu).  If time permits, we can try a more advanced chatbot following this [tutorial](https://pusher.com/tutorials/chatbot-flask-dialogflow).   

While it's not common, you can write an application in pure Python.      



Flask is one of the simplest Python web frameworks available and has a lot in common with Django.



```python
import csv
import random
from flask import Flask


app = Flask(__name__)
application = app


@app.route("/")
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
```
