from rest_framework import fields, serializers
from .models import PassengerModel


class passengerSerializer(serializers.ModelSerializer):

    class Meta:
        model = PassengerModel
        fields = '__all__'