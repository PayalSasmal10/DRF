from rest_framework import serializers
from .models import PassengerModel

class PassengerSeralizer(serializers.ModelSerializer):
    class Meta:
        model = PassengerModel
        fields = '__all__'