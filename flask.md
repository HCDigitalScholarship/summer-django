This is a page for the section on creating and deploying a Flask app to the web 


Let's get some data for our app.  I going to fetch course information from the Haverford Registrar's [courses page](https://www.haverford.edu/academics/courses).  I'm going to get the url for a full search of every class offered at Haverford, Swarthmore and Bryn Mawr this coming fall. Looking at the results page, I can see a few important things:
`https://www.haverford.edu/academics/results?semester%5B0%5D=fall_2019&college%5B0%5D=bryn_mawr&college%5B1%5D=haverford&college%5B2%5D=swarthmore&page=1&per_page=50`  
Notice the `&page=1` in the URL.  I can change that and I'll get the second page of results. If you right click and view the page source, you can see that all of the information I'd want is contained in the table <tbody></tbody> tags.  Using a Python library called [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), I can parse the HTML to get the information that we want. I'll use the requests library to fetch the HTML from the web.  Note that there are 51 pages of results. `range(1,52)` move through each page of search results and scrape the results.  You'd need to update that value for a different search.  

```python 
import requests
from bs4 import BeautifulSoup
courses = {}

for i in range(1,52):
    page = requests.get('https://www.haverford.edu/academics/results?semester%5B0%5D=fall_2019&college%5B0%5D=bryn_mawr&college%5B1%5D=haverford&college%5B2%5D=swarthmore&page={}&per_page=50'.format(i))
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
This can take some time and saves the results in memory. To save the `courses` dictionary, we can either save it as a binary pickle or a csv.  

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
        row = courses[course]
        writer.writerow(row)
```
    
    
