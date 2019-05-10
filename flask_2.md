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
