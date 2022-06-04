from django.urls import path
from .views import PartyListView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('party-list', PartyListView.as_view(), name="party_list"),
    path('token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]



