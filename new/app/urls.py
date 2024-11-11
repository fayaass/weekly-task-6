from django.urls import path
from . import views
urlpatterns=[
    path('',views.new_login),
    path('home',views.home),
    path('new_logout',views.new_logout),
    path('add_prod',views.add_prod),
    path('edit/<pid>',views.edit),
    path('delete/<pid>',views.delete)

]