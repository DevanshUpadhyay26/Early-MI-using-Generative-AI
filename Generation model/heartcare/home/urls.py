from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict),
    path('chat', views.chat),
    path('view_report', views.view_report),
    path('delete-all-entries/', views.delete_all_entries, name='delete_all_entries'),
]