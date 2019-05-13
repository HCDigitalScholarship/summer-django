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
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
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
response.status_code
response.content
response.text
```

Our "textbook" the [Mozilla Django Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website)

