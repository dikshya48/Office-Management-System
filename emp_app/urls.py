from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('list_emp/',views.list_emp,name='list_emp'),
    path('add_emp/',views.add_emp,name='add_emp'),
    path('filter_emp/',views.filter_emp,name='filter_emp'),
    path('delete_emp/',views.delete_emp,name='delete_emp'),
    path('delete_emp/<int:pk>/',views.delete_emp,name='delete_emp'),
]
