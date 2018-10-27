from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('signup', views.SignUp)
router.register('profile', views.ProfileView)


urlpatterns = [
    url(r'', include(router.urls))
]

