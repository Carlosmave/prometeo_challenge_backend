from django.urls import path
from authentication.views import LoginView, ProviderView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('providers/', ProviderView.as_view(), name='providers'),
]
