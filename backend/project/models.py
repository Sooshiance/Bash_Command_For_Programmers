from django.db import models

from shortuuid.django_fields import ShortUUIDField

from user.models import User


class Project(models.Model):
    # List of projects with descriptions, images, and links.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sku = ShortUUIDField(max_length=20, db_index=True, unique=True, alphabet="0123456789abcdefghij")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    # Create, read, update, and delete blog posts.
    title = models.CharField(max_length=100)
    sku = ShortUUIDField(max_length=20, db_index=True, unique=True, alphabet="0123456789abcdefghij")
    content = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Skill(models.Model):
    # Display a list of skills with proficiency levels.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sku = ShortUUIDField(max_length=20, db_index=True, unique=True, alphabet="0123456789abcdefghij")
    name = models.CharField(max_length=50)
    proficiency = models.IntegerField()


class Testimonial(models.Model):
    # Display testimonials from clients or colleagues.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sku = ShortUUIDField(max_length=20, db_index=True, unique=True, alphabet="0123456789abcdefghij")
    name = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    position = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class ContactMessage(models.Model):
    # Allow visitors to send messages.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sku = ShortUUIDField(max_length=20, db_index=True, unique=True, alphabet="0123456789abcdefghij")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'


class Education(models.Model):
    # Display your educational background, including degrees, institutions, and graduation dates.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sku = ShortUUIDField(max_length=20, db_index=True, unique=True, alphabet="0123456789abcdefghij")
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    graduation_date = models.DateField()
    description = models.CharField(max_length=255, blank=True, null=True)


class Experience(models.Model):
    # List your work experience, including job titles, companies, durations, and descriptions of your roles.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sku = ShortUUIDField(max_length=20, db_index=True, unique=True, alphabet="0123456789abcdefghij")
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)


class Certification(models.Model):
    # Showcase any certifications or courses you have completed.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sku = ShortUUIDField(max_length=20, db_index=True, unique=True, alphabet="0123456789abcdefghij")
    name = models.CharField(max_length=100)
    issuing_organization = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiration_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
