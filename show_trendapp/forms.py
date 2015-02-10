import re
from django import forms
from django.forms import extras
from django.forms import ModelForm
from django.core.exceptions import ObjectDoesNotExist
from show_trendapp.models import *
import datetime

latest_age_date = UrlPerAge.objects.latest('age_date').age_date
earliest_age_date = UrlPerAge.objects.earliest('age_date').age_date
latest_trend_date = TrendingUrl.objects.order_by('-trend_date', '-trend_hh')[0].trend_date

def timetostr(time):

    return datetime.date.strftime(time, "%Y-%m-%d")

class WeekForm(forms.Form):

    weekdate_choice = forms.ChoiceField(widget=forms.Select())

    def __init__(self, *args, **kwargs):
    	super(self.__class__, self).__init__(*args, **kwargs)
    	CHOICES = []
    	days = (latest_age_date - earliest_age_date).days
    	for i in xrange(0,days,7):
    		start_date = earliest_age_date+datetime.timedelta(i)
    		end_date = earliest_age_date+datetime.timedelta(i+6)
    		if end_date > latest_age_date:
    			end_date = latest_age_date
    		CHOICES.append((start_date, timetostr(start_date)+" ~ "+timetostr(end_date)))

    	self.fields['weekdate_choice'].choices = CHOICES

    	if len(CHOICES) > 0:
    		self.fields['weekdate_choice'].initial = CHOICES[0]
    	else:
    		self.fields['weekdate_choice'].initial = ('','')

    def initial_value(self):
    	return self.fields['weekdate_choice'].initial


class RankPerDayForm(forms.Form):

    dayrank_date = forms.DateField(widget=extras.SelectDateWidget, label = "", initial=datetime.date.today() - datetime.timedelta(days=1))

class DiffPerDayForm(forms.Form):

    daydiff_date = forms.DateField(widget=extras.SelectDateWidget, label = "", initial=datetime.date.today() - datetime.timedelta(days=1))

class TrafficPerDayForm(forms.Form):

    traffic_start = forms.DateField(widget=extras.SelectDateWidget, label = "", initial=datetime.date.today() )
    traffic_end = forms.DateField(widget=extras.SelectDateWidget, label = "", initial=datetime.date.today() )


class TrafficPerHourForm(forms.Form):

    traffic_date = forms.DateField(widget=extras.SelectDateWidget, label = "", initial=datetime.date.today() - datetime.timedelta(days=1))


class UrlPerAgeForm(forms.Form):

	age_start = forms.DateField(widget=extras.SelectDateWidget, label = "", initial=datetime.date.today() )
	age_end = forms.DateField(widget=extras.SelectDateWidget, label = "", initial=datetime.date.today() )


class TrendingUrlForm(forms.Form):

	trend_date = forms.DateField(widget=extras.SelectDateWidget, label = "", initial=latest_trend_date)
	#trend_hour = forms.ChoiceField(widget=forms.Select(), choices = HOUR_CHOICES, label = "")

class ManageUrlForm(forms.Form):

	trend_url = forms.ChoiceField(widget=forms.Select())

	def __init__(self, *args, **kwargs):
		super(self.__class__, self).__init__(*args, **kwargs)
		CHOICES = []
		obj = TrendingUrl.objects.filter(manage_url=True).values_list('trend_url', 'trend_url').distinct()
		for i in obj:
			CHOICES.append(i)
		self.fields['trend_url'].choices = CHOICES

		if len(CHOICES) > 0 :
			self.fields['trend_url'].initial = CHOICES[0]
		else:
			self.fields['trend_url'].initial = ('','')


	def initial_value(self):

		return self.fields['trend_url'].initial



