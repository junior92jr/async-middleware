from rest_framework import serializers

from common.utils import generate_unique_string
from common.constants import TIER_APP_URL

from .models import TierAppUrl
from .exceptions import RepeatedUrlHashException


class TierAppUrlSerializer(serializers.ModelSerializer):
    """
    Model Serializer that Handles TierAppUrl model.
    """

    shortened_url = serializers.SerializerMethodField()

    class Meta:
        model = TierAppUrl
        fields = ('id', 'original_url', 'shortened_url')

    def get_shortened_url(self, obj):
        """
        Return a short Url based on the stored hashlib obj.
        """
        
        return '{domain}/{url_hash_string}'.format(
            domain=TIER_APP_URL, url_hash_string=obj.url_hash_string)


class StoreUrlSerializer(serializers.ModelSerializer):
    """
    Model Serializer that Handles TierAppUrl model.
    """

    class Meta:
        model = TierAppUrl
        fields = ('original_url',)

    def generate_hash(self):
        """
        Method that generates hashlib string.
        """

        return generate_unique_string(self.validated_data['original_url'])
    
    def create(self, validated_data):
        """
        Perform Create in Serializer.
        """
        
        new_url_hash_string = self.generate_hash()
        
        if TierAppUrl.objects.filter(
            url_hash_string=new_url_hash_string).exists():
            raise RepeatedUrlHashException()

        validated_data['url_hash_string'] = new_url_hash_string

        return super(StoreUrlSerializer, self).create(validated_data)
