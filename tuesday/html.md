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
    <p>It feels just like 1996 again, in my high school computer lab. The computer lab manager was also my swim coach, Mr. Neat. Sometimes we would have class in the computer lab and learn how to make very basic web pages, but my primary engagement with the Web was through America Online. To open a web page, I had to: </p>
    <ul>
        <li>Make sure no one was on the phone.</li>
        <li>Open the AOL program</li>
        <li>Listen to the modem call a phone number and connect</li>
        <li>Open the browser in AOL and type in an address for a web page</li>
    </ul>
    <p>It was not the most soothing sequences of sounds. It sounded like <a href="https://www.youtube.com/watch?v=D1UY7eDRXrs">this</a>!</p>
</body>

</html>
```

What do you think each element does? Do some elements seem different in structure than others?

The <a href="https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/HTML_text_fundamentals">text fundamentals section</a> of the Mozilla HTML Tutorial will guide us on the basics of HTML. Read through it and create a new HTML file that tells us something about you. What are you interested in? What are your hobbies? What have your favorite classes been? Save the file with the ".html" extension
