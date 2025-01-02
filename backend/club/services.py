from .repositories import (
    StatisticRepository,
    GalleryItemRepository,
    ServiceRepository,
    EventRepository,
    FAQRepository,
    SubscriberRepository,
)


class Statistic_Services:
    """
    Extending Statistic model CRUD operations
    """

    def __init__(self, *args, **kwargs):
        self.repository = StatisticRepository()

    def get_all_statistics(self):
        return self.repository.get_all_statistics()

    def get_single_statistic(self, sku):
        return self.repository.get_statistic_by_sku(sku)

    def create_statistic(self, user, project, description, rate):
        return self.repository.create_statistic(user, project, description, rate)

    def update_statistic(self, sku, **kwargs):
        self.repository.update_statistic(sku, kwargs)

    def delete_statistic(self, sku):
        self.repository.delete_statistic(sku)


class GalleryItem_Services:
    """
    Extending GalleryItem model CRUD operations
    """

    def __init__(self, *args, **kwargs):
        self.repository = GalleryItemRepository()

    def get_all_galleryitems(self):
        return self.repository.get_all_gallery_item()

    def get_single_galleryitem(self, sku):
        return self.repository.get_gallery_item_by_sku(sku)

    def create_galleryitem(self, title, image, description):
        return self.repository.create_gallery_item(
            title=title, image=image, description=description
        )

    def update_galleryitem(self, sku, **kwargs):
        self.repository.update_gallery_item(sku, kwargs)

    def delete_galleryitem(self, sku):
        self.repository.delete_gallery_item(sku)


class Service_Services:
    """
    Extending Service model CRUD operations
    """

    def __init__(self, *args, **kwargs):
        self.repository = ServiceRepository()

    def get_all_service(self):
        return self.repository.get_all_service()

    def get_single_service(self, sku):
        return self.repository.get_service_by_sku(sku)

    def create_service(self, user, name, description, price):
        return self.repository.created_service(
            user=user, name=name, description=description, price=price
        )

    def update_service(self, sku, **kwargs):
        self.repository.update_service(sku, kwargs)

    def delete_service(self, sku):
        self.repository.delete_service(sku)


class Event_Service:
    """
    Extending Event model CRUD operations
    """

    def __init__(self, *args, **kwargs):
        self.repository = EventRepository()

    def get_all_event(self):
        return self.repository.get_all_event()

    def get_single_event(self, sku):
        return self.repository.get_event_by_sku(sku)

    def create_event(self, user, name, date, location, description):
        return self.repository.create_event(
            user=user, name=name, date=date, location=location, description=description
        )

    def update_event(self, sku, **kwargs):
        self.repository.update_event(sku, kwargs)

    def delete_event(self, sku):
        self.repository.delete_event(sku)


class FAQ_Service:
    """
    Extending FAQ model CRUD operations
    """

    def __init__(self, *args, **kwargs):
        self.repository = FAQRepository()

    def get_all_faq(self):
        return self.repository.get_all_faq()

    def get_single_faq(self, sku):
        return self.repository.get_faq_by_sku(sku)

    def create_faq(self, question, answer):
        return self.repository.create_faq(question=question, answer=answer)

    def update_faq(self, sku, **kwargs):
        self.repository.update_faq(sku, kwargs)

    def delete_faq(self, sku):
        self.repository.delete_faq(sku)


class Subscriber_Service:
    """
    Extending Subscriber model CRUD operations
    """

    def __init__(self, *args, **kwargs):
        self.repository = SubscriberRepository()

    def get_all_subscriber(self):
        return self.repository.get_all_subscriber()

    def get_single_subscriber(self, sku):
        return self.repository.get_subscriber_by_sku(sku)

    def create_subscriber(self, email, date_subscribed):
        return self.repository.create_subscriber(
            email=email, date_subscribed=date_subscribed
        )

    def update_subscriber(self, sku, **kwargs):
        self.repository.update_subscriber(sku, kwargs)

    def delete_subscriber(self, sku):
        self.repository.delete_subscriber(sku)
