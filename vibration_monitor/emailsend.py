# -*- coding: utf-8 -*-
from django.core.mail import send_mail
from django.conf import settings
from .models import Client


def send_email(ca_meter_float, cin_house_float, va_meter_float):
    client_of_interest = Client.objects.get(email = 'aggrey@gmail.com')
        
    client_name = client_of_interest.name

    
    print('CLIENT NAME', client_name)
    print('DATA IN HOUSE: ', cin_house_float)
    print('DATA AFTER METER: ', ca_meter_float)
    
    
    if cin_house_float > ca_meter_float:
        send_mail(
                'POWER BYPASS',
                'The system has recorded a bypass connection for client,  ' + client_name,
                settings.EMAIL_HOST_USER,
                ['alkaleos10@gmail.com', 'aggreyndiku@gmail.com', 'mgodwin987@gmail.com'],
                fail_silently = False
                )
        
    if  va_meter_float > 50 and  va_meter_float < 200:
        send_mail(
                'POWER BYPASS',
                'The system has recorded an undervoltage for client,  ' + client_name,
                settings.EMAIL_HOST_USER,
                ['alkaleos10@gmail.com','aggreyndiku@gmail.com', 'mgodwin987@gmail.com'],
                fail_silently = False
                )
        
    
    
