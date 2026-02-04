from django.db import models

class Skills(models.Model):
    username = models.CharField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    skill_title = models.CharField(max_length=30)
    skill_description = models.CharField(max_length=200)
    skill_links = models.URLField(null=True)

    def __str__(self):
        return self.skill_title