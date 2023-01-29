from django.urls import path

from . import views

app_name = 'reg'
urlpatterns = [
    path('', views.home, name='home'),
    path('create_st/', views.create_st, name='create_st'),
    # path('groups/', views.groups, name='groups'),
    # path('detail/<int:groupss_id>',views.detail, name='detail'),
    
    # path('updategroup/<str:pk>',views.updategroup, name='updategroup'),
    # path('delete/<str:pk>',views.deletegroup, name='deletegroup'),
    # path('group_csv/',views.group_csv, name='group_csv'),
    # path('group_csv_m/',views.group_csv_m, name='group_csv_m'),
]