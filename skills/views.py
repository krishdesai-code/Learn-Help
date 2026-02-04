from django.shortcuts import render,redirect
from .models import Skills

def All_skills(request):
    skills = Skills.objects.all()
    return render(request,"skills/all_skill.html",{'skills' : skills})

def Add_skills(request):
    if request.session['name'] == None:
        return redirect("/")
    elif request.method == 'POST':
      username = request.POST.get('username')
      skill_title = request.POST.get('skill_title')
      skill_description = request.POST.get('skill_desc')
      skill_link = request.POST.get('skill_link')
      
      Skills.objects.create(
          username=request.session['name'],
          skill_title = skill_title,
          skill_description = skill_description,
          skill_links = skill_link,
      )
      return redirect("allSkills")
    return render(request,"skills/add_skill.html")