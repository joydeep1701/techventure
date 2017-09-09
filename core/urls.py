from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
	url(r'^login/$',views.authorize,name='login'),
	url(r'^logout/$', auth_views.logout, {'next_page': '/accounts/login/'}, name='logout'),
	url(r'^signup$',views.signup,name='signup'),
	url(r'^dash/$',views.dash,name='dash'),
	url(r'^comingsoon$',views.comingsoon,name='cusoon')
]
