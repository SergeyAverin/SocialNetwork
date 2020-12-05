from django.urls import path
from . import views


urlpatterns = [
    path('user/<str:username>', views.UserByUserNameView.as_view())
]
