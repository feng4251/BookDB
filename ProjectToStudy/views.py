from django.http import HttpResponse,Http404
import datetime

def hello(request):
    return HttpResponse("Hello World!")
    
def now(request):
    now=datetime.datetime.now()
    html='<html><body>The current time is %s.</body></html>' % now
    return HttpResponse(html)
    
def after_now(request,dt):
    try:
        dt=int(dt)
    except:
        return Http404()
    time=datetime.datetime.now()+datetime.timedelta(hours=dt)
    html='<html><body>After %d hours,time will be %s.</body></html>' %(dt,time)
    return HttpResponse(html)
    
    