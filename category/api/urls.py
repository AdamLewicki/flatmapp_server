from django.urls import path

from category.api import views
app_name = 'category'

urlpatterns = [
    path('', views.Category.as_view()),
]