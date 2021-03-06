---
layout: default
title: Flask, Part I
parent: Monday
nav_order: 1
---

## Python Web Applications  
Welcome to Digital Scholarship.  In the following section, we're going to quickly build and deploy a Python web appication so that you can get a feel for the development process from beginning to end.  We'll also cover some useful skills and tricks as well as point you to resources that will help you in your work over the summer.  

<img style="width=10%;" src="https://cdn-images-1.medium.com/max/1200/1*vdSIa2rFEAZS1YUsgOZR0A.jpeg">

--- 

To get started, let's get some data.  
- I'm going to fetch course information from the Haverford Registrar's [courses page](https://www.haverford.edu/academics/courses).  
![](https://github.com/HCDigitalScholarship/summer-django/raw/master/search-results.png)  

- Let's run a search and get the url for a full search of every class offered at Haverford, Swarthmore and Bryn Mawr this coming Fall. 
- Looking at the results page URL, I can see my query `semester=fall_2019`, `college=bryn_mawr` `&haverford` and so on:  

```
https://www.haverford.edu/academics/results?semester%5B0%5D=fall_2019&college%5B0%5D=bryn_mawr&college%5B1%5D=haverford&college%5B2%5D=swarthmore&page=1&per_page=50    
```

- Notice the `&page=1` in the URL.  I can change that and I'll get the second page of results.  

- If you right click, inspect and view the page source, you can see that all of the information I'd want is contained in the table <tbody></tbody> tags.  Using a Python library called [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), I can parse the HTML to get the information that we want.

- I'll use the requests library to fetch the HTML from the web.  Note that there are 51 pages of results. `for i in range(1,52)` will change the page `&page={i}` and scrape each page of results.  You'd need to update that value for a different search.  Note that I'm using an [f-string](https://realpython.com/python-f-strings/) to update the url.  If you using a version earlier than 3.6, you'll need to use `'&page={}'.format(i)` or `&page=%d' % i`.  

```python 
import requests
from bs4 import BeautifulSoup
courses = {}

for i in range(1,52):
    page = requests.get(f'https://www.haverford.edu/academics/results?semester%5B0%5D=fall_2019&college%5B0%5D=bryn_mawr&college%5B1%5D=haverford&college%5B2%5D=swarthmore&page={i}&per_page=50')
    soup = BeautifulSoup(page.text, 'html.parser')
    course_table = soup.tbody  #This selects all of the content between the <tbody> </tbody> tags
    links = course_table.find_all('a', href=True)
    #First, let's create a dictionary for each of the classes using the registration id.  We will also record the URL for the class record.
    for link in links:
        if 'mailto' in link['href']:
            pass
        else:
            id = link.text
            url = link['href']
            courses[id] = {}
            courses[id]['url'] = 'https://www.haverford.edu/' + url

```

Now that we have a dictionary of course ids and their urls, I can visit each individual course page to fetch the data.  
![](https://github.com/HCDigitalScholarship/summer-django/raw/master/individual_page.png) 

For each course, I'll add the campus, semester, title, number of credits, department and so on.

```python
for course in courses:
    url = courses[course]['url']
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    courses[course]['campus'] = soup.find("td", text="Campus").find_next_sibling("td").text
    courses[course]['semester'] = soup.find("td", text="Semester").find_next_sibling("td").text
    courses[course]['title'] = soup.find("td", text="Course Title").find_next_sibling("td").text
    courses[course]['credit'] = soup.find("td", text="Credit").find_next_sibling("td").text
    courses[course]['department'] = soup.find("td", text="Department").find_next_sibling("td").text
    courses[course]['instructor'] = soup.find("td", text="Instructor").find_next_sibling("td").text
    courses[course]['times'] = soup.find("td", text="Times and Days").find_next_sibling("td").text
    courses[course]['room'] = soup.find("td", text="Room Location").find_next_sibling("td").text
    courses[course]['additional_info'] = soup.find("td", text="Additional Course Info").find_next_sibling("td").text
    courses[course]['misc_links'] = soup.find("td", text="Miscellaneous Links").find_next_sibling("td").text
```
This can take some time and will save all of the data into memory so be careful with large datasets. 

---

To save the `courses` dictionary, we can either save it as a binary pickle or a csv.  

```python
import pickle
pickle.dump(courses, open("courses.pickle", "wb" ))
```
or 

```python
import csv
with open('courses.csv','w') as f:
    field_names = ["url","campus","semester","title","credit","department","instructor","times","room","additional_info","misc_links"]
    writer = csv.DictWriter(f, field_names)
    writer.writeheader()
    for course in courses:
        writer.writerow(courses[course])
```
Please feel free to try and adapt the code above.  You can also download the [csv here](https://github.com/HCDigitalScholarship/summer-django/raw/master/courses.csv) or the [pickle file](https://github.com/HCDigitalScholarship/summer-django/raw/master/courses.pickle).

[continue...](https://hcdigitalscholarship.github.io/summer-django/monday/flask_2.html)
    
