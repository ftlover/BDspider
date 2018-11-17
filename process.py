import requests
import re
import base64
import cv2
import sqlite3
import uuid


def create_uid():
	return str(uuid.uuid1())


def get_file_id_and_url(cat_url, proxies):
	try:
		response = requests.get(cat_url, proxies=proxies, timeout=5)
	except Exception as e:
		print(e)
		return None, None, None
	else:
		cookies = response.cookies
		html = response.text
		#print(html)
		try:
			rr = re.search(r'''a href="fmdown.php?.*?"''', html).group()
		except Exception as e:
			print(e)
			return None, None, None
		else:
			path = re.search(r'''".*"''', rr).group().strip("\"")
			#print(path)
			url = "https://www.feemoo.com/" + path
			# browser.get(url)
			#print(url)
			headers = {
				"authority": "www.feemoo.com",
				"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
				"Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
				"path": "/"+path,
				"scheme": "https",
				"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"
			}
			id_resp = requests.get(url, headers=headers, proxies=proxies, timeout=5)
			string = re.search(r'''vip_downvip_down\(.*?\)''', id_resp.text).group()
			# print(string)
			file_id = re.sub("\D", "", string)
			if file_id is not None:
				return file_id, url, id_resp.cookies
			return None, None, None


def getRealUrl(file_id, referer_url, cookies, proxies):
	image_code_url = "https://www.feemoo.com/new_imgcode.php"
	image_code_data = {"act": "downvf"}
	referer = referer_url
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
		, "Referer": referer, "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
	try:
		image_response = requests.post(image_code_url, image_code_data, cookies=cookies, headers=headers, proxies=proxies,timeout=5)
	except Exception as e:
		print(e)
		return None, None
	else:
		image_code_json = eval(image_response.text)
		image_code = image_code_json["code"].replace(r"\/", r"/")
		image_base64 = image_code_json["base"].replace(r"\/", r"/")
		# print(image_base64)
		codeencry = image_code
		image_type = re.search("image/.+;", image_base64).group()
		image_type = re.sub(r';', "", image_type)
		image_type = re.sub(r'image/', "", image_type)
		image_base64 = re.sub(r'data.+,', "", image_base64)
		image_data = base64.b64decode(image_base64)
		file = open("temp" + "." + image_type, 'wb')
		file.write(image_data)
		file.close()
		img = cv2.imread('temp.png')
		cv2.imshow('image', img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		verycode = input("Please intput image code:")
		download_url = "https://www.feemoo.com/ajax.php"
		download_data = {
			"action": "load_down_addr_com",
			"file_id": file_id,
			"verycode": verycode,
			"codeencry": codeencry
		}
		if verycode == "exit":
			return "exit", None
		try:
			headers = {
				"authority": "www.feemoo.com",
				"method": "POST",
				"path": "/ajax.php",
				"scheme": "https",
				"accept": "application/json, text/javascript, */*; q=0.01",
				"accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
				"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
				"origin": "https://www.feemoo.com",
				"referer": referer,
				"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
				"x-requested-with": "XMLHttpRequest"
			}

			real_resp = requests.post(download_url, download_data, cookies=cookies, headers=headers, proxies=proxies)
		except Exception as e:
			print(e)
			return None, None
		else:
			real_url_json = real_resp.text
			cookies = real_resp.cookies
			http_str = re.search(r'''\"http:.+?\"''', real_url_json)
			if http_str is not None:
				cv2.imwrite("images/" + "_" + verycode + "_" + create_uid() + ".png", img)
				return http_str.group().replace(r"\/", r"/"), cookies
			else:
				return None, None


def update(database_path, data):
	cat_url = data["cat_url"]
	real_url = data["real_url"]
	file_txt = data["file_txt"]
	# sql = "UPDATE results set real_url = '" + real_url + "'where cat_url='" + cat_url + "'"
	sql = "UPDATE results set real_url = '" + real_url + "', file_txt = '" + file_txt + "' where cat_url='" + cat_url + "'"
	# print(sql)
	conn = sqlite3.connect(database_path)
	c = conn.cursor()
	c.execute(sql)
	conn.commit()
	conn.close()


def select(database_path):
	conn = sqlite3.connect(database_path)
	c = conn.cursor()
	cursor = c.execute("SELECT cat_url from results desc where real_url is null order by id desc")
	cat_urls = list()
	for row in cursor:
		if row[0] != 'null' and re.search("http", row[0]) is not None:
			cat_urls.append(row[0])
	conn.close()
	return cat_urls


def get_file_txt(real_url, cookies):
	try:
		txt_bytes = requests.get(real_url, cookies=cookies).content
	except Exception as e:
		print(e)
		return None
	with open("temp.txt", 'wb') as file:
		file.write(txt_bytes)
	with open("temp.txt", 'r') as file:
		txt = file.read()
	return txt


# update("D:\cache\spider.db", {"cat_url": "http://www.fmpan.com/file-2136124.html", "real_url": "aaaa"})

if __name__ == '__main__':
	should_pro = input("should set proxies? [y/n]:")
	if should_pro == "y":
		proxies = {
			"http": "http://" + "127.0.0.1:1080",
			"https": "http://" + "127.0.0.1:1080",
		}
	else:
		proxies = None
	cat_urls = select("bai_spider.db")
	url_count = len(cat_urls)
	for cat_url in cat_urls:
		print(url_count)
		file_id, referer_url, cookies = get_file_id_and_url(cat_url, proxies)
		print(file_id)
		if file_id is not None:
			real_url, cookies = getRealUrl(file_id, referer_url, cookies, proxies)
			if real_url == "exit":
				exit()
			if real_url is not None:
				print("获得real_url")
				real_url = real_url.strip("\"")
				file_txt = get_file_txt(real_url, cookies)
				if file_txt is not None:
					# print(file_txt)
					data = dict()
					data["cat_url"] = cat_url
					data["real_url"] = real_url
					data["file_txt"] = file_txt
					print("real写入数据库")
					update("bai_spider.db", data)
					url_count -= 1
			else:
				cat_urls.append(cat_url)
		else:
			continue
