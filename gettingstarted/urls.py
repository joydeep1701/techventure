from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

import landingpage.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', landingpage.views.index, name='index'),
    url(r'^accounts/',include('core.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
