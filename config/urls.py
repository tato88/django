from django.contrib import admin
from django.urls import path

from first.views import FirstView,SecondView,ThirdView
from hw1.views import HomeWorkView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('first', FirstView.as_view()),
    path('second', SecondView.as_view()),
    path('third/<str:name>/<int:age>', ThirdView.as_view()),
    path('test', HomeWorkView.as_view())
]
