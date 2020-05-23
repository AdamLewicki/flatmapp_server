from django.urls import path

from backup.api import views
app_name = 'blog'

urlpatterns = [
    path('', views.PointerList.as_view()),
]