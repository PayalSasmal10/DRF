from django.contrib import admin
from django.urls import path
from functionviewapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('passenger', views.passengerDetails, name="passenger"),
    path('passenger/<int:pk>', views.singlePassengerDetails, name="passenger"),
]