from django.db.models import fields
from rest_framework import serializers
from .models import PassengerModel

class PassengerSeralizer(serializers.ModelSerializer):
    class Meta:
        models = PassengerModel
        fields = '__all__'