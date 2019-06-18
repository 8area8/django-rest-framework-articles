# Articles

Article is a simple Django Rest Framework app to add some articles.

## Quick start

### 1. Add "articles" to your `INSTALLED_APPS` setting like this:

```python
# settings.py

INSTALLED_APPS = [
...
'article',
]
```

### 2. Include the articles URLconf in your project `urls.py`

```python
# urls.py

urlpatterns = [
    # ...
    path('articles/', include('article.urls')),
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
