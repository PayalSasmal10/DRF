from django.db import models

# Create your models here.
class PassengerModel(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    trackPoint = models.DecimalField()

    def __str__(self) -> str:
        return self.firstName