from django.db import models

# Create your models here.
class Data(models.Model):
    serial_number = models.CharField(max_length = 255)
    date_time = models.DateTimeField(auto_now_add =True)
    v1_sensor = models.CharField(max_length = 255)
    v2_sensor = models.CharField(max_length = 255)
    v3_sensor = models.CharField(max_length = 255)
    v4_sensor = models.CharField(max_length = 255)
    



