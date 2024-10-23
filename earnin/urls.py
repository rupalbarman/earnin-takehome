"""
URL configuration for earnin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from account.views import AccountViewSet
from metric.views import MetricViewSet
from user.views import UserViewSet

router = SimpleRouter()
router.register("account", AccountViewSet, "signup-view-set")
router.register("metric", MetricViewSet, "metric-view-set")
router.register("user", UserViewSet, "user-view-set")

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += router.urls
