from django.urls import path, include

from apps.computers.views import ComputersListCreateView,ComputerUpdateRetrieveDestroyView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('computers', include('apps.computers.urls'))
]
