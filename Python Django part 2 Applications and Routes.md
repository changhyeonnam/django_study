# Python Django part 2  Applications and Routes

Created: Mar 2, 2021 7:52 PM

1.  Adding a blog application to Django site 
2.  Setting up some URL routes so that can start directing people to pages that we'd like them to see. 

---

```python
# blog/views.py
from django.http import HttpResponse
def home(request) :
	return HttpResponse('<h1>Blog Home<h1>') # home view function

def about(request):
	return HttpResponse('<h1>Blog About<h1>') # about view function
```

this is the log for how we want to handle when a user goes to our blog homepage. 

[urls.py](http://urls.py) : map the urlls that we want to correspond to each view function. it's in project level too. 

```python
#/blog/urls.py
from django.urls import path
from . import views
urlpatterns = [
	path('', views.home, name='blog-name'),
	path('about/', views.about, name='blog-about'), 
	#don't need to add path for project urls.py for adding about. 
]
```

second argument of path : specify the view that we want to handle the logic at that homepage route. 

reason for name : time that we want to do a reverse look-up on this route.

→ URL path for our blog hompage mapped to our home funciton in views file. 

we have [urls.py](http://urls.py) file in main project also. that urls module will tell our whole website which urls should send us to our blog app. 

```python
#/django_urls.py/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.siteurls),
	path('blog/', include('blog.urls')),
]
```

Tell Django which route should get mapped to our blog URLs.  

include : add to our list of URL pattern to specify which route should go to our blogs URLs. path('blog/', include('blog.urls')) : go to '/blog' then it will map to 'blog.urls'. then in blog/urls.py : empty path '' maps on to home view. 

include : only send the remaing string to the included URLs module for further processing. 

(skip for regular experssion for route)

if we want to change route to our blog application then we can simply change that in oneplace and it applies to all of those routes. Go to project's urls file, and simply change the path. if we change 'blog/' in to 'blog_dev/', then we can access with /blog_deb/about(or home). we don't need to change anything within our actual blog application. 

reason for slash in path : by default if it has trailing slash, then django will redirect routes without a forward slash so that no one ever gets confused about what routes are not returning the same results. 

What if we want [localhost:8000](http://localhost:8000) to be a blog page : 'blog/' → '' (empty).

```bash
cd django_project
virtualenv venv
python manage.py startapp blog
python manage.py runserver 
```