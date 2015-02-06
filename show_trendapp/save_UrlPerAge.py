import sqlite3
import os
import datetime

filenames = next(os.walk("../media/daily"))[2]

file_content = []
content_tup = ()
url_list = []

for file_name in filenames:
	if len(file_name) >= 19:
		year = int(file_name[:4])
		month = int(file_name[4:6])
		day = int(file_name[6:8])
		date = datetime.date(year, month, day)
		try:
			with open("../media/daily/"+file_name,'r') as f:
				for line in f:
					line_list = line.strip("\n").split("\t")
					if len(file_name) == 19:
						over_tf = True
					elif len(file_name) == 20:
						over_tf = False

					url = line_list[0].decode("utf-8")
					ttl = line_list[1].decode("utf-8")
					cnt = int(line_list[2])


					file_content.append((date,url,ttl,cnt,over_tf))
		except:
			file_content = []

conn = sqlite3.connect("../show_trend.sqlite3")
cursor = conn.cursor()

#cursor.execute("DELETE FROM show_trendapp_urlperage")

sql = "INSERT OR REPLACE INTO"
sql = sql + " show_trendapp_urlperage('age_date','age_url','age_title','age_url_cnt','over_tf')"
sql = sql + " VALUES (?,?,?,?,?)"

cursor.executemany(sql, file_content)
conn.commit()
