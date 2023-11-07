from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *





urlpatterns = [
    path('', ViewProcessRequests.as_view(), name='index'),
    path('register/', registration, name='register'),
    path('home/', home, name='home'),
    path('login/', login_v, name='login'),
    path('logout/', logout_view, name='logout'),
    path('request/create/', CreateRequest.as_view(), name='request_create'),
    path('accounts/profile/', ViewRequests.as_view(), name='profile'),
    path('accounts/profile/delete/<int:pk>', DeleteRequest.as_view(), name='request_delete'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
