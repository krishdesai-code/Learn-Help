from django.shortcuts import render,redirect
from .models import Skills
from Account.models import User

def All_skills(request):
    skills = Skills.objects.all()
    return render(request,"skills/all_skill.html",{'skills' : skills})

def Add_skills(request):
    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
      skill_title = request.POST.get('skill_title')
      skill_description = request.POST.get('skill_desc')
      skill_level = request.POST.get('skill_level')
      skill_link = request.POST.get('skill_link')
      
      Skills.objects.create(
          user=user,
          skill_title = skill_title,
          skill_description = skill_description,
          skill_level=skill_level,
          skill_links = skill_link,
      )
      return redirect("allSkills")
    return render(request,"skills/add_skill.html")

def my_skill(request):
    user_id = request.session.get('user_id')
    my_skills = Skills.objects.filter(user_id=user_id)

    return render(
        request,
        "skills/my_skill.html",
        {'my_skills': my_skills}
    )