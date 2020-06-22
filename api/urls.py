from django.urls import path
from .views.plan_views import Plans, PlanDetail
from .views.itinerary_views import Itineraries, ItineraryDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
	# Restful routing
    path('plans/', Plans.as_view(), name='plans'),
    path('plans/<int:pk>/', PlanDetail.as_view(), name='plan_detail'),
    path('plans/<int:pk>/itineraries/', Itineraries.as_view(), name='itineraries'),
    path('itineraries/<int:pk>/', ItineraryDetail.as_view(), name='itinerary_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
