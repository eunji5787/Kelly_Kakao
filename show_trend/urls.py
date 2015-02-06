from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'show_trendapp.views.home'),
	url(r'^rankperweek/$', 'show_trendapp.views.rank_per_week'),
	url(r'^diffperweek/$', 'show_trendapp.views.diff_per_week'),
	url(r'^rankperday/$', 'show_trendapp.views.rank_per_day'),
	url(r'^diffperday/$', 'show_trendapp.views.diff_per_day'),
	url(r'^trafficperday/$', 'show_trendapp.views.traffic_per_day'),
	url(r'^trafficperhour/$', 'show_trendapp.views.traffic_per_hour'),
	url(r'^twentyfivetrend/$', 'show_trendapp.views.twentyfive_trend'),
	url(r'^hourlyurl/$', 'show_trendapp.views.hourly_trending_url'),
	url(r'^manageurl/$', 'show_trendapp.views.manage_url'),
	url(r'^manageurlday/$', 'show_trendapp.views.manage_url_day'),
	url(r'^manageurlweek/$', 'show_trendapp.views.manage_url_week'),
    url(r'^admin/', include(admin.site.urls)),
)
