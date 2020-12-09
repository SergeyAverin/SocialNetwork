from django.urls import path

from . import views


urlpatterns = [
    path('user/<str:username>', views.UserByUserNameView.as_view()),
    path('publication/user/<str:username>', views.PublicationByAutorView.as_view()),
    path('publication/<str:titel>', views.PublicationByTitelView.as_view()),
    path('publication/<str:titel>/<str:voice>', views.add_publication_voted_view),
]
