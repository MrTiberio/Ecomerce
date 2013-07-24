from django.conf.urls import patterns, include, url
from ecomstore import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('', 
    (r'^catalog/?', 'preview.views.home'), 
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root' : 'C:/Users/CARLOS/workspace/ecomstore/ecomstore/static' }), 
    # Examples:
    # url(r'^$', 'ecomstore.views.home', name='home'),
    # url(r'^ecomstore/', include('ecomstore.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',   
    (r'^catalog/$', 'preview.views.home'), 
) 

if settings.DEBUG: 
    urlpatterns += patterns('', 
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root' : 'C:/Users/CARLOS/workspace/ecomstore/ecomstore/static' }), 
)