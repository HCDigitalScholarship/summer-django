---
layout: default
title: HTML
parent: Tuesday
nav_order: 2
---

## What is HTML?

The web is essentially made up of text files. These text files are sent to the client when a request is made, and a web browser renders a page based on the contents of the text file. These files are given meaning by Hypertext Markup Language, HTML. HTML is a simple language of elements and attributes that gives a text document structure and meaning, which is interpreted by the browser.

## An HTML Document
Elements are identified with _tags_ that open and close sections of a document. Tags are marked by angle brackets, as they are in any XML document:

Opening tags contain the name of the element enclosed by angle brackets (`<span>`) while closing tags are identical but for a leading forward slash (`</span>`). In between the opening and closing tags is the information contained within that element. Elements can be nested, creating a hierarchical structure for the document.

Let's take the following example:

```
<!DOCTYPE html>
<html>

<head>
    <title>My First Page</title>
</head>

<body>
    <h1>Welcome to my HTMl page!</h1>
    <p>It feels just like 1996 again. Try opening me in Netscape Navigator.</p>
</body>

</html>
```

