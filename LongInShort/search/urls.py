
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name= 'home'),
    path('search/',views.search,name ='search'),
    path('upload/',views.upload, name= 'upload'),
    path('summary/<int:myid>',views.summary,name= "summary"),
    path('textsummary/<int:sid>',views.textsummary,name= "textsummary"),
]
