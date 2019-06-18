# Mb-drf-article

Mb-drf-article is a simple Django Rest Framework app to add some articles.  
install the package with `pip install mb-drf-article`.

## Quick start

### 1. Add "mb-drf-article" to your `INSTALLED_APPS` settings

```python
# settings.py

INSTALLED_APPS = [
...
'mb_drf_article',
]
```

### 2. Include the articles URLconf in your project `urls.py`

```python
# urls.py

urlpatterns = [
    # ...
    path('articles/', include('mb_drf_article.urls')),
]
```

### 3. Add the models in your Database

Run `python manage.py migrate` in your SHELL.

### 4. Update the Django Rest Framework Settings

Update the Django Rest Framework settings to add a pagination.

```python
# Django Rest Framework
# https://www.django-rest-framework.org

REST_FRAMEWORK = {
    # ...
    'DEFAULT_PAGINATION_CLASS': ('rest_framework.pagination.'
                                 'LimitOffsetPagination'),
    'PAGE_SIZE': 5
}
```

## Try it

try the application with httpie :

```bash
http http://127.0.0.1:8000/articles/

# OUTPUT :

HTTP/1.1 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Length: 341
Content-Type: application/json
Date: Tue, 18 Jun 2019 12:34:41 GMT
Server: WSGIServer/0.2 CPython/3.6.5rc1
Vary: Accept
X-Frame-Options: SAMEORIGIN

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": []
}
```

## Methods

- **GET** `http://127.0.0.1:8000/articles/`: get the articles
- **POST** `http://127.0.0.1:8000/articles/`: post a new article
  <br>
- **GET** `http://127.0.0.1:8000/articles/<slug_title>`: get a specific article
- **PUT** `http://127.0.0.1:8000/articles/<slug_title>`: update or create (all fields required)
- **PATCH** `http://127.0.0.1:8000/articles/<slug_title>`: update an article
- **DELETE** `http://127.0.0.1:8000/articles/<slug_title>`: delete an article

> Note: Get methods doesn't require the admin permission. Others methods requires the admin permission.
