from . import views

from rest_framework import routers

from django.urls import path, include


router = routers.DefaultRouter()
router.register('categories', views.CategoryViewSet)
router.register('books', views.BookViewSet)

urlpatterns = [
    # API-REST
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]