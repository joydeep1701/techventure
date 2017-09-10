from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,JsonResponse
from django.utils import timezone
import json
from .models import CalenderEvent
# Create your views here.

@login_required
def index(request):
    #event_id = request.GET['id']
    return render(request,'calender/index.html')

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
