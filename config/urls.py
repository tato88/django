from django.contrib import admin
from django.urls import path

from users.views import UsersListCreateView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('users', UsersListCreateView.as_view()),
    path('users/<int:pk>', UsersListCreateView.as_view()),

]
