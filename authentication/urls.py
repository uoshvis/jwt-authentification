from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from authentication.views import MemeberView


urlpatterns = [
    url(r'^login/', obtain_jwt_token),
    url(r'^list/$', MemeberView.as_view()),
    # url(r'^token-refresh/', refresh_jwt_token),
    # url(r'^token-verify/', verify_jwt_token),
    # url(r'^register/$', AuthRegister.as_view()),
]
