from django.contrib import admin
from django.urls import path
from collage import views
app_name = "collage"

urlpatterns = [
    path('',views.home, name = "home"),
    path('student1/', views.student1, name = "student1"),
    path('detail/', views.detail, name='detail'),
    path('register/', views.registration , name= "registration"),
    path('login/', views.login, name="login"),
path('logout/', views.logout, name="logout"),

    path('search/', views.search, name="search"),
# ex: /polls/5/results/
    #path('<int:pk>/result/', views.result, name='result'),
# ex: /polls/5/vote/
    #path('<int:pk>/vote/', views.vote, name='vote'),
]
