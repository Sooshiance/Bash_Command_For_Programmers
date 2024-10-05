from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg

from shortuuid.django_fields import ShortUUIDField

from user.models import User
from project.models import Project


class Statistic(models.Model):
    # Display statistics like the number of projects completed, years of experience, etc.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True, null=True)
    rate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    sku = ShortUUIDField(max_length=20, db_index=True, unique=True, alphabet="0123456789abcdefghij")

    def averageSingleProjectRate(self):
        return Statistic.objects.filter(project=self.project).aggregate(Avg('rate'))['rate__avg']
    
    def __str__(self):
        return f"{self.project}"


class GalleryItem(models.Model):
    # A gallery to showcase images or media related to your work or interests.
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True, null=True)
    sku = ShortUUIDField(max_length=20, db_index=True, unique=True, alphabet="0123456789abcdefghij")

    class Meta:
        verbose_name = 'Gallery Item'
        verbose_name_plural = 'Gallery Items'


class Service(models.Model):
    # If you offer services, you can list them with descriptions and pricing.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = ShortUUIDField(max_length=20, db_index=True, unique=True, alphabet="0123456789abcdefghij")


class Event(models.Model):
    # If you participate in or host events, you can list them with details.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    sku = ShortUUIDField(max_length=20, db_index=True, unique=True, alphabet="0123456789abcdefghij")


class FAQ(models.Model):
    # A section for frequently asked questions to help visitors understand more about you and your work.
    question = models.CharField(max_length=200)
    answer = models.TextField()
    sku = ShortUUIDField(max_length=20, db_index=True, unique=True, alphabet="0123456789abcdefghij")

    class Meta:
        verbose_name = 'Frequently Asked Question'
        verbose_name_plural = 'Frequently Asked Questions'


class Subscriber(models.Model):
    # Allow visitors to subscribe to your newsletter.
    email = models.EmailField()
    date_subscribed = models.DateField(auto_now_add=True)
    sku = ShortUUIDField(max_length=20, db_index=True, unique=True, alphabet="0123456789abcdefghij")
