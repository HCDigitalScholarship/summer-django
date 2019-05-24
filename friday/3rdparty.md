---
layout: default
title: Third-Party Apps
parent: Friday
nav_order: 1
---

A showcase of our favorite 3rd party apps and how we use them. 

## Where to find apps
1) [Django Packages](https://djangopackages.org/) is a great place to start
2) [Github](https://github.com/search?q=Django&type=Repositories)

## Apps that we have used and like
- [Registration](https://github.com/ubernostrum/django-registration): A great app for managing external user accounts.  Create a new account, receive an email with a validation code, all the features you'd expect, but you don't have to code. 

- [CKEditor](https://github.com/django-ckeditor/django-ckeditor): Adds a very nice richtext model field that can handle text formatting (bold, italic and so on).  We use it together with Django's native flat-pages app to create an interface where users can easily add content to a project, including text, images and other HTML elements, from the admin panel. 

- [Google Map Widget](https://github.com/erdem/django-map-widgets)

- [Autocomplete-light](https://github.com/yourlabs/django-autocomplete-light): Lets you easily add autocomplete fields to front-facing forms.  Note that autocomplete_fields is a built-in option in Django 2.0+, but only works in admin.  
```python
class ChoiceAdmin(admin.ModelAdmin):
    autocomplete_fields = ['question']
```

- [Django Haystack](https://github.com/django-haystack/django-haystack): Is a relatively easy way to create and manage search indexes.

- [Django Channels](https://github.com/django/channels): Is currently the most accepted way to add [async](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/Synchronous_and_Asynchronous_Requests) to Django.  Note that Tornado in an effective alternative to Django if async is an key feature of your app. 

- [jQuery datatables](https://datatables.net/): Is an easy way to serve data to a template in a spreadsheet-like grid with search, sort and filter capabilities.  It can also be used in a variety of languages.  

- [Openseadragon](https://openseadragon.github.io/): Is a javascript library and a relatively simple way to serve deep zoom images.  A DZI is a tree of image directories, with small tiles coresponding to a particular zoom level.  The user can seamlessly zoom in very very close and then out without seeing the transitions.  We use dzis for transcription work and other applications where users need to look a small details in an image.   
