https://github.com/hussain-mustafa990/automax_django_web_app

### VS code Extensions
Django by Robert Solis
Django template by bibhasdn
Material Icon by Philip kief
Django by Baptiste Darthenay


### 1- Create project file
```
mkdir my_project
cd my_project
```

### 2- Create virtaul env named `env`
```
python -m venv env
```

### 3- Activate the env
```
source env/bin/activate
```


### 4- Install django in your virtualenv and check for django sub-commands using the django-admin.
```
python -m pip install django
python -m pip show django
django-admin help
```

### 5- start project inside the project folder
```
django-admin startproject automax
```
- Change the name of the main-level folder of the project from automax to src. i.e the folder that contains subfolders called automax and manage.py

### 6- run the development server
```
python manage.py runserver
```
### NOTE:
- Manage.py file: 
The manage.py file is a utility file that allows us interact with our project via the commandline. from the `src` folder run the `python manage.py --help` command to see a list of commands that can be used to interact with your projects. An example is the command we used to run the development server earlier. Another example is the `python manage.py migrate` that will be used below for migrations.

- Migrations: Django has a built-in ORM i.e object relation mapper. ThIS basically abstracts away the complexity of interacting with a database.The ORM allows us to write python code that can interact with a sql databse on it's own. When we make changes to our code, they need to translated to sql code, that is MIGRATION. 
After these migrations have been done and we have sql code, we need to instruct django to APPLY THESE MIGRATIONS TO THE DATABASE so that the DB has an updated schema and can interact with our application. 

The use the `python manage.py migrate` command to instruct django to apply the migrations.  

### Understanding the Django Project structure
- src: This is the source of everything.
- automax: This reflects the name we gave the project when it was started. This sub-folder is an app within the django app. every other app that we will create during the course of creating the project will be linked to this app. Django projects are generally a composition of smaller sub-apps that come together to form the complete application.

A section/app will be used sorely for authenticating users, another section/app will be used for the views/landing page. All these apps will be attached to the main app i.e the automax app so that it has the ability to authenticate users. But all the logic pertaining to authentication is kept containerized within the  authentication app.


<!-- -->
### Models

Models are a representation of our database schema.
We use models to rep the structure of that data. We write them by using python classes. Example

Let's create a class `lead`, this class will inherit from `models.model`. The `.model` is a python class inside the python file and that is what we want our class to inherit from.

While creating our model `lead` we will create different Properties that will help us represent what the data in a lead database will look like.
Below we will create a database table with 3 columns i.e firtname, lastname and age

### RELATIONSHIP BETWEEN TABLES.
Relationships btw tables are normal. Example we are using a CRM, we have leads in a lead table. These leads will be pursued by agents, that means we have to find a way to assign these leads to agents in a different agent table. We use a 'ForeignKey' for that.

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)



class Agent(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    <!-- lead = models.ForeignKey("Lead", on_delete=models.CASCADE) -->
   

What the above means is that every lead is created with it's own agent. There could be thousands of leads in the database but each will have it's own agent.
If the ForeignKey was in the Agent database(as commented out), that means we are saying that every agent can only have 1 lead, so if we have hundreds of leads, then we will not have enough agents.

Django Built-In User Model.(1.11.00) 
Django has an in-built user model 'AbstractUser', you can find this in the env folder, this model already has a lot of lay-outs/columns that you will use, but you are advised to create your own model so that you can customize it. So what we do is to create our own model, but our model inherits from the django User model's ('AbstractUser'). The `Agent class` changeS FROM A to B below because the fields `firstname anad lastname` are already in the `AbstractUser Model` we are inheriting from. 
```
A

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
```
```
B
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
```

### Model Managers
The concept of Model managers in Django Models is to help us manipulate the model class easier. Example the model below:
Video Title: python shell and model managers.
```
class Car(models.Model):
    
    CAR_MANUFACTURERS = (
       ('Audi', 'Audi'),
       ('BMW', 'BMW'),
       ('Ferrari', 'Ferrari'),

    )
    make = models.CharField(max_length=20, choices=CAR_MANUFACTURERS)
    model = models.CharField(max_length=20)
    year = models.IntegerField(default=2015)

```


To access the car manager you use:
Car.objects

This calls the manager and gives us access to a whole bunch of methods e.g: We can use the manager to:


1- To create a new car on the database
`Car.objects.create(make="BMW", model="X5", year=2017)`

#### Querysets
2- Query for all cars in the database
`car.objects.all()`

3- Querry for cars with the make equal to "Audi"
`car.objects.filter(make="Audi")`

4- Query for cars with a year greater than 2016
`car.objects.filter(make="year__gt=2016")`


NOTE: Whenever you are querying a database i.e filtering or retrieving a list of rows from the database, the datatype is called a QUERYSET. We can loop over these Querysets or do much complex things on them. 


### Python Shell 1:32:20
Video Title: python shell and model managers.
We will use the python shell to play around with Model managers
```
$ python manage.py shell
$ from leads.models import Lead
$ Lead.objects.all()
$ from  django.contrib.auth import get_user_model
$ CustomUser = get_user_model()
$ CustomUser.objects.all()

$ from leads.models import Agent
$ admin_user = CustomUser.objects.get(username = 'ozor')
$ admin_user
$ Agent.objects.create(user=admin_user)

$ from leads.models import Lead
$ ozor_agent = Agent.objects.get(user__email="ozor@gmail.com")
$ ozor_agent
$  Lead.objects.create(first_name="joe", last_name="soap", age="39", agent=ozor_agent)
```

![python shell 1](./journal_images/python%20shell%201.png)

Note that when we use the .all command to query a database it returns a datatype that is a queryset. But if the .get is used to get a single row/value, it's output datatyepe is not a queryset, it is the datatype of the model i.e 'Agent', 'Lead', 'CustomUser'    

### To add our Models to the Admin Panel 

This is done so that they are easiy accessible and manipulated Register them in admin.py file of a leads app
```
from .models import User, Lead, Agent

admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Agent)
```   
### VIEWS. 1:50:00

A person visits a web address and navigates to some path, this makes a request to the django server, django server goes through its urls.py file to find one that matches one that is requested, when it finds it, it triggers the accompanying function in the views.py file and the function renders a http response or renders a html page or form as defined. 

#### Ways of Templating 1:57

### CONTEXT 2:01:00
Video Title: Context

Context is basically Passing information into the django template.(that is being rendered). In the example below context is used to pass information to the home.html template i.e the render method. The key:
```
def home_page(request):
    context = {
        "name": "Joe",
        "age": "35"
    }
    return render(request, "leads/home.html", context)
```

The keys used in the context i.e `name and age` can be used in the `home.html` template and when it's rendered the values will be rendered. Just like below
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Hello world</h1>
    <p>Here is our custom HTML template</p>
    <p>My {{ name}} is John
        I am {{ 32 }} years old
    </p>
</body>
</html>
```
### URLS 2:09:00
Video Title: Class 3 Url

### Forms
Video title:
Update an existing form 2:55:30
Delete an exsiting Lead 3:03:00

### URL Namespaces 3:05:30
