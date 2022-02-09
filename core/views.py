from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import mixins

from .models import TierAppUrl
from .serializers import StoreUrlSerializer, TierAppUrlSerializer


class TierAppUrlViewset(mixins.CreateModelMixin,
                        mixins.ListModelMixin,   
                        viewsets.GenericViewSet):
    """
    Viewset to Create and Display all Urls.
    """

    queryset = TierAppUrl.objects.all()
    serializer_class = TierAppUrlSerializer

    def create(self, request):

        serializer = StoreUrlSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        response = TierAppUrlSerializer(serializer.instance)

        return Response(response.data, status=status.HTTP_201_CREATED)
