# Django Lab 3
## Build a REST API
### Assigned Week 5, February 19; due February 26, by 5:29 PM

**Purpose**: Design and implement a simple Django API service.  

**Artifacts**
* Codebase in GitHub COMP 705-805 organization (github.com/comp705-805) for
lab3 Django API project with **config** and **music** packages
* **lab3log** in your Google Drive learning portfolio

### Getting Started
In your Google Drive learning portfolio  
1. Create **lab3log** in your Google Drive learning portfolio. Use it to
    1. Log all the development tasks and steps
    2. Indicate success or briefly describe issues you had and how you resolved
    them.
    3. During the incremental development process, for each commit:
        1. Include commit message and commit link
        2. Brief explanation of the purpose of the change within the context of
        Django REST API architecture and API service design.
        3. Include a link to the official documentation supporting your answer

In GitHub COMP 705-805 organization

2. Accept invitation from
[https://classroom.github.com/a/XXXX](https://classroom.github.com/a/XXX)
to have a **lab3-xxx** remote repository created in github.com/comp705-805

On your machine

3. Activate your Python 3.7.2 virtual environment.

4. Packages you have already installed are **pycodestyle** and **requests**

Use ```pip freeze``` to check. The output you get should be
```
certifi==2018.11.29
chardet==3.0.4
idna==2.8
pycodestyle==2.5.0
requests==2.21.0
urllib3==1.24.1
```
Install them if you don't have them installed

5. Install the latest official Django package 2.1.7 and Django REST API framework (DRF)
```
(first-venv) $ pip install Django==2.1.7
(first-venv) $ pip install djangorestframework
```
Check with ```pip freeze``` that you have the django installations

### Create Django API project structure

1. Go to **labs** directory ```cd ~/workspace/labs``` and create lab3 with README.md
in it
```
(first-venv) $ mkdir lab3
(first-venv) $ cd lab3
(first-venv) $ touch README.md
```
**lab3** is the root-level directory for your **_Django API project_**

2. Create a Python package, **config**, in your Django API project **lab3**
```
(first-venv) $ django-admin startproject config .
```
Notice the dot . at the end of the command above. Very important!  
The structure of the Django API project **lab3** is:
```
lab3
├── README.md
├── config
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└──  manage.py
```

3. Inspect the content of **config** package. On my machine it has the following content
```
drwxr-xr-x  6 mcs_admin  staff   204 Feb 16 09:56 .
drwxr-xr-x  5 mcs_admin  staff   170 Feb 16 09:56 ..
-rw-r--r--  1 mcs_admin  staff     0 Feb 16 09:56 __init__.py
-rw-r--r--  1 mcs_admin  staff  3097 Feb 16 09:56 settings.py
-rw-r--r--  1 mcs_admin  staff   751 Feb 16 09:56 urls.py
-rw-r--r--  1 mcs_admin  staff   395 Feb 16 09:56 wsgi.py
```
**config** is a Python package: it has ```__init__.py```

Open **lab3** in Atom to easily move into **config** package and its modules:
**settings.py**, **urls.py**, and **wsgi.py**

4. Create another package that will have the API implementation for your project.
    1. Go into **lab3**
    2. Run ```(first-venv) $ django-admin startapp music```, where **music** is the name of the resource for which we create the API.
    3. Inspect the structure of your lab3 Django project with ```$ tree -L 2```. The output should be
```
lab3
├── README.md
├── config
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── music
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    ├── models.py
    ├── tests.py
    └── views.py
```

### Start version control
1. Turn your **lab3** into a Git repository
    1. Be in the root-level directory for your **_Django API project_**, that is
    **lab3**
    2. Run ```$ git init```
    3. Check with ```$ tree -L 3``` that **lab3** is now a repository: should have **.git** directory

2. Configure local repository **lab3** to synchronize its changes with the remote location of **lab3-xxx** in [https://github.com/comp705-805](https://github.com/comp705-805)

    1. Get the URL of the remote repo **lab3-xxx**
    2. On your machine, run ```$ git remote add school <remote URL>```
        1. Note that we picked a different name for this location
        2. This is it to give your practice with configuring multiple remotes for your repo
    3. Check that your local repo is configured to push to **school** remote  
    ```$ git remote show school```

3. Add all local changes made in **lab3** to the commit history
    1. Check what changes have occured, that is, see all the **_untracked_*** *files with ```$ git status```
    2. Stage all changes with ```$ git add``` and check with ```$ git status```
    3. Commit all staged changes
    ```
    $ git commit -m 'created Django API project with packages config and music'
    ```
    and check again with ```$ git status```

4. Synchronize local changes with **school** remote:
    1. ```$ git push school master``` and check with ```$ git status```
    2. Go to the remote repo **lab3-xxx** in [https://github.com/comp705-805]
    (https://github.com/comp705-805) and refresh page to see your commit
    3. Get commit link and paste it **lab3log**

### Setup database and create initial user

1. Be in **lab3** and run the following commands in bash
    ```
    $ python manage.py migrate
    $ python manage.py createsuperuser
    ```
    Enter credentials that are identical to your UNH credentials, so you don't forget them.

2. Open **config/settings.py** in Atom to add **'rest_framework'** and
**'music'** to INSTALLED_APPS list:
    1. Notice the single quotes: these are string values
    2. Notice that we use , after the last item in the list.
    It's good practice to prepare the list for adding other string values.
```
INSTALLED_APPS = [
   ...
   'rest_framework',
   'music',
]
```

Version development steps 1 and 2 above

3. Time to commit this change
    1. Check untracked files with ```git status```, stage with ```git add```,
    make the commit with MEANINGFUL message, check again with ```git status```
    2. Synchronize your local repo with the remote repo by pushing local commit history
    to **school** remote ```$ git push school master```
    3. Go to remote repo, check the new commit, get the link, paste it in **lab3log**.

4. Open **config/urls.py** and add the following changes:
```
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('music.urls')),
]
```

Version development step 4 above

5. Commit and publishing time!
    1. Check status, stage, check status again, commit, check status, publish changes, check status
    2. Check remote and get the commit link. Paste it in **lab3log**.  

### Test-Driven Development AND Logging Development Tasks/Steps

1. Read the **_Test-Driven Development_** section in Emmanuel King Kasulani (2018). See **References** section below.
    * Note that your **config** package is called **api** in King Kasulani's example.

2. Follow King Kasulani's instructions to **create an endpoint** that lists all
the entries in the **music** resource.

3. When trying to view the endpoints in your browser you need to start the
django development server. The command is ```$ python manage.py runserver```.

4. In parallel with development work log tasks/steps as instructed at
**Getting Started**, item **1**.

### Trace Execution

* import **pdb** module in **test.py**
* Add **pdb.set_trace()** before the first line of code in your testing method
* Run ```$ python manage.py test```
* Use Python debugger commands, **list**, **next** and/or **step**, and **pp**
<variable name> to better understand what gets executed and what what values
the testing method variables take.
* Commit and publish this last change.
* In **lab3log** include a brief descriptions of your findings and any questions
you might have about the trace and the use of the debugger.

### Reference

Emmanuel King Kasulani. 2018. Let’s build an API with Django REST Framework.
[https://medium.com/backticks-tildes/lets-build-an-api-with-django-rest-framework-32fcf40231e5](https://medium.com/backticks-tildes/lets-build-an-api-with-django-rest-framework-32fcf40231e5).
Project repository on GitHub at: https://github.com/kasulani/drf_tutorial

Jon Shallow. 2019. lab3-drf-api-example repository with list all pilots action
on pilots resource. See GitHub Classroom invitation in 5sp slide presentation.

### Grading

* **lab3log**: 1 point
* Implementation: 1 point
* Documentation and version control: 1 point
    * All modules, classes, and methods have docstrings
    * All commits document your development process.
