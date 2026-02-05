from django.urls import path
from . import views

urlpatterns = [
    path("all/",views.All_skills,name="allSkills"),
    path("add/",views.Add_skills,name="addSkills"),
    path("myskills",views.my_skill,name="my_skills"),
]
