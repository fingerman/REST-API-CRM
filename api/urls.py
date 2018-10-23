from django.conf.urls import url, include
from .accounts import views as user_views


urlpatterns = [
    url(
        r'^signup/$',
        user_views.SignUp.as_view(),
        name='user-signup'
    ),
    url(
        r'^auth/', include('rest_framework.urls')
    ),

]
