from django.urls import path

from .views import (ProjectAPIView,
                    PostAPIView,
                    SkillAPIView,
                    TestimonialAPIView,
                    ContactMessageAPIView,
                    EducationAPIView,
                    ExperienceAPIView,
                    CertificationAPIView,
                    )


app_name = "project"

urlpatterns = [
    path('projects/', ProjectAPIView.as_view(), name='project-list'),
    path('projects/<str:sku>/', ProjectAPIView.as_view(), name='project-detail'),
]