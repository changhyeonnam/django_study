# Python Django  01

Created: Mar 2, 2021 7:52 PM

Tutorial from  Python Django Tutorial: Full-Featured Web App Part 1 - Getting Started

---

How to build full featured web application using the Django Framework.

What will be building in this series of videos

- blog style applcation
- differenct user can write different post : blog, twitter update whatever
- authentication system : log out, log in, regsiter, forgot password? resest password, email.
- profile, pitcure
- post : update, delete.
- admin : backend information and update it on the fly.

→ database system, authentication system, user input from form, send email. 

django-admin : list of subcommand 

startproject : make a new django project for us that has a complete struture with different files and everything else that we'll need to get started. 

[manage.py](http://manage.py) , django project directory 

- [manage.py](http://manage.py) : allow us to run command line commands, we won't any change in this file
- django_project directory
    - __init__.py: empty file. just tells python that this is a python package
    - __settings__.py : we'll using the through out the series, good document.
        - SECRET_KEY→ add a lots of security enhancements to Django.
        - Debug =True.
        - installed app section.
        - database settings
    - [urls.py](http://urls.py): set up the mapping from certain urls to where we sent the user.
        - ex) one path pattern

        ```python
        urlpatterns = [
            path('admin/', admin.site.urls),
        ]
        ```

        go to our site and go to the route admin then it will send us to this admin.site.urls. add some additional routes

    - [wisgi.py](http://wisgi.py) : how our python web appliation and the web sever communicate. django set up a simple default whiskey configuration for us. actually not touching this file.

To run our sever, access our sit, runserver. 

```bash
sudo pip3 install virtualenv
# create a virtual environment within the project directory by typing
virtualenv newenv
# To install packages into the isolated environment, 
# you must activate it by typing this.
source newenv/bin/activate

#install django
pip install django

#startproject
django-admin startproject [projectname]

#run server
python manage.py runserver
```

[http://127.0.0.1:8000](http://127.0.0.1:8000/)/admin : [urls.py](http://urls.py) → path('admin/', admin.site.urls)