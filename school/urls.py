from django.conf.urls import url, include
from .import views
from django.conf import settings

app_name = 'school'

urlpatterns=[
	# url(r'^fileupload/$',views.model_form_upload, name='model_form_upload'),
	# url(r'^pdf-download/$',views.pdf_download, name='pdf_download'),
	url(r'^down/(?P<slug>.*)/(?P<slug1>.*)/(?P<slug2>.*)/$',views.pdf_month, name='pdf_month'),
	url(r'^excel/(?P<slug>.*)/$', views.excel_download, name='excel_download'),
	url(r'^excel-data/(?P<slug>.*)/(?P<slug1>.*)/(?P<slug2>.*)/$', views.excel_download_date, name='excel_download_date'),
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
	url(r'^hdfc-upload/$',views.hdfc_upload, name='hdfc_upload'),
	url(r'^check-report/$',views.check_report, name='data_upload'),
	url(r'^ledger/$',views.layer, name='layer'),
	# url(r'^pdf/(?P<slug>.*)$',views.pdf_month, name='pdf_month'),
	url(r'^layer-detail/(?P<slug>.*)/$',views.layerdetail, name='layerdetail'),
	url(r'^layer-detail-date/(?P<slug>.*)/(?P<slug1>.*)/(?P<slug2>.*)/$',views.layerdetail_date, name='layerdetail_date'),
	
]


