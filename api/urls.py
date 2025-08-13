from django.urls import path, include
from rest_framework import routers
from .views import (
    ProjectViewSet, SkillViewSet, ContactMessageViewSet,
    ExperienceViewSet, BlogPostViewSet, CVViewSet, AwardViewSet, ExtracurricularActivityViewSet
)

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'contacts', ContactMessageViewSet)
router.register(r'experiences', ExperienceViewSet)
router.register(r'blogs', BlogPostViewSet)
router.register(r'cv', CVViewSet)
router.register(r'awards', AwardViewSet)
router.register(r'extracurriculars', ExtracurricularActivityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
