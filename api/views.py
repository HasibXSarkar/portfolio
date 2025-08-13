from rest_framework import viewsets
from .models import (
    Project, Skill, ContactMessage, Experience,
    BlogPost, CV, Award, ExtracurricularActivity
)
from .serializers import (
    ProjectSerializer, SkillSerializer, ContactMessageSerializer,
    ExperienceSerializer, BlogPostSerializer, CVSerializer, AwardSerializer, ExtracurricularActivitySerializer
)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class CVViewSet(viewsets.ModelViewSet):
    queryset = CV.objects.all()
    serializer_class = CVSerializer

class AwardViewSet(viewsets.ModelViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer

class ExtracurricularActivityViewSet(viewsets.ModelViewSet):
    queryset = ExtracurricularActivity.objects.all()
    serializer_class = ExtracurricularActivitySerializer