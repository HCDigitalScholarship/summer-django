---
layout: default
title: Introduction to Django 
nav_order: 1
parent: Wednesday 
---

![](https://www.marc-richter.info/wp-content/uploads/2018/08/Django_Pony-632x208.png)


Using the [Django](https://docs.djangoproject.com/en/2.2/) documentation and [Mozilla tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website), we will:
- Install django in a virtual envorionment `conda create python=3 <env_name>` or `virtualenv --p python3 <env_name>`
- Create a project
- Create an app using `python manage.py startapp <app>`
- Add our new app to settings.py
- Run migrations 
- Create a superuser
- create subdirectories in the app directory for templates and static
- Test with runserver

> I try to be consistent in the language I use.  The `project directory` is the directory that was created with `django-admin startproject <project_name>`.  That directory contains `settings.py` and other global assets.  An `application directory` is created when you run `startapp` or add a third-party Django application (there are tons of them [here](https://djangopackages.org/)).  You can think of these as modules that we've imported to our central project. 
  

**Part II**
Create a simple webpage with Django:
- create a path for our index page in our app's `urls.py`
- create a view for our index page `path('', views.index, name='index'),`
- create a `base.html` template
- create an `index.html` file that extends `base.html`
- create a footer.html 
- runserver!

**Part III**
Add images and links using the [Django template language](https://docs.djangoproject.com/en/2.2/ref/templates/language/) 
- Add images to the app's static directory
- Add another path to urls.py.


