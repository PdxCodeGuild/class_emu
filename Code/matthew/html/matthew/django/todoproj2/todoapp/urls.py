

from django.urls import path

from . import views

app_name = 'todoapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_list/', views.create_list, name='create_list'),
    path('<int:todo_list_id>/', views.detail, name='detail'),
    path('delete_list/', views.delete_list, name='delete_list'),
    path('delete_list2/<int:todo_list_id>/', views.delete_list2, name='delete_list2'),
    path('delete_list3/', views.delete_list3, name='delete_list3'),
    path('create_todo_item/', views.create_todo_item, name='create_todo_item'),
    path('complete_todo_item/<int:todo_item_id>/', views.complete_todo_item, name='complete_todo_item'),
    path('restore_todo_item/<int:todo_item_id>/', views.restore_todo_item, name='restore_todo_item'),

]
