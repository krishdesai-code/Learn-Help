from django.db import models
from Account.models import User

class Skill_category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Skills(models.Model):
    Level_option = [
        ('Basic','Basic'),
        ('Intermediate','Intermediate'),
        ('Advance','Advance'),
    ]

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    skill_title = models.CharField(max_length=30)
    skill_description = models.CharField(max_length=200)
    skill_category = models.ForeignKey(Skill_category,on_delete=models.CASCADE,related_name='skills')
    skill_level = models.CharField(max_length=20,choices=Level_option)
    skill_links = models.URLField(null=True)

    def __str__(self):
        return self.skill_title