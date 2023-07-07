from . import views
from django.urls import path

app_name='webapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.my_login, name='login'),
    path('logout', views.my_logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('add_record', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('view_record/<int:pk>', views.view_record, name='view_record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
]
