from django.db import models
from django.core.validators import *
import datetime

HOUR_CHOICES = (
    (1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),
    (8,8),(9,9),(10,10),(11,11),(12,12),(13,13),
    (14,14),(15,15),(16,16),(17,17),(18,18),(19,19),
    (20,20),(21,21),(22,22),(23,23),(0,24))


class TrafficPerHour(models.Model):

    traffic_date = models.DateField(default=datetime.date.today())
    traffic_hh = models.IntegerField(max_length=10)
    traffic_cnt = models.IntegerField(max_length=10)

    def __unicode__(self):
        return unicode(str(self.traffic_date)+str(self.traffic_hh))

class UrlPerAge(models.Model):

    age_date = models.DateField(default=datetime.date.today())
    age_url = models.URLField(max_length=500, blank=True, default='')
    age_title = models.CharField(max_length=100)
    age_url_cnt = models.IntegerField(max_length=10)
    over_tf = models.BooleanField(default=False)


    def __unicode__(self):
        return unicode(str(self.age_date))

class TrendingUrl(models.Model):

    trend_date = models.DateField(default=datetime.date.today())
    trend_hh = models.IntegerField(max_length=10, choices = HOUR_CHOICES)
    trend_url = models.URLField(max_length=500, blank=True, default='')
    trend_title = models.IntegerField(max_length=100)
    trend_url_cnt = models.IntegerField(max_length=10)
    timespan_per_hour = models.IntegerField(max_length=10)
    manage_url = models.BooleanField(default=False)


    def __unicode__(self):
        return unicode(str(self.trend_date)+str(self.trend_hh))




