---
layout: default
title: Sockets
parent: Tuesday
nav_order: 1
---

## What is the Web?  
![](https://maqentaer.com/devopera-static-backup/http/devfiles.myopera.com/articles/356/article3_1.gif)

### [HTTP request methods](https://www.w3schools.com/tags/ref_httpmethods.asp) 

- [HTTP bin](https://httpbin.org/)

- With Python, we can easily create a socket and send requests.  Below is a simple client script with a GET request.  For more a more detailed discussion of sockets Real Python has a wonderful tutorial [Socket Programming in Python](https://realpython.com/python-sockets/) by Nathan Jennings. Try pasting the [script below](https://github.com/HCDigitalScholarship/summer-django/raw/master/tuesday/socket.py) into a Python shell.  

```python
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.gutenberg.org', 80))
cmd = 'GET http://www.gutenberg.org/files/120/120-0.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
```

You can also easily GET with the [Python requests library](https://realpython.com/python-requests/)
```python
import requests
response = requests.get('http://data.pr4e.org/romeo.txt')
```
Experiment by looking at `response.status_code`,`response.content`, and `response.text`;
or use the native Python urllib,
```python
import urllib.request
response = urllib.request.urlopen('http://www.google.com')
```

