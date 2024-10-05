from typing import Any
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.exceptions import ValidationError

from .serializers import (StatisticSerializer,
                          GalleryItemSerializer,
                          ServiceSerializer,
                          EventSerializer,
                          FAQSerializer,
                          SubscriberSerializer,)
from .services import (Statistic_Services,
                       GalleryItem_Services,
                       Service_Services,
                       Event_Service,
                       FAQ_Service,
                       Subscriber_Service,)

from project.models import Project


class StatisticAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def __init__(self) -> None:
        self.service = Statistic_Services()
    
    def get(self, request, sku=None):
        if sku:
            statistic = self.service.get_single_statistic(sku)
            srz = StatisticSerializer(statistic)
            return Response(srz.data, status=status.HTTP_200_OK)
        statistics = self.service.get_all_statistics()
        srz = StatisticSerializer(statistics)
        return Response(srz.data, status=status.HTTP_200_OK)

    def post(self, request, psku):
        try:
            p = Project.objects.get(sku=psku)
        except ValidationError as e:
            raise e
        statistic = self.service.create_statistic(
            user=request.user,
            project=p,
            description=request.data.get("description"),
            rate=request.data.get("rate"),
        )
        srz = StatisticSerializer(statistic)
        return Response(srz.data, status=status.HTTP_200_OK)

    def put(self, request, sku):
        self.service.update_statistic(sku, **request.data)
        return Response(status=status.HTTP_205_RESET_CONTENT)

    def delet(self, request, sku):
        self.service.delete_statistic(sku)
        return Response(status=status.HTTP_204_NO_CONTENT)


class GalleryItemAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def __init__(self) -> None:
        self.service = GalleryItem_Services()
    
    def get(self, request, sku=None):
        if sku:
            gi = self.service.get_single_galleryitem(sku)
            srz = GalleryItemSerializer(gi)
            return Response(srz.data, status=status.HTTP_200_OK)
        gi = self.service.get_all_galleryitems()
        srz = GalleryItemSerializer(gi)
        return Response(srz.data, status=status.HTTP_200_OK)

    def post(self, request):
        gi = self.service.create_galleryitem(
            title=request.data.get("title"),
            image=request.data.get("image"),
            description=request.data.get("description"),
        )
        srz = GalleryItemSerializer(gi)
        return Response(srz.data, status=status.HTTP_201_CREATED)

    def put(self, request, sku):
        self.service.update_galleryitem(sku, **request.data)
        return Response(status=status.HTTP_205_RESET_CONTENT)

    def delet(self, request, sku):
        self.service.delete_galleryitem(sku)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ServiceAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def __init__(self) -> None:
        self.service = Service_Services()
    
    def get(self, request, sku=None):
        if sku:
            serv = self.service.get_single_service(sku)
            srz = ServiceSerializer(serv)
            return Response(srz.data, status=status.HTTP_200_OK)
        serv = self.service.get_all_service()
        srz = ServiceSerializer(serv)
        return Response(srz.data, status=status.HTTP_200_OK)

    def post(self, request):
        serv = self.service.create_service(
            user=request.user,
            description=request.data.get("description"),
            price=request.data.get("price"),
        )
        srz = ServiceSerializer(serv)
        return Response(srz.data, status=status.HTTP_201_CREATED)

    def put(self, request, sku):
        self.service.update_service(sku, **request.data)
        return Response(status=status.HTTP_205_RESET_CONTENT)

    def delet(self, request, sku):
        self.service.delete_service(sku)
        return Response(status=status.HTTP_204_NO_CONTENT)


class EventAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def __init__(self) -> None:
        self.service = Event_Service()
    
    def get(self, request, sku=None):
        if sku:
            e = self.service.get_single_event(sku)
            srz = EventSerializer(e)
            return Response(srz.data, status=status.HTTP_200_OK)
        events = self.service.get_all_event()
        srz = EventSerializer(events)
        return Response(srz.data, status=status.HTTP_200_OK)

    def post(self, request):
        event = self.service.create_event(
            user=request.user,
            name=request.data.get("name"),
            date=request.data.get("date"),
            location=request.data.get("location"),
            description=request.data.get("description"),
        )
        srz = EventSerializer(event)
        return Response(srz.data, status=status.HTTP_201_CREATED)

    def put(self, request, sku):
        self.service.update_event(sku, **request.data)
        return Response(status=status.HTTP_205_RESET_CONTENT)

    def delet(self, request, sku):
        self.service.delete_event(sku)
        return Response(status=status.HTTP_204_NO_CONTENT)


class FAQAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def __init__(self) -> None:
        self.service = FAQ_Service()
    
    def get(self, request, sku=None):
        if sku:
            faq = self.service.get_single_faq(sku)
            srz = FAQSerializer(faq)
            return Response(srz.data, status=status.HTTP_200_OK)
        faqs = self.service.get_all_faq()
        srz = FAQSerializer(faqs)
        return Response(srz.data, status=status.HTTP_200_OK)

    def post(self, request):
        faq = self.service.create_faq(
            question=request.data.get("question"),
            answer=request.data.get("answer"),
        )
        srz = FAQSerializer(faq)
        return Response(srz.data, status=status.HTTP_201_CREATED)

    def put(self, request, sku):
        self.service.update_faq(sku, **request.data)
        return Response(status=status.HTTP_205_RESET_CONTENT)

    def delet(self, request, sku):
        self.service.delete_faq(sku)
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubscriberAPIView(APIView):

    def __init__(self) -> None:
        self.service = Subscriber_Service()
    
    def get(self, request, sku=None):
        if sku:
            ss = self.service.get_single_subscriber(sku)
            srz = SubscriberSerializer(ss)
            return Response(srz.data, status=status.HTTP_200_OK)
        ss = self.service.get_all_subscriber()
        srz = SubscriberSerializer(ss)
        return Response(srz.data, status=status.HTTP_200_OK)

    def post(self, request):
        ss = self.service.create_subscriber(
            email=request.data.get("email"),
            date_subscribed=request.data.get("date_subscribed"),
        )
        srz = SubscriberSerializer(ss)
        return Response(srz.data, status=status.HTTP_201_CREATED)
