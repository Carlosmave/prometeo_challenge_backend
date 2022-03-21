from django.urls import path
from authentication.views import LoginView, LogoutView, ProviderView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('providers/', ProviderView.as_view(), name='providers'),
]
