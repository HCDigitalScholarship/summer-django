---
layout: default
title: Django Models 
nav_order: 1
parent: Thursday 
---
## Models 
During this session, please feel free to consult the [Django Tutorial](https://docs.djangoproject.com/en/2.2/intro/tutorial02/)
and the [Mozilla Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models) tutorials on models. 

What is a model?  It is a Python object that the Django ORM (object-relational mapper) uses to make databases seem familiar and friendly for Pythonistas. One of the key adavantages of this approach is that developers can use multiple databases and types of databases without having to learn the subtile differences between a query in MySQL or postgres.  We going to do that anyway, but not just right now. 

As a quick reminder, Python is an object oriented language, so you've been using objects all along even if you didn't know it. 
Here's a very simple object in Python from the GAM project:

```python 
class CurrentItem:
    def __init__(self, name, letters):
        self.name = name
        self.letters = letters
```
To create a current item object, just use `current_item = CurrentItem`
We can set or update the values for name and letters with `current_item.name = item_name` or `current_item.letters`


Model.objects.filter()
Model.objects.get()
Model.object.update_or_create()
[queryset objects](https://docs.djangoproject.com/en/2.2/ref/models/querysets/)
Q objects

