from django.utils.dateparse import parse_date
from django.db.models import Q

from project.models import (Project,
                            Post,)


class ProjectQuery:
    """
    Some queries for `Project` model and
    Advanced Search for it
    """

    @staticmethod
    def count_created_project_duration(start, end):
        start = parse_date(start)
        end = parse_date(end)
        return Project.objects.filter(created_at__range=(start,end))
    
    @staticmethod
    def advancedSearch(title, description, url):
        qr=None

        if title:
            qr &= Q(title__icontains=title)
        
        if description:
            qr &= Q(description__icontains=description)
        
        if url:
            qr &= Q(url__icontains=url)
        
        return Project.objects.filter(qr)


class PostQuery:
    """
    Some queries for `Post` model
    """

    @staticmethod
    def count_created_post_duration(day):
        day = parse_date(day)
        return Post.objects.filter(created_at__date=day)
