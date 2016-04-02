from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^about_us/$', views.about_us, name='about_us'),
	url(r'^line/$', views.line, name='line'),
	url(r'^get_name/$', views.get_name, name='get_name'),
	url(r'^handle_submission/$', views.handle_submission, name='handle_submission'),
]