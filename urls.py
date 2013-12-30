from django.conf.urls.defaults import *

urlpatterns = patterns('myproject.projects.views',
    (r'^/(?P<slug>[a-zA-Z0-9_.-]+)$', 'Detail'),
    (r'^', 'Main'),
)


