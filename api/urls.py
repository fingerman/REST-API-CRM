from django.conf.urls import url, include


urlpatterns = [
    url(r'^products/', include('api.products.urls')),
    url(r'^companies/', include('api.companies.urls')),
    url(r'^suppliers/', include('api.suppliers.urls')),
]
