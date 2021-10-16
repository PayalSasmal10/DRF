from datetime import date
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import PassengerModel
from .serializers import PassengerSeralizer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@api_view(["GET","POST"])
def passengerDetails(request):

    if request == "GET":
        passengers = PassengerModel.objects.all()
        serializer = PassengerSeralizer(passengers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request == "POST":
        serializer = PassengerSeralizer(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)



@api_view(["GET","PUT","DELETE"])
def singlePassengerDetails(request,pk):
    
    if request == "GET":
        passenger = PassengerModel.objects.get(id=pk)
        serializer = PassengerSeralizer(data=passenger)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request == "PUT":
        passenger = PassengerModel.objects.get(id=pk)
        serializer = PassengerSeralizer(instance=passenger, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    elif request == "DELETE":
        passenger = PassengerModel.objects.get(id=pk)
        passenger.delete()
        return Response("Successfully Deleted")


