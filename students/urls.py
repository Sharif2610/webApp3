from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns=[
    path('loginapi/',obtain_auth_token),
    path('show/',views.show_students),
    path('update_student/<int:id>/',views.update_student),
]