from django.urls import include,path
from .import views

app_name='search'

urlpatterns=[
    path('',views.Searchres,name='Searchres'),
]