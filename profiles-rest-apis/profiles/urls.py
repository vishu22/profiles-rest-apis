from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewset, base_name="Hello-viewset")

urlpatterns = [
    path('',views.HelloAPiView.as_view(),name='hello'),
    path('',include(router.urls))
]