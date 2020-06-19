from django.conf.urls import url, include
from .import views
from django.conf import settings

app_name = 'school'

urlpatterns=[
	url(r'^$',views.home, name='home'),
	url(r'^about/$',views.about, name='about'),
	url(r'^contact/$',views.contact, name='contact'),
	url(r'^course/$',views.course, name='course'),
	url(r'^teacher/$',views.teacher, name='teacher'),
	url(r'^report/$',views.report, name='report'),
	url(r'^gallery/$',views.gallery, name='gallery'),
	url(r'^login/$', views.login, name='login'),
	# url(r'^register/$', views.register, name='register'),
	url(r'^logout/$',views.logout_view, name='logout_view'),
	url(r'^dashboard/$',views.dashboard, name='dashboard'),
	url(r'^dashboard-report/$',views.dashboard_report, name='dashboard_report'),
	url(r'^data-upload/$',views.data_upload, name='data_upload'),
	url(r'^check-report/$',views.check_report, name='data_upload'),
]


