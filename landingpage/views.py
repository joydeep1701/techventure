from django.shortcuts import render,redirect
#from django.http import HttpResponse

def index(request):
    if request.session['username']:
        return redirect('dash')
    return render(request, 'landing_page/index.html')
