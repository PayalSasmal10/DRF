from django.shortcuts import render
from rest_framework.serializers import Serializer
from classviewproject.classviewapp.models import PassengerClassModel
from .serializer import passengerSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.
class PassengerDetails(APIView):

    def get(self, request):
        passenger = PassengerClassModel.objects.all()
        serializer = passengerSerializer(passenger, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = passengerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PassengerDetailsPKBased(APIView):
    def get(self, pk):
        try:
            return PassengerClassModel.objects.get(id=pk)
        except return Response
