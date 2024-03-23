from django.urls import path
from . import views

urlpatterns = [
    path("",views.CreatorView.as_view(),name="prohome"),
    path("profiles",views.UserProfileView.as_view(),name="profiles"),
    path("thankyou",views.thankyou)
]
