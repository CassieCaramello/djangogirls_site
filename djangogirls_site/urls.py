from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    # Examples:
    # url(r'^$', 'djangogirls_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^about/', TemplateView.as_view(template_name="about.html"), name="about"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url('^', include('django.contrib.auth.urls')),
    
    
 ]
