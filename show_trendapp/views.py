# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from show_trendapp.forms import *
from show_trendapp.models import *
from django.db.models import *
from django.template import Context, loader, RequestContext
from django.template.loader import get_template
from django.contrib import messages
import os
import collections
import operator
import datetime
import time
import sys
import urllib2
import re

def home(request):
    select_url(request)
    latest = TrendingUrl.objects.order_by('-trend_date', '-trend_hh')[0]
    trend_date = latest.trend_date
    hour = latest.trend_hh
    recent_list = TrendingUrl.objects.filter(trend_date = trend_date, trend_hh = hour).order_by('-trend_url_cnt')
    recent_list = recent_list[:10]

    recent_chart = chart_trendingurl(recent_list)
    variables = RequestContext(request, recent_chart)
    return render_to_response('home.html',locals(), variables)

def rank_per_week(request):
    if request.method == 'POST':
        form = WeekForm(request.POST)
        if form.is_valid():
            target_date = datetime.datetime.strptime(form.cleaned_data['weekdate_choice'], '%Y-%m-%d')
    else:
        form = WeekForm()
        target_date = WeekForm().initial_value()[0]

    chart_info = get_agechart_info_week(target_date)
    variables = RequestContext(request,chart_info)
    return render_to_response('rank_per_week.html',locals(), variables)

def get_agechart_info_week(target_date):
    target_end = target_date + datetime.timedelta(days=6)
    target_list = UrlPerAge.objects.filter(age_date__range=[target_date,target_end]).order_by('-age_url_cnt')

    return chart_rank_per_week(target_list)

def chart_rank_per_week(target_list):
    limit = 30
    weekrank_dict = make_rank(target_list)[:limit]
    xdata, ydata = get_age_x_and_y(weekrank_dict)[:2]
    extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
    chartcontainer = 'discretebarchart_container'
    chartdata = {
        'x': xdata, 'y1': ydata, 'extra1': extra_serie,
    }
    charttype = "discreteBarChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer':chartcontainer,
            }

    return locals()

def diff_per_week(request):
    variables = RequestContext(request)
    diff_dict = {}
    sameurl_list = []

    lastweek_end = datetime.date.today() - datetime.timedelta(days=8)
    lastweek_start = lastweek_end - datetime.timedelta(days=6)
    lastweek = UrlPerAge.objects.filter(
        age_date__range = [lastweek_start, lastweek_end]).order_by('-age_url_cnt')
    distinct_lastweek = lastweek.values_list('age_url' ,flat=True).distinct()

    thisweek_end = datetime.date.today() - datetime.timedelta(days=1)
    thisweek_start = thisweek_end - datetime.timedelta(days=6)
    thisweek = UrlPerAge.objects.filter(
        age_date__range = [thisweek_start, thisweek_end]).order_by('-age_url_cnt')

    for i in thisweek:
        ind = i.age_url
        if not ind in distinct_lastweek:
            if ind in diff_dict.keys():
                diff_dict[ind] = diff_dict[ind] + i.age_url_cnt
            else:
                diff_dict[ind] = i.age_url_cnt
        else:
            sameurl_list.append(i.age_url)

    data = chart_diff_per_week(diff_dict, sameurl_list, lastweek, thisweek)
    variables = RequestContext(request, data)

    return render_to_response('diff_per_week.html',locals(), variables)

def chart_diff_per_week(diff_dict, sameurl_list, lastweek, thisweek):
    xdata = []
    ydata = []
    xdata2 = []
    ydata1 = []
    ydata2 = []
    print UrlPerAge.objects.filter(age_url="http://i.sstudy.kr/L/142").values('age_url_cnt')
    print lastweek.values('age_url_cnt').annotate(Sum('age_url'))


    for i in sameurl_list:
        print i



    diff_dict = diff_dict.items()
    diff_dict.sort(key=lambda x: x[1], reverse=True)
    for k, v in diff_dict:
        xdata2.append(k)
        ydata2.append(v)

    extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"}}
    chartcontainer = 'multibarchart_container'
    chartcontainer1 = 'discretebarchart_container'

    limit = 10
    chartdata = {
        'x': xdata[:limit],
        'name1': '지난 주', 'y1': ydata[:limit], 'extra1': extra_serie,
        'name2': '이번 주', 'y2': ydata1[:limit], 'extra2': extra_serie,
    }
    chartdata1 = {
        'x': xdata2[:limit], 'y1': ydata2[:limit], 'extra1': extra_serie,
    }
    charttype = "multiBarChart"
    charttype1 = "discreteBarChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartdata1': chartdata1,
        'chartcontainer':chartcontainer,
        'chartcontainer1': chartcontainer1
            }

    return locals()

def make_rank(rank_list):
    rank_dict = {}

    for i in rank_list:
        ind = (i.age_url, i.age_title)
        if ind in rank_dict.keys():
            rank_dict[ind] += i.age_url_cnt
        else:
            rank_dict[ind] = i.age_url_cnt

    ranks = rank_dict.items()
    ranks.sort(key=lambda x: x[1], reverse=True)

    return ranks

def rank_per_day(request):
    if request.method == 'POST':
        form = RankPerDayForm(request.POST)
        if form.is_valid():
            target_date = form.cleaned_data['dayrank_date']
    else:
        form = RankPerDayForm()
        target_date = datetime.date.today() - datetime.timedelta(days=1)

    chart_info = get_agechart_info(target_date)
    variables = RequestContext(request,chart_info)
    return render_to_response('rank_per_day.html',locals(), variables)

def get_agechart_info(target_date, yester_date = None):
    target_list = UrlPerAge.objects.filter(age_date = target_date).order_by('-age_url_cnt')
    if yester_date != None:
        yester_list = UrlPerAge.objects.filter(age_date = yester_date).order_by('-age_url_cnt')
        return chart_diff_per_day(target_list, yester_list)

    return chart_rank_per_day(target_list)

def get_age_x_and_y(dayrank_dict):
    xdata = []
    ydata = []
    ydata1 = []

    for k,v in dayrank_dict:
        xdata.append(k[0])
        if type(v)==tuple:
            ydata.append(v[0])
            ydata1.append(v[1])
        else:
            ydata.append(v)

    return xdata, ydata, ydata1

def chart_rank_per_day(dayrank_list):
    limit = 30
    dayrank_dict = make_rank(dayrank_list)[:limit]
    xdata, ydata = get_age_x_and_y(dayrank_dict)[:2]
    extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
    chartcontainer = 'discretebarchart_container'
    charttype = "discreteBarChart"

    chartdata = {
        'x': xdata,
        'y1': ydata,
        'extra1': extra_serie,
    }

    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
    }

    return locals()

def make_diff(target_list, compare_list):
    target_dict = make_rank(target_list)
    compare_dict = dict(make_rank(compare_list))
    same_dict = {}
    diff_dict = {}

    for ind, cnt in target_dict:
        if ind in compare_dict.keys():
            compare_cnt = compare_dict[ind]
            same_dict[ind] = (compare_cnt, cnt, cnt - compare_cnt, compare_cnt + cnt)
        else:
            diff_dict[ind] = (0, cnt, cnt, cnt)

    same_dict = same_dict.items()
    same_dict.sort(key=lambda x: x[1][2], reverse=True)

    diff_dict = diff_dict.items()
    diff_dict.sort(key=lambda x: x[1][3], reverse=True)

    return diff_dict, same_dict

def diff_per_day(request):
    if request.method == 'POST':
        form = DiffPerDayForm(request.POST)
        if form.is_valid():
            target_date = form.cleaned_data['daydiff_date']
    else:
        form = DiffPerDayForm()
        target_date = datetime.date.today() - datetime.timedelta(days=1)

    yester_date = target_date - datetime.timedelta(days=1)
    chart_info = get_agechart_info(target_date, yester_date)
    variables = RequestContext(request,chart_info)
    return render_to_response('diff_per_day.html',locals(), variables)

def chart_diff_per_day(target_list, yester_list):
    limit = 10
    diff_dict, same_dict = make_diff(target_list, yester_list)
    xdata , ydata, ydata1 = get_age_x_and_y(same_dict)
    minus_dict = same_dict[len(same_dict)-limit:len(same_dict)][::-1]
    same_dict = same_dict[:limit]
    diff_dict = diff_dict[:limit]
    extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
    chartcontainer = "multibarchart_container"

    chartdata = {
        'x': xdata[:limit],
        'name1': '어제 공유 횟수    '.decode("utf-8"), 'y1': ydata[:limit], 'extra1': extra_serie,
        'name2': '오늘 공유 홋수    '.decode("utf-8"), 'y2': ydata1[:limit], 'extra2': extra_serie,
    }
    charttype = "multiBarChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer':chartcontainer,
            }

    return locals()

def traffic_per_day(request):
    show_week = True
    if request.method == 'POST':
        form = TrafficPerDayForm(request.POST)
        if form.is_valid():
            show_week = False
            start_time = form.cleaned_data['traffic_start']
            end_time = form.cleaned_data['traffic_end']
    else:
        form = TrafficPerDayForm()
        end_time = datetime.date.today() - datetime.timedelta(days=1)
        start_time = end_time - datetime.timedelta(days=6)

    chart_info = get_trafficday_chart_info(start_time, end_time)
    variables = RequestContext(request, chart_info)
    return render_to_response('traffic_per_day.html',locals(), variables)

def get_trafficday_chart_info(start_time, end_time):
    traffic_cnt_list = TrafficPerHour.objects.filter(
        traffic_date__range = [start_time, end_time]
        ).values('traffic_date').annotate(Sum('traffic_cnt'))

    return chart_traffic_per_day(start_time, end_time, traffic_cnt_list)

def chart_traffic_per_day(start_time, end_time, traffic_cnt_list):
    ydata = [0]*int(((end_time-start_time).days)+1)
    time_info = [start_time + datetime.timedelta(days=x) for x in range(len(ydata))]

    for i in traffic_cnt_list:
        traffic_time = i['traffic_date']
        if traffic_time in time_info:
            ydata[time_info.index(traffic_time)] = i['traffic_cnt__sum']

    xdata = map(lambda x: int(time.mktime(x.timetuple()))*1000, time_info)
    scrap_counts_diff = calculate_difference(ydata)

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    charttype = "lineChart"
    extra_serie = { "tooltip": {"y_start": "", "y_end": " cal"}, "date_format": tooltip_date }
    kw_extra = { 'x_is_date': True , 'x_axis_format': "%d %b %Y" }
    chartdata = {
        'x': xdata, 'name': '일별 스크랩 횟수'.decode("utf-8"), 'y': ydata, 'extra':extra_serie }
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'kw_extra' : kw_extra,
        }

    return locals()


def traffic_per_hour(request):
    show_today = True

    if request.method == 'POST':
        form = TrafficPerHourForm(request.POST)
        if form.is_valid():
            show_today = False
            target_date = form.cleaned_data['traffic_date']
    else:
        form = TrafficPerHourForm()
        target_date = datetime.date.today() - datetime.timedelta(days=1)

    chart_info = get_traffichour_chart_info(target_date)
    variables = RequestContext(request, chart_info)
    return render_to_response('traffic_per_hour.html',locals(), variables)

def get_traffichour_chart_info(target_date):
    traffic_cnt_list = TrafficPerHour.objects.filter(traffic_date = target_date).order_by('traffic_hh')

    return chart_traffic_per_hour(traffic_cnt_list)

def chart_traffic_per_hour(traffic_cnt_list):
    xdata = []
    ydata = []

    for i in traffic_cnt_list:
        xdata.append(i.traffic_hh)
        ydata.append(i.traffic_cnt)

    scrap_counts_diff = calculate_difference(ydata)

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"}, "date_format": tooltip_date}
    chartdata = {
        'x': xdata, 'name': '시간별 스크랩 횟수'.decode("utf-8"), 'y': ydata, 'extra': extra_serie }
    kw_extra = { 'x_is_date': False , 'x_axis_format': ""}
    charttype = "lineChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'kw_extra' : kw_extra
    }

    return locals()

def calculate_difference(scrap_counts):
    l = [0]
    for i in range(1, len(scrap_counts)):
        diff = scrap_counts[i] - scrap_counts[i -1]
        l.append(diff)

    return l

def twentyfive_trend(request):
    show_week = True

    if request.method == 'POST':
        form = UrlPerAgeForm(request.POST)
        if form.is_valid():
            show_week = False
            start_time = form.cleaned_data['age_start']
            end_time = form.cleaned_data['age_end']
    else:
        form = UrlPerAgeForm()
        end_time = datetime.date.today() - datetime.timedelta(days=1)
        start_time = end_time - datetime.timedelta(days=6)

    chart_info = get_twentyfive_chart_info(start_time, end_time)
    variables = RequestContext(request, chart_info)
    return render_to_response('twentyfive_trend.html', locals(), variables)

def get_twentyfive_chart_info(start_time, end_time):
    undertf_list = UrlPerAge.objects.filter(age_date__range = [start_time, end_time], over_tf=False
        ).order_by('-age_url_cnt')
    overtf_list = UrlPerAge.objects.filter(age_date__range = [start_time, end_time], over_tf=True
        ).order_by('-age_url_cnt')

    return chart_twentyfive_trend(undertf_list, overtf_list)

def get_twentyfive_x_and_y(age_list):
    time_info = []
    ydata = []
    xdata = []

    for i in age_list:
        if not i.age_url in xdata:
            xdata.append(i.age_url)
            ydata.append(i.age_url_cnt)
            time_info.append(i.age_date)

    return xdata, ydata, time_info

def chart_twentyfive_trend(undertf_list, overtf_list):
    xdata1, ydata1, time_info1 = get_twentyfive_x_and_y(undertf_list)
    xdata2, ydata2, time_info2 = get_twentyfive_x_and_y(overtf_list)
    extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"}}
    chartcontainer = 'discretebarchart_container'
    chartcontainer1 = 'discretebarchart_container1'

    limit = 10
    chartdata = { #25세 이하
        'x': xdata1[:limit], 'y1': ydata1[:limit], 'extra1': extra_serie,
    }
    chartdata1 = { #25세 이상
        'x': xdata2[:limit], 'y1': ydata2[:limit], 'extra1': extra_serie,
    }
    charttype = "discreteBarChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartdata1': chartdata1,
        'chartcontainer':chartcontainer,
        'chartcontainer1': chartcontainer1
            }

    return locals()

def hourly_trending_url(request):
    variables = RequestContext(request)
    latest = TrendingUrl.objects.order_by('-trend_date', '-trend_hh')[0]
    trend_date = latest.trend_date
    hour = latest.trend_hh
    trend_list = TrendingUrl.objects.filter(trend_date = trend_date, trend_hh = hour).order_by('-trend_url_cnt')
    chart_info = chart_trendingurl(trend_list[:10])
    if request.method == 'POST':
        selected_url = request.POST.get('manage')
        select_url(selected_url)
        if request.POST.has_key('hour'):
            hour = request.POST.get('hour')
        else:
            hour = 0
        form = TrendingUrlForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            trend_date = info['trend_date']

            if TrendingUrl.objects.filter(trend_date = trend_date, trend_hh = hour).exists():
                trend_list = TrendingUrl.objects.filter(trend_date = trend_date, trend_hh = hour).order_by('-trend_url_cnt')
                trend_list = trend_list[:10]
            else:
                latest = TrendingUrl.objects.order_by('-trend_date', '-trend_hh')[0]
                trend_date = latest.trend_date
                hour = latest.trend_hh
                trend_list = TrendingUrl.objects.filter(trend_date = trend_date, trend_hh = hour).order_by('-trend_url_cnt')
            chart_info = chart_trendingurl(trend_list[:10])

    else:
        form = TrendingUrlForm()
    variables = RequestContext(request, chart_info)
    return render_to_response('hourly_trending_url.html',locals(), variables)


def chart_trendingurl(trending_list):
    title = []
    xdata = []
    ydata = []

    for i in trending_list:
        xdata.append(i.trend_url)
        ydata.append(i.trend_url_cnt)
        title.append(i.trend_title)

    extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
    chartdata = {'x': xdata, 'y1': ydata, 'extra1': extra_serie}
    charttype = "discreteBarChart"
    data = {'charttype': charttype, 'chartdata': chartdata }

    return locals()


def manage_url(request):
    initial_url = ManageUrlForm().initial_value()[0]
    url_list = TrendingUrl.objects.filter(trend_url=initial_url).order_by(
                'trend_date', 'trend_hh')
    chart_info = chart_manage_url(url_list)
    if request.method == 'POST':

        if request.POST.has_key('delete'):
            deleted_url = request.POST.get('delete')
            if len(deleted_url) == 0:
                deleted_url = request.POST.get('trend_url')
            form = delete_url(deleted_url)


        elif request.POST.has_key('select'):
            form = ManageUrlForm(request.POST)
        if form.is_valid():
            trend_url = form.cleaned_data['trend_url']
            url_list = TrendingUrl.objects.filter(trend_url=trend_url).order_by(
                'trend_date', 'trend_hh')
            chart_info = chart_manage_url(url_list)
    else:
        form = ManageUrlForm()

    variables = RequestContext(request, chart_info)
    return render_to_response('manage_url.html', locals(),variables)


def chart_manage_url(url_list):
    xdata = [i for i in range(24)]
    ydata1 = [0]*len(xdata)
    ydata2 = [0]*len(xdata)
    cntperhour = [0]*len(xdata)

    if len(url_list) > 0:
        start_date , start_hour = url_list.first().trend_date , url_list.first().trend_hh
        end_date, end_hour =  url_list.last().trend_date , url_list.last().trend_hh

        time_list = [i.trend_hh for i in url_list]
        time_set =  set([(x,time_list.count(x)) for x in time_list])

        for i in url_list:
            ind = xdata.index(i.trend_hh)
            if ydata1[ind] == 0:
                ydata1[ind] = i.trend_url_cnt
            else:
                ydata1[ind] = ydata1[ind] + i.trend_url_cnt


        for i in time_set:
            ydata2[i[0]] = ydata1[i[0]]/i[1]
            cntperhour[i[0]] = i[1]

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"},
                   "date_format": tooltip_date}
    chartdata = {
        'x': xdata,
        'name1': '  시간별 누적 스크랩 횟수  ', 'y1': ydata1, 'extra': extra_serie,
        'name2': '  시간별 평균 스크랩 횟수  ', 'y2': ydata2, 'extra': extra_serie,
    }
    kw_extra = { 'x_is_date': False , 'x_axis_format': ""}
    charttype = "lineChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'kw_extra' : kw_extra,
    }

    return locals()

def select_url(selected_url):

    if TrendingUrl.objects.filter(trend_url=selected_url).exists():
        TrendingUrl.objects.filter(trend_url=selected_url).update(manage_url=True)

def delete_url(deleted_url):

    if TrendingUrl.objects.filter(trend_url=deleted_url).exists():
        TrendingUrl.objects.filter(trend_url=deleted_url).update(manage_url=False)

    return ManageUrlForm({'trend_url': '' })

