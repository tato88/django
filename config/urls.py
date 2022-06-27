from django.contrib import admin
from django.urls import path

from first.views import FirstView,SecondView,ThirdView
from hw1.views import HomeWorkView

urlpatterns = [
    path('admin/', admin.site.urls),

]
