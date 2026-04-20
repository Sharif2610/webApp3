from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns=[
    path('loginfactory/',obtain_auth_token),
    path('list/',views.factory_list,name='factory_list'),
    path('update_fact/<int:id>/',views.update_fact,name='update'),
] 