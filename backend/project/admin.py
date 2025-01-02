from django.contrib import admin

from project.models import (
    Project,
    Post,
    Skill,
    Testimonial,
    ContactMessage,
    Education,
    Experience,
    Certification,
)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title",)


class PostAdmin(admin.ModelAdmin):
    list_display = ("title",)


class SkillAdmin(admin.ModelAdmin):
    list_display = ("name",)


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name",)


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name",)


class EducationAdmin(admin.ModelAdmin):
    list_display = ("institution",)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("user",)


class CertificationAdmin(admin.ModelAdmin):
    list_display = ("user",)


admin.site.register(Project, ProjectAdmin)

admin.site.register(Post, PostAdmin)

admin.site.register(Skill, SkillAdmin)

admin.site.register(Testimonial, TestimonialAdmin)

admin.site.register(ContactMessage, ContactMessageAdmin)

admin.site.register(Education, EducationAdmin)

admin.site.register(Experience, ExperienceAdmin)

admin.site.register(Certification, CertificationAdmin)
