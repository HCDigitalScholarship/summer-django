---
layout: default
title: Django Views 
nav_order: 2
parent: Thursday 
---

Now that you have updated models.py and run migrations we can turn to adding and retrieving data from the database and serving it to a dynamic HTML template.

```python
from my_app.models import Fish
all_fish = Fish.objects.all()
```
This equivalent to a query of all values in a table:
```sql
SELECT * from my_app_fish;
```
Note that you have the option to [send raw queries](https://docs.djangoproject.com/en/2.2/topics/db/sql/), it's just a lot more complicated that way: `all_fish = Fish.objects.raw('SELECT * from my_app_fish;')`

Our `all_fish` variable is a Django queryset object.  You can find the documentation on them here: [queryset objects](https://docs.djangoproject.com/en/2.2/ref/models/querysets/#queryset-api).

The most common ways that you'll request data from the data base is either with `all()` or 

- `Model.objects.filter()` with a field and value. `Fish.objects.filter(type='trout')`, for example, will return all the trout records. 

-`Model.objects.get()` will get a single record.  `Fish.objects.filter(id=1)`

When adding records to the database, we very often rely on the `update_or_create()` function.  This will check if an existing record exists, in which case it updates the existing record. Otherwise it creates a new record.  

```python
data = {'fish':{'name':'Sammy','type':'shark'}}
name = data['fish']['name']
type = data['fish']['type']
Fish.object.update_or_create(name=name, type=type)  
```

Q objects
