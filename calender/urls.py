from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$',views.index,name='calender_index'),
	url(r'^addNewEvent$',views.newEvent,name='add_new_event'),
	url(r'^getEventsByMonth$',views.events_for_month,name='events_for_month'),

]
