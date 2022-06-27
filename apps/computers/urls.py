from django.urls import path

from .views import ComputersListCreateView, ComputerUpdateRetrieveDestroyView

urlpatterns = [
    path('', ComputersListCreateView.as_view()),
    path('/<int:pk>', ComputerUpdateRetrieveDestroyView.as_view())

]