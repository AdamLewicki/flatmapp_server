from django.urls import path

from backup.api import views
app_name = 'backup'

urlpatterns = [
    path('pointer/', views.PointerList.as_view()),
    path('group/', views.GroupList.as_view()),
]