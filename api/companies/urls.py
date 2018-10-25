from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', views.CompanyView)

urlpatterns = [
    url(r'', include(router.urls))
]

