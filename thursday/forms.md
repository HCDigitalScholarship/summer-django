---
layout: default
title: Forms 
nav_order: 3
parent: Thursday
---

Forms! 

```python
ef index(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        search_form = SearchForm(request.POST)

        if form.is_valid() or search_form.is_valid():
            campus = request.POST.get('campus', None)
            semester = request.POST.get('semester', None)
            title = request.POST.get('title', None)
            search_query = request.POST.get('search', None)

            search_result = \
                Course.objects.annotate(
                search = SearchVector('title') + SearchVector('instructor'),
                ).filter(search=search_query)

            now = datetime.datetime.now()
            return render(request, 'index.html', {'current_date': now, 'form': form, 'search':search_form, 'search_result': search_result})

    else:
        form = CourseForm()
        search_form = SearchForm()
        now = datetime.datetime.now()
        return render(request, 'index.html', {'current_date': now, 'form':form, 'search':search_form})
```
