from django.conf.urls import url, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    url(r'^products/', include('api.products.urls')),
    url(r'^companies/', include('api.companies.urls')),
    url(r'^suppliers/', include('api.suppliers.urls')),
    url(r'^auth/', include('rest_framework.urls')),
    url(r'^token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
]
