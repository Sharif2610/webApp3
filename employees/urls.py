from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('registerapi/',views.registeruser),
    path('loginapi/',obtain_auth_token),
    path('show_employee/',views.show_employees),
    path('update_employee/<int:id>/',views.update_employee)
]