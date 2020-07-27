# from django.urls import path,include
# from . import views
# from django.conf.urls import url
# from rest_framework_simplejwt import views as jwt_views
# from rest_framework import routers
# router=routers.DefaultRouter()
#
# router.register('user',views.UserView())
#
#
# urlpatterns=[
#     # path("all_posts/",views.UserView,name="index"),
#     path('v1/',include(router.urls)),
#     path('token/',jwt_views.TokenObtainPairView.as_view(),name='token'),
#     path('token/refresh/',jwt_views.TokenRefreshSlidingView.as_view(),name='refresh')
#
# ]

from django.urls import path,include
from rest_framework import routers
from . import views
from rest_framework_simplejwt import views as jwt_views
router=routers.DefaultRouter()
router.register('',views.UserView)


urlpatterns = [
    path('',include(router.urls)),
    path('token/',jwt_views.TokenObtainPairView.as_view(),name='token'),
    path('token/refresh/',jwt_views.TokenRefreshSlidingView.as_view(),name='refresh')

]