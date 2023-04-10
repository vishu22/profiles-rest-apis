from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewset, base_name="Hello-viewset")
router.register('profile',views.ProfilesViewSet)
router.register('feed',views.ProfileFeedViewSet)

urlpatterns = [
    path('hello',views.HelloAPiView.as_view(),name='hello'),
    path('login/',views.UserLoginApiView.as_view()),
    path('',include(router.urls)),
]