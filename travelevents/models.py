from django.db import models

# Create your models here.
class TravelEvent(models.Model):
    agency_id = models.PositiveIntegerField("ID Agência")
    agency_name = models.CharField("Nome da agência", max_length=50)
    tour_id = models.PositiveIntegerField("ID Passeio")
    tour_name = models.CharField("Nome do passeio", max_length=50)
    date = models.DateField("Data do passeio")
