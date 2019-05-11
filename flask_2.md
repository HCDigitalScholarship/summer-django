## Part II 

Now that we have some data to work with, we can start working on a web application. We'll start by creating a simple "course of the day" application that will randomly pick a course from our dataset and display information in the browser.  Later, we're going to publish the application to the web using [sites.haverford.edu](sites.haverford.edu).  If time permits, we can try a more advanced chatbot following this [tutorial](https://pusher.com/tutorials/chatbot-flask-dialogflow).   

While it's not common, you can write an application in pure Python.      

```python
# https://docs.python.org/3/howto/sockets.html
# https://stackoverflow.com/questions/8627986/how-to-keep-a-socket-open-until-client-closes-it
# https://stackoverflow.com/questions/10091271/how-can-i-implement-a-simple-web-server-using-python-without-using-any-libraries
import csv
import random
import socket 

def createServer():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try :
        serversocket.bind(('localhost',9000))
        serversocket.listen(5)
        while True:
            (clientsocket, address) = serversocket.accept()

            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            if ( len(pieces) > 0 ) : print(pieces[0])

            with open("courses.csv", "r") as f:
                    reader = csv.DictReader(f)
                    random_course = random.choice(list(reader))
                    course_text = ""
                    for i in random_course:
                        course_text += i + ":  " + random_course[i] + "<br>"
                    data = "HTTP/1.1 200 OK\r\n"
                    data += "Content-Type: text/html; charset=utf-8\r\n"
                    data += "\r\n"
                    data += "<html><body>{}</body></html>\r\n\r\n".format(course_text)
                    clientsocket.sendall(data.encode())
                    clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt :
        print("\nShutting down...\n");
    except Exception as exc :
        print("Error:\n");
        print(exc)

    serversocket.close()

print('Access http://localhost:9000')
createServer()
```


Flask is one of the simplest Python web frameworks available and has a lot in common with Django.
Create a new folder called `flask_app`.
- Create app.py in the `flask_app` directory
- Download [courses.csv](https://github.com/HCDigitalScholarship/summer-django/raw/master/courses.csv) to the `flask_app` directory
- create a subfolder templates for our index.html file
- create a static subfolder for our main.css file

```
flask_app
    ├── .env
    ├── app.py
    ├── requirements.txt
    ├── static
    │   └── main.css
    └── templates
        └── index.html
```

**app.py**
```python
import csv
import random
from flask import Flask, render_template


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
In the terminal run `$ python app.py`

We can now serve content from our csv file to the web.  Without any styling, it's really ugly.  Let's add some HTML and CSS to make this look better.   

We'll need to make a few small changes to the application so that we're rendering an HTML template and not just sending text to the browser. Change the app to the following:

```python
info = ""
for i in random_course:
    info += "<tr>" + "<th>"+ i +"</th>" + "<td>" + random_course[i] + "</td>" + "</tr>"
return render_template('index.html', course_info=info)
```

Create an index.html file in a new `templates` directory (`mkdir templates`).  Second, create `static/css/main.css`. 

**/templates/index.html**
```HTML
<!DOCTYPE>
<html>

<head>
    <link rel="stylesheet" href="{{ url_for('static', filename='main.css') }}" 
</head>

    <body>

        <table style="width:100%">

            {{ course_info|safe }}

        </table>

    </body>

</html>

```
**/static/main.css**
```css
@import url('https://fonts.googleapis.com/css?family=Cinzel');

table {
  border-collapse: collapse;
  width: 80%;
}

td, th {
  font-family: 'Cinzel', serif;
  border: 1px solid #4C061D;
  text-align: left;
  padding: 12px;
}

tr {
  background-color: #ffffff;
}

```
> Note the `@import url()`. This comes from [Google Fonts](https://fonts.google.com/).  You can use any of their thousands of multi- lingual fonts, just by adding this import to your css.  For example, `@import url('https://fonts.googleapis.com/css?family=Roboto');` and then `font-family: 'Roboto', sans-serif;`


*your page should look something like this*  
![](https://github.com/HCDigitalScholarship/summer-django/raw/master/pink_course.png) 

The cycle of life is complete.  You've taken data from the web and can now serve it back to your browser. In the next section, we discuss how to deploy your application using sites.haverford.edu. 

[continue...](https://github.com/HCDigitalScholarship/summer-django/blob/master/flask_3.md)
