from django.urls import path,include
import team.views as tasks_views
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet
router = DefaultRouter()
router.register(r'teams', TeamViewSet)
urlpatterns = [
    path('', include(router.urls)),
]