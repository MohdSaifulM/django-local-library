# The Django Local Library

## Description
Chris our random `angmoh` has asked us to make another app for his company, this Chris ah, `why ah why`. So Chris requires a library app to manage his new business. Chris has his library in 3 locations and hopes to expand his library to more locations in the future. He wants his users to be registered before they can borrow books online and would also like to know the books location.

## Setup
1. Set up django
```sh
ebere$ django-admin startproject PROJECTNAME
ebere$ cd PROJECTNAME
ebere$ python manage.py startapp APPNAME
ebere$ python manage.py migrate
ebere$ python manage.py runserver

```
2. Postgresql Setup(settings.y)
```python

    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'projectname_development',
        'USER': '<USERNAME>',  # postgres # if using windows
        # 'PASSWORD' : '', # if using windows
        'HOST': 'localhost',
        'PORT': 5432
    }
```

## Deliverables
### User
1. User should be able to register online
1. User should be able to borrow as a member from any library location seamlessly.
1. User should be able to return book online seamlessly.

The below code can be used to stop the csrf check on form submission without using serializers.
```python
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def borrow_book(request, postid):
    return JsonResponse({"message": "error"}, status=400)
```


Happy coding! Make our random `angmoh` proud again~

## Submission
1. Send a pull request with pictures of app in readme.
