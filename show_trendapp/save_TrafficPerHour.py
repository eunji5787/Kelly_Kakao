import sqlite3
import os
import datetime

filenames = next(os.walk("../media/daily/log"))[2]

content_tup = ()
file_content = []

for file_name in filenames:
	time_list = []
	if len(file_name) == 16:
		year = int(file_name[4:8])
		month = int(file_name[8:10])
		day = int(file_name[10:12])
		date = datetime.date(year, month, day)
		try:
			with open("../media/daily/log/"+file_name,'r') as f:
				for line in f:
					time_list.append((line.strip("\n").split("\t"))[1][:2])

				for x in set(time_list):
					file_content.append((date,int(x), int(time_list.count(x))))
		except:
			file_content = []



conn = sqlite3.connect("../show_trend.sqlite3")
cursor = conn.cursor()
#cursor.execute("DELETE FROM show_trendapp_trafficperhour")
cursor.executemany(
	"INSERT INTO show_trendapp_trafficperhour('traffic_date','traffic_hh','traffic_cnt') VALUES (?,?,?)" , file_content
)

conn.commit()
