from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from app.serializers import authorSerializer


class authorViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    class_serializer = authorSerializer