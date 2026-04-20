from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('home/',views.home,name='home'),
    path('list/',views.workforce_list,name='workforce_list'),
    path('insert/',views.insert_workforce,name='insert_workforce'),
    path('update/<int:wfno>/',views.update_workforce,name='update_workforce'),
    path('delete/<int:wfno>/',views.delete_workforce,name='delete_workforce'),
]