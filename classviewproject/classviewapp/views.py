from django.shortcuts import render
from classviewproject.classviewapp.models import PassengerModel
from .serializer import passengerSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class PassengerDetails:

    def get(self, request):
        passenger = PassengerModel.objects.all()
        serializer = passengerSerializer(passenger, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(requ)
