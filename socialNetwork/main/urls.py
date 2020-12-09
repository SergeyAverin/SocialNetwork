from django.urls import path
from . import views


urlpatterns = [
    path('user/<str:username>', views.UserByUserNameView.as_view()),
    path('publication/<str:titel>', views.PublicationByTitelView.as_view()),
    path('publication/<str:titel>/addupvoice', views.add_upvoted),
    path('publication/<str:titel>/downupvoice', views.add_downvoted),
]
