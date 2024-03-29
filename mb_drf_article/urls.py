"""Articles urls."""

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path('', views.ArticleList.as_view()),
    path('<str:slug_title>', views.ArticleDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
