### 1. Create Django project
```
    django-admin startproject project_name
    python manage.py runserver
```
### 2. Create apps
```
    python manage.py startapp app_name
    register our app in admin site config in settings.py -> 'app_name.apps.app_nameConfig'
    In our app:
    1. Create  urls.py file to register url with appropriate in views.py
       Register app url: Include all app's urls in admin site url.  path('/app-name',include('app_name.urls')),
    2. Create app migrations
        python manage.py makemigrations app_name
    3. Create a model in models.py then save in the database
        !Remember to register the model: admin.site.register(OurModel)
        python manage.py migrate
        Create a form for model: Create forms.py -> OurForm(forms.Form) with meta is our model.
    4. Using shell to interact with the database
        python manage.py shell
        from app_name.models import *
        Get all objects -> OurModel.objects.all()
        Get a object based on primary key -> Ourmodel.objects.get(pk=id)
        Save model -> Object.save()
    
    5. create admin user
    python manage.py createsuperuser
```