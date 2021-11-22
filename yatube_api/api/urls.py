from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views
from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router_v1 = routers.DefaultRouter()
router_v1.register(
    'posts',
    PostViewSet,
    basename='posts'
)
router_v1.register(
    'groups',
    GroupViewSet,
    basename='groups'
)
router_v1.register(
    'follow',
    FollowViewSet,
    basename='follows'
)
router_v1.register(
    r'posts/(?P<id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token, name='auth'),
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
