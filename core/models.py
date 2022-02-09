from django.db import models


class TierAppUrl(models.Model):
    """
    Model that stores shortened Urls for Tier App.
    """

    url_hash_string = models.CharField(editable=False, unique=True, max_length=8)
    original_url= models.URLField(max_length=250)
    clicks_counter = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.original_url 
