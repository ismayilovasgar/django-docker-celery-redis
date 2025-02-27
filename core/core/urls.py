from django.urls import path
from django.conf import settings
from notification import views
from django.contrib import admin
from django.conf.urls.static import static
from notification.consumers_me import MyNotificationConsumer
from notification.consumers import NotificationConsumer

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.notification_page_view, name="notification_page"),
    path("me/", views.notification_page_view_me, name="notification_page_me"),
]


websocket_urlpatterns = [path("ws/notifications/", MyNotificationConsumer.as_asgi())]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
# websocket_urlpatterns = [
#     path("ws/notifications/", NotificationConsumer.as_asgi())
# ]
