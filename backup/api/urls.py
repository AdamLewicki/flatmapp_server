from django.urls import path

from backup.api.views import api_marker_detail_view, api_marker_detail_post, api_marker_detail_delete

app_name = 'blog'

urlpatterns = [
    path('marker/<int:slug>/', api_marker_detail_view, name='marker_detail'),
    path('marker-post/', api_marker_detail_post, name='marker_post'),
    path('marker/delete/<int:slug>', api_marker_detail_delete, name='marker_delete')
]