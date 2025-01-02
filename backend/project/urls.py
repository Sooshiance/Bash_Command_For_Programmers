from django.urls import path

from .views import (
    ProjectAPIView,
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
    path("projects/", ProjectAPIView.as_view(), name="project-list"),
    path("projects/<str:sku>/", ProjectAPIView.as_view(), name="project-detail"),
    path("posts/", PostAPIView.as_view(), name="post-list"),
    path("posts/<str:sku>/", PostAPIView.as_view(), name="post-detail"),
    path("skills/", SkillAPIView.as_view(), name="skill-list"),
    path("skills/<str:sku>/", SkillAPIView.as_view(), name="skill-detail"),
    path("testimonials/", TestimonialAPIView.as_view(), name="testimonial-list"),
    path(
        "testimonials/<str:sku>/",
        TestimonialAPIView.as_view(),
        name="testimonial-detail",
    ),
    path("messages/", ContactMessageAPIView.as_view(), name="message-list"),
    path("messages/<str:sku>/", ContactMessageAPIView.as_view(), name="message-detail"),
    path("educations/", EducationAPIView.as_view(), name="education-list"),
    path("educations/<str:sku>/", EducationAPIView.as_view(), name="education-detail"),
    path("experiences/", ExperienceAPIView.as_view(), name="experience-list"),
    path(
        "experiences/<str:sku>/", ExperienceAPIView.as_view(), name="experience-detail"
    ),
    path("certifications/", CertificationAPIView.as_view(), name="certification-list"),
    path(
        "certifications/<str:sku>/",
        CertificationAPIView.as_view(),
        name="certification-detail",
    ),
]
