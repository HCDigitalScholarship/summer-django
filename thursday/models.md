---
layout: default
title: Django Models 
nav_order: 1
parent: Thursday 
---
## Models 
During this session, please feel free to consult the [Django Tutorial](https://docs.djangoproject.com/en/2.2/intro/tutorial02/)
and the [Mozilla Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models) tutorials on models. 

What is a model?  It is a Python object that the Django ORM (object-relational mapper) uses so that databases are familiar and friendly for Pythonistas. One of the key adavantages of this approach is that developers can use multiple databases and types of databases without having to learn the differences between a query in MySQL or postgres.  We'll discuss sql queries later on so that you understand what's going on under the hood of the ORM.     

Python is an object oriented language. Here's a very simple object in Python from the GAM project:

```python 
class CurrentItem:
    def __init__(self, name, letters):
        self.name = name
        self.letters = letters
```

To create a current item object, just use `current = CurrentItem`
We can set or update the values for name and letters with `current.name = item_name` or `current.letters`

Python 3.7+ comes with a [native dataclass object](https://realpython.com/python-data-classes/), which is an elegant way to define a data class object. 

```python
from dataclasses import dataclass

@dataclass
class CurrentItem:
    name: str
    letters: str
```

---
In a Django model we add fields to the model. Note that there are many data types.  The most common is Charfield, for a string.  For a full list of model field types [documentation](https://docs.djangoproject.com/en/2.2/ref/models/fields/#model-field-types).:

```python
from django.db import models

class Fish(models.Model):
    """A model for adding fish to the database."""

    # Fields
    name = models.CharField(max_length=200, help_text='The fish's prefered name')
    type = models.CharField(max_length=20, help_text='The type of fish')
    date_of_birth = models.DateField(auto_now=False)
    has_fins = models.BooleanField(null=True)
    
    def __str__(self):
        return self.name
```

Note the __str__ method.  This defines what is displayed in the admin interface (we'll get to that soon). 
You can also add methods to the model. For example, for age"

```python
import datetime 
    ... 
    def age(self):
        dob = self.date_of_birth
        now = datetime.datetime.now().date()
        age = now - dob
        return age.days / 365
```

## ManytoMany and Foreign Key

## RichTextField
```
from ckeditor.fields import RichTextField
RichTextField(blank=True, default='')
```
Model.objects.filter()
Model.objects.get()
Model.object.update_or_create()
[queryset objects](https://docs.djangoproject.com/en/2.2/ref/models/querysets/)
Q objects

