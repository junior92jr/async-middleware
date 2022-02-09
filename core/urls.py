from rest_framework.routers import DefaultRouter

from .views import TierAppUrlViewset

app_name = 'core'

router = DefaultRouter()

router.register('', TierAppUrlViewset, basename='tier_app_url')

urlpatterns = []

urlpatterns += router.urls