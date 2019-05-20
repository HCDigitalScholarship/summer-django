---
layout: default
title: Github Workflow
nav_order: 3
parent: Wednesday 
---

## .gitignore 
The .gitignore file defines which files and file types will be ignored by git.  That means it won't track changes in those files.  More importantly, it will not push those files to your online repository.  If you push an API key or a database password or private information to GitHub, it's free for the world to see.  There are spiders crawling GitHub looking for AWS passwords or any information that will help crack your application.  .gitignore is very easy to use and can save you from accidentally telling the world that one password you use for everything: `Pa$$word123`.

> Go to [gitignore.io/](https://gitignore.io/) and enter "Django" and create.  What kinds of files does it include in .gitignore?

[Here is a good compilation of .gitignore rules](https://github.com/github/gitignore/blob/master/Python.gitignore).  You won't need all of them for your project, but it never hurts to ignore things.  

Here is the [.gitignore](https://github.com/HCDigitalScholarship/django-showcase-2/blob/master/.gitignore) for our showcase app: 
```
.venv
__pycache__
*.pyc
*.pyo
.mypy_cache

/static_collected
*.log
*.sqlite3

*.swp
~*
.DS_Store
```
