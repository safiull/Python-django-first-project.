from django.urls import path
from .views import *

urlpatterns = [
    path('create/', post_create_view, name = 'create'),
    path('list/', post_list_view, name = 'list'),
    path('details/<int:id>', post_details_view, name = 'post_details'),
    path('update/<int:id>', post_update_view, name = 'update')
]
