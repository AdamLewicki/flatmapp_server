from django.urls import path

from backup.api import views
app_name = 'blog'

urlpatterns = [
    path('trigger/<int:pk>/', views.TriggerDetail.as_view()),
    path('trigger/', views.TriggerList.as_view()),
]