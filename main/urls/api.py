from django.urls import path, include
from rest_framework import routers
from sales.views import ArticleViewSet, SaleViewSet
from users.views import UserViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'articles', ArticleViewSet, basename='article')
router.register(r'sales', SaleViewSet, basename='sale')
router.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path(
        "v1/",
        include(
            [
                path("", include(router.urls)),
            ]
        ),
    )
]
