from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Redirect
from .serializers import RedirectSerializer
from django.core.cache import cache

class RedirectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = RedirectSerializer

    def retrieve(self, request, key=None):
        queryset = cache.get('QuerysetRedirect')
        if not queryset:
            queryset = Redirect.objects.all() # first time
        redirect = get_object_or_404(queryset, key=key)
        serializer = RedirectSerializer(redirect)
        return Response(serializer.data)


class RedirectModelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Redirect.objects.all()
    serializer_class = RedirectSerializer