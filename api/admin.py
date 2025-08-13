from django.contrib import admin
from .models import (
    Project, Skill, ContactMessage, Experience,
    BlogPost, CV, Award, ExtracurricularActivity
)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(ContactMessage)
admin.site.register(Experience)
admin.site.register(BlogPost)
admin.site.register(CV)
admin.site.register(Award)
admin.site.register(ExtracurricularActivity)