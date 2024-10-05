from .models import (Statistic,
                     GalleryItem,
                     Service,
                     Event,
                     FAQ,
                     Subscriber,)


class StatisticRepository:
    """
    Statistic CRUD Operations
    """
    def get_all_statistics(self):
        return Statistic.objects.all()
    
    def get_statistic_by_sku(self, sku):
        return Statistic.objects.get(sku=sku)
    
    def create_statistic(self, user, project,description,rate):
        s = Statistic(user=user,project=project,description=description,rate=rate)
        s.save()
        return s
    
    def update_statistic(self, sku, **kwargs):
        Statistic.objects.get(sku=sku).update(**kwargs)

    def delete_statistic(self, sku):
        Statistic.objects.get(sku=sku).delete()


class GalleryItemRepository:
    """
    GalleryItem CRUD operations
    """
    def get_all_gallery_item(self):
        return GalleryItem.objects.all()
    
    def get_gallery_item_by_sku(self, sku):
        return GalleryItem.objects.get(sku=sku)
    
    def create_gallery_item(self, title, image, description):
        gi = GalleryItem(title=title, image=image, description=description)
        gi.save()
        return gi
    
    def update_gallery_item(self, sku, **kwargs):
        GalleryItem.objects.get(sku=sku).update(**kwargs)

    def delete_gallery_item(self, sku):
        GalleryItem.objects.get(sku=sku).delete()


class ServiceRepository:
    """
    Service CRUD operations
    """
    def get_all_service(self):
        return Service.objects.all()
    
    def get_service_by_sku(self, sku):
        return Service.objects.get(sku=sku)
    
    def created_service(self, user, name, description, price):
        s = Service(user=user, name=name, description=description, price=price)
        s.save()
        return s
    
    def update_service(self, sku, **kwargs):
        Service.objects.get(sku=sku).update(**kwargs)

    def delete_service(self, sku):
        Service.objects.get(sku=sku).delete()


class EventRepository:
    """
    Event CRUD operations
    """
    def get_all_event(self):
        return Event.objects.all()
    
    def get_event_by_sku(self, sku):
        return Event.objects.get(sku=sku)
    
    def create_event(self, user, name, date, location, description):
        e = Event(user=user,name=name,date=date,location=location,description=description)
        e.save()
        return e
    
    def update_event(self, sku, **kwargs):
        Event.objects.get(sku=sku).update(**kwargs)

    def delete_event(self, sku):
        Event.objects.get(sku=sku).delete()


class FAQRepository:
    """
    FAQ CRUD operations
    """
    def get_all_faq(self):
        return FAQ.objects.all()
    
    def get_faq_by_sku(self, sku):
        return FAQ.objects.get(sku=sku)
    
    def create_faq(self, question, answer):
        f = FAQ(question=question, answer=answer)
        f.save()
        return f
    
    def update_faq(self, sku, **kwargs):
        FAQ.objects.get(sku=sku).update(**kwargs)

    def delete_faq(self, sku):
        FAQ.objects.get(sku=sku).delete()


class SubscriberRepository:
    """
    Subscriber CRUD operations
    """
    def get_all_subscriber(self):
        return Subscriber.objects.all()
    
    def get_subscriber_by_sku(self, sku):
        return Subscriber.objects.get(sku=sku)
    
    def create_subscriber(self, email, date_subscribed):
        s = Subscriber(email=email, date_subscribed=date_subscribed)
        s.save()
        return s
    
    def update_subscriber(self, sku, **kwargs):
        Subscriber.objects.get(sku=sku).update(**kwargs)

    def delete_subscriber(self, sku):
        Subscriber.objects.get(sku=sku).delete()
