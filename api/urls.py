from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


from api import views

router = DefaultRouter()
router.register('todofeed', views.todoViewSet)
router.register('userViewSet', views.userViewSet)


urlpatterns =[
    path('',  include(router.urls)),
    path('login/', obtain_auth_token)
]