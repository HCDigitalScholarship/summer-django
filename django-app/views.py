from django.shortcuts import render
import random
import csv

def index(request):
    with open("courses.csv", "r") as f:
        reader = csv.DictReader(f)
        random_course = random.choice(list(reader))
        info = ""
        for i in random_course:
            info += "<tr>" + "<th>" + i + "</th>" + "<td>" + random_course[i] + "</td>" + "</tr>"
        return render(request, 'index.html', {'course_info': info})
