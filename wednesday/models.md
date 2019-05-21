---
layout: default
title: Django Models 
nav_order: 2
parent: Wednesday 
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

Python 3.7+ comes with a [native dataclass object](https://realpython.com/python-data-classes/).

```python
from dataclasses import dataclass

@dataclass
class Course:
    campus: str    # 'campus' has no default value
    semester: str
    title: str
    credit: int = 1  # assign a default value for 'credit'
    department: str
    instructor: str
    times: str
    room: str 
    additional_info: str
    misc_links: str
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

![](https://mdn.mozillademos.org/files/16479/local_library_model_uml.png)
- [ManytoMany](https://docs.djangoproject.com/en/2.1/ref/models/fields/#manytomanyfield)

```python
class Persona(models.Model):
    """A person."""

    nombre_de_la_persona = models.CharField(max_length=200, null=True)
    nombre = models.CharField(max_length=200, blank=True)
    segundo = models.CharField(max_length=200, blank=True)
    apellido_paterno = models.CharField(max_length=200, blank=True)
    apellido_materno = models.CharField(max_length=200, blank=True)
    fecha_de_nacimiento = models.CharField(max_length=200, blank=True)
    fecha_desaparicion = models.CharField(max_length=200, blank=True)
    edad_en_el_momento = models.CharField(max_length=200, blank=True)
    género = models.CharField(max_length=200, blank=True)
    etnicidad = models.CharField(max_length=200, blank=True)
    profesión = models.CharField(max_length=200, blank=True)
    actividades_políticas = models.ManyToManyField('Organización', blank=True)
    # relaciones = models.ManyToManyField('Relación', blank=True)
    image = models.ManyToManyField('Imagen', blank=True)
    notas = RichTextField(blank=True)

    def __str__(self):
        return self.nombre_de_la_persona

    def get_absolute_url(self):
        return "/persona/%i/" % self.id
```

vs.
- [ForeignKey](https://docs.djangoproject.com/en/2.1/ref/models/fields/#foreignkey)

```python
class Caja(models.Model):
    """A folder."""

    archivo = models.ForeignKey('Archivo', on_delete=models.CASCADE, default=1)
    colección = models.ForeignKey('Colección', on_delete=models.CASCADE, default=1)
    número_de_caja = models.CharField(max_length=200, blank=True)
    carpetas = models.ManyToManyField('Carpeta', blank=True, related_name='carpetas')
    departamento = models.ManyToManyField(
        Lugar, blank=True, related_name='departamento'
    )
    municipios = models.ManyToManyField(Lugar, blank=True, related_name='municipios')
    letras = models.CharField(max_length=200, blank=True)
    legajos = models.CharField(max_length=200, blank=True)
    fechas_extremas = models.CharField(max_length=200, blank=True)
    volumen_en_metros_lineales = models.CharField(max_length=200, blank=True)
    sistema_digital = models.CharField(max_length=200, blank=True)
    descripción = RichTextField(blank=True, default='')

    def __str__(self):
        return '{}/{}/{}'.format(self.archivo, self.colección, self.número_de_caja)
```


## RichTextField
```
from ckeditor.fields import RichTextField
RichTextField(blank=True, default='')
```

## Migrations 

Keep in mind that your models.py file is a set of instructions to Django on how to structure your database.  Any changes that you make to models need to be applied to the database using `manage.py makemigrations` and then `manage.py migrate`.  These commands generate a migrations file (such as ./migrations/0001_initial.py) with step-by-step instructions to update the database.  You should not need to change them, but it's good to understand the process.  For a more in depth discussion of migrations, see this [Real Python primer](https://realpython.com/django-migrations-a-primer/).  

