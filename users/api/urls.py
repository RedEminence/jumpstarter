from django.urls import path
from rest_framework.routers import DefaultRouter

from users.api.views.registration import register

router = DefaultRouter(trailing_slash=False)

urlpatterns = router.urls

urlpatterns.extend([
    path('auth/registration', register),
    # path('auth/token', None),
    # path('auth/token/refresh', None)
])
