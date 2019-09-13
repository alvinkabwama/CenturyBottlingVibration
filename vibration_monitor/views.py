from django.shortcuts import render
from django.http import HttpResponse
from .models import Data

#from .emailsend import send_email
          
def datashow(request):
      
     if(request.method == 'GET'):
         
        selectdevicenumber = '064531'
                      
        devicedata = Data.objects.filter(serial_number = selectdevicenumber).order_by("-pk")
        
        context = {'devicedata': devicedata, 'selectdevicenumber': selectdevicenumber}
        return render(request, 'tableview.html', context)
    
    
def datareceive(request):
       
    if(request.method == 'GET'):
        serial_number = request.GET.get("serial_number")
        v1_sensor = request.GET.get("v1_sensor")
        v2_sensor = request.GET.get("v2_sensor")
        v3_sensor = request.GET.get("v3_sensor")
        v4_sensor = request.GET.get("v4_sensor")
        
        print(serial_number)
        print(v1_sensor)
        print(v2_sensor)
        print(v3_sensor)
        print(v4_sensor)
        
        if(serial_number and v1_sensor and v2_sensor and
            v3_sensor and v4_sensor):
            
            v1_float = float(v1_sensor)
            v2_float = float(v2_sensor)
            v3_float = float(v3_sensor)
            v4_float = float(v4_sensor)
                        
            #send_email(v1_float, v2_float, v3_float, v4_float)
                
            Data(
                serial_number = serial_number,
                v1_sensor = v1_sensor,
                v2_sensor = v2_sensor,
                v3_sensor = v3_sensor,
                v4_sensor = v4_sensor              
            ).save()
                  
            return HttpResponse("<br><h3> Pass </h3>")
        else:
            return HttpResponse("<br><h3> Data Missing </h3>")
        

def datasend(request):
    if(request.method == 'GET'):
        return render(request, 'datasend.html')
        
        
        
