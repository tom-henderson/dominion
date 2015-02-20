from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings

import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='dominion/base.html')),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.log_out, name='log_out'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)