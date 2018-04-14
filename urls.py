from django.contrib import admin
from django.urls import path
from django.conf.urls import url 
from django.conf.urls import include
from project1.views import current_datetime, hours_ahead


'''
urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = patterns('',
	(r'^time/$', current_datetime),
)
'''
urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^time/$', current_datetime),
	url(r'^time/plus/(\d{1,2})/$', hours_ahead),
]