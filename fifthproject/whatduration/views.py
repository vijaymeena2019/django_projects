from django.shortcuts import render
from django.http import HttpResponse
import datetime

# from django.shortcuts import render
# from django.http import HttpResponse
# import datetime
#
# # Create your views here.
# def time_server(request):
#     #time= datetime.datetime.now()
#     return render(request,'timeapp/timeapp_results.html',{'samay':datetime.datetime.now()})

# Create your views here.
def time_duration(request):
    # return HttpResponse('<h1>Hello time duration </h1>')
    time2 = datetime.datetime.now()
    h =13
    msg = 'Good '
    if h<12:
        msg+='Morning'
    elif h<16:
        msg+= 'Afternoon'
    elif h<20:
        msg+= 'Evening'
    else:
        msg+= 'Night'

    if h==13:
        return render(request,'whatduration/duration.html',{'m':'Morning','time':time2})
    else:
        return render(request,'whatduration/duration.html',{'m':msg,'time':time2})

def your_duration(request):
    return render(request,'whatduration/duration.html')
