from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from api.viewsets import Users, UserProfiles
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

router = DefaultRouter()
router.register('users', Users, base_name='users')
router.register('user-profiles', UserProfiles, base_name='users-profiles')

# General API urls
urlpatterns = router.urls

# Special urls used for authentication purposes
# such as obtaining a token
urlpatterns += [
    url(r'^auth/obtain-token/$', obtain_jwt_token, name='obtain_token'),
    url(r'^auth/refresh-token/', refresh_jwt_token, name='refresh_token'),
]