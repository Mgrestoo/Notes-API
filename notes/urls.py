from django.urls import path
from .views import NoteViewSet, register, login_view, login_page, register_page
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet, basename='note')

urlpatterns = [
    path('auth/register/', register, name='api-register'),
    path('auth/login/', login_view, name='api-login'),
    ] + router.urls
 