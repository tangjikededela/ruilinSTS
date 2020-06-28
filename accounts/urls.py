from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('locations/', views.locations, name="locations"),
    path('users/', views.users, name="users"),
    path('create_users/', views.createUsers, name="create_users"),
    path('update_users/<str:pk>/', views.updateUsers, name="update_users"),
    path('delete_users/<str:pk>/', views.deleteUsers, name="delete_users"),
    path('admin/accounts/locations/add/', views.createLocations, name="create_locations"),
    path('update_locations/<str:pk>/', views.updateLocations, name="update_locations"),
    path('delete_locations/<str:pk>/', views.deleteLocations, name="delete_locations"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

]