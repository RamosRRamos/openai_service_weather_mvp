"""
Module: urls

This module defines URL patterns for the common app.

URL Patterns:
    - index: URL pattern for the index view.
"""

from django.urls import path

from . import views
from .views import PlaylistView, TaskStatusView

app_name = "core"
urlpatterns = [

    path('playlist/', PlaylistView.as_view(), name='playlist'),
    path('task/<str:task_id>/', TaskStatusView.as_view(), name='task_status'),

]
