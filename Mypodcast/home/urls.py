from django.urls import path
from .views import home_view, login_view, logout_view, registration

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registration/', registration, name='registration'),
]