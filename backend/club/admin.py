from django.contrib import admin

from .models import (Statistic,
                     GalleryItem,
                     Service,
                     Event,
                     FAQ,
                     Subscriber,)


class StatisticAdmin(admin.ModelAdmin):
    list_display = ['project',]


class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ['title',]


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name',]


class EventAdmin(admin.ModelAdmin):
    list_display = ['name',]


class FAQAdmin(admin.ModelAdmin):
    list_display = ['question',]


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email',]


admin.site.register(Statistic, StatisticAdmin)

admin.site.register(GalleryItem, GalleryItemAdmin)

admin.site.register(Service, ServiceAdmin)

admin.site.register(Event, EventAdmin)

admin.site.register(FAQ, FAQAdmin)

admin.site.register(Subscriber, SubscriberAdmin)
