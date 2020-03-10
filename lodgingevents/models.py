from django.db import models

# Create your models here.
class LodgingEvent(models.Model):
    host_id = models.PositiveIntegerField("ID Hospedaria")
    host_name = models.CharField("Nome da hospedaria", max_length=50)
    bedroom_id = models.PositiveIntegerField("ID Quarto")
    bedroom_name = models.CharField("Nome do quarto", max_length=50)
    start_date = models.DateField("Data de início")
    end_date = models.DateField("Data do fim")
    