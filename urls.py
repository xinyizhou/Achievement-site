from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
#from django.views.static import *
from achievement.views import homepage, achievement, set_completed_achievement, get_achievement_for_vote, vote_for, vote_achievement
from cycle.views import hall_of_fame
from django.views.generic.simple import redirect_to
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),
    url(r'^$|^home/$', homepage),
    url(r'^achievement/(\d+)/$', achievement),
    url(r'^achievement/(\d+)/(\d+)/$', set_completed_achievement),
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}, name='logout'),
    url(r'^vote_list/$', get_achievement_for_vote),
    url(r'^vote_list/(\d+)/$', vote_achievement),
    url(r'^vote_list/(\d+)/vote/$', vote_for),
    url(r'^hall_of_fame/$', hall_of_fame),
    url(r'^accounts/profile/$', redirect_to, {'url': '/'}),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
