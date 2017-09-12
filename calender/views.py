from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,JsonResponse
from django.utils import timezone
import json
from .models import CalenderEvent
from .forms import CalenderEventForm
# Create your views here.

@login_required
def index(request):
    #event_id = request.GET['id']
    form = CalenderEventForm()
    return render(request,'calender/index.html',{'form':form})

def newEvent(request):
    #form = CalenderEventForm()
    #return render(request, 'core/signup.html', {'form':form})
    if request.method == "POST":
        form = CalenderEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.creator_name = request.session['firstname']
            event.save()
            return HttpResponse(json.dumps({'status':'ok'}))
        else:
            return HttpResponse(json.dumps({'status':'failed'}))
    else:
        return HttpResponse("Invalid Request")

@login_required
def events_for_month(request):
    if 'month' in request.GET and request.GET['month'] != '':
        date = request.GET['month']
        q = CalenderEvent.objects.filter(start_date__contains=date).values().order_by('start_date')
        response = list(q)
        #return HttpResponse(json.dumps(response))
        return JsonResponse(response,safe=False)
    else:
        return HttpResponse("Specify date as GET parameter baseurl?date=")
