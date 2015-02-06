from django.contrib import admin
from show_trendapp.models import *
from django.forms import TextInput
from django.db import models


admin.site.register(TrafficPerHour)
admin.site.register(UrlPerAge)
admin.site.register(TrendingUrl)
