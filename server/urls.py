from django.conf.urls import patterns, include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('server.free2me.views',
    (r'^admin/', include(admin.site.urls)),
    (r'^$','index'),
    (r'^user/(?P<user_name>\w+)/$', 'user'),
    (r'^resource/(?P<resource_name>\w+)/$', 'resource'),
    (r'^using/$', 'using'),
    (r'^waiting/$', 'waiting'),
    (r'^resources/$','resources'),
    (r'^pop_use/$','pop_use'),
    (r'^pop_wait/$','pop_wait'),
    (r'^push_use/$','push_use'),
    (r'^push_wait/$','push_wait')
    )

