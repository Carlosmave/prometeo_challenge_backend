from django.urls import path
from account.views import AccountView, ClientView, CreditCardView, ProviderView, ProfileView, MovementView, TransferDestinationView, TransferenceView

urlpatterns = [
    path('accounts/', AccountView.as_view(), name='accounts'),
    path('clients/', ClientView.as_view(), name='clients'),
    path('credit-cards/', CreditCardView.as_view(), name='credit_cards'),
    path('providers/', ProviderView.as_view(), name='providers'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('movements/', MovementView.as_view(), name='movements'),
    path('transfer-destinations/', TransferDestinationView.as_view(), name='transfer_destinations'),
    path('transferences/', TransferenceView.as_view(), name='transferences'),
]
