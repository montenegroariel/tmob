from django.urls import path, include
from .views import RedirectViewSet, RedirectModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', RedirectModelViewSet, basename='redirects')

urlpatterns = [
    path('<str:key>/', RedirectViewSet.as_view({'get': 'retrieve'}), name='redirect'),
    path('', include(router.urls)),
]
