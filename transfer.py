import sqlite3


def trans(old_database_path, new_database_path):
	conn_old = sqlite3.connect(old_database_path)
	conn_new = sqlite3.connect(new_database_path)
	c = conn_old.cursor()
	cursor = c.execute("SELECT real_url,file_txt, cat_url from results where real_url is not null ")
	for row in cursor:
		query = "update results set real_url = "+"\'"+row[0]+"\', " + "file_txt="+"\'" + row[1] + "\'" + " where cat_url = \'" + row[2] + "\'"
		conn_new.execute(query)
		conn_new.commit()
	conn_old.clo
	conn_new.close()


trans("bai_spider_old.db", "bai_spider.db")


