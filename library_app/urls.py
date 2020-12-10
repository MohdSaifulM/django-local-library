from django.urls import path
from . import views

urlpatterns = [
    # index
    path('', views.index, name="index"),

    # auth
    path('register/', views.register, name="register"),
    path('login/', views.signin, name="login"),
    path('logout/', views.signout, name="logout"),

    #apis
    path('api/v1/borrow/<int:id>', views.api_borrow, name="api_borrow"),

]
