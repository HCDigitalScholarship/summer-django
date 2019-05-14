---
layout: default
title: The Web, Beginning
nav_order: 4
---

Back to Basics, What is the Web?  

### [HTTP request methods](https://www.w3schools.com/tags/ref_httpmethods.asp) 
Talking to the 'net: [HTTP bin](https://httpbin.org/)

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


Our "textbook" the [Mozilla Django Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website)

