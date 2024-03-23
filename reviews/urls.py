from django.urls import path
from . import views

urlpatterns = [
    # path("",views.review),
    path("",views.ReviewView.as_view()),
    # path("thankyou",views.thankyou)
    path("thankyou",views.ThankyouView.as_view()),
    path("reviews",views.ReviewslistView.as_view(),name="review_list"),
    path("reviews/favorite",views.AddFavoriteView.as_view()),
    path("reviews/<int:pk>",views.SinglereviewView.as_view(),name="review_detail")
]
