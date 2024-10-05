from rest_framework import permissions, generics
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination

from .queries import (ProjectQuery,
                      PostQuery,)
from .serializers import (ProjectSerializer as BaseProjectSerializer)

from project.serializers import (ProjectSerializer,
                                 PostSerializer)


class CreatedProjectTimeLapse(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ProjectSerializer
    pagination_class = PageNumberPagination

    def get_object(self):
        start = self.kwargs['start']
        end = self.kwargs['end']
        if str(end) <= str(start):
            raise ValidationError(detail="Not ordered days!")
        return start, end
    
    def get_queryset(self):
        start, end = self.get_object()
        x = ProjectQuery.count_created_project_duration(start, end)
        return x


class CreatedPostOneDay(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination

    def get_object(self):
        day = self.kwargs['day']
        return day
    
    def get_queryset(self):
        day = self.get_object()
        x = PostQuery.count_created_post_duration(day)
        return x


class AdvancedSearchView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BaseProjectSerializer

    def get_object(self):
        kwargs = self.request.query_params
        title = kwargs.get("title", None)
        description = kwargs.get("description", None)
        url = kwargs.get("url", None)
        return title, description, url

    def get_queryset(self):
        t, d, u = self.get_object()
        x = ProjectQuery.advancedSearch(t, d, u)
        return x
