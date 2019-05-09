This is a page for the section on creating and deploying a Flask app to the web 


Let's get some data for our app: 
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
            courses[id]['url'] = url

```
