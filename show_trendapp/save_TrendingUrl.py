import sqlite3
import os
import datetime

filenames = next(os.walk("../media/hourly_trend"))[2]

file_content = []
content_tup = ()

def timespan(file_name):
	sample_file = file_name[:9]+"_sample"+file_name[9:]
	try:
		with open("../media/hourly_trend/"+sample_file,'r') as f:
			time_list = []
			for line in f:
				if len(line)>2:
					time = (line.strip("\n").split("\t"))[1][:2]
					if not time in time_list:
						time_list.append(time)

		return len(time_list)
	except:
		return 0


for file_name in filenames:
	if len(file_name) == 13:
		print file_name
		year = int("20"+file_name[:2])
		month = int(file_name[2:4])
		day = int(file_name[4:6])
		hour = int(file_name[7:9])
		date = datetime.date(year, month, day)
		try:
			with open("../media/hourly_trend/"+file_name,'r') as f:
				for line in f:
					line_list = line.strip("\n").split("\t")
					url = line_list[0].decode("utf-8")
					ttl = line_list[1].decode("utf-8")
					cnt = int(line_list[2])


					file_content.append((date, hour, url, ttl, cnt, timespan(file_name),False))
		except:
			file_content = []

conn = sqlite3.connect("../show_trend.sqlite3")
cursor = conn.cursor()
#cursor.execute("DELETE FROM show_trendapp_trendingurl")
cursor.executemany(
	"INSERT INTO show_trendapp_trendingurl('trend_date','trend_hh','trend_url','trend_title','trend_url_cnt','timespan_per_hour','manage_url') VALUES (?,?,?,?,?,?,?)" , file_content
)
conn.commit()

