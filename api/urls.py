from django.conf.urls import url, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf.urls import url, include
from .profiles import views
from rest_framework import routers
from rest_framework import viewsets

router = routers.DefaultRouter()
router.register('signup', views.SignUp)
router.register('', views.ProfileView)


urlpatterns = [
    url(r'^products/', include('api.products.urls')),
    url(r'^companies/', include('api.companies.urls')),
    url(r'^suppliers/', include('api.suppliers.urls')),
    url(r'^profile/', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls')),
    url(r'^token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
]
