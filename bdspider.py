import requests
from urllib import parse




class Spider:
	def __init__(self, cookies, url, bdstoken):
		self.cookies = cookies
		self.url = url
		self.bdstoken = bdstoken
		self.headers = {
			"Accept": "*/*",
			"Accept-Encoding": "gzip, deflate, br",
			"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
			"Cache-Control": "no-cache",
			"Connection": "keep-alive",
			"Content-Length": "114",
			"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
			"Host": "pan.baidu.com",
			"Origin": "https://pan.baidu.com",
			"Pragma": "no-cache",
			"Referer": "https://pan.baidu.com/disk/home?",
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36",
			"X-Requested-With": "XMLHttpRequest"
		}

	def create_folder(self,path):
		url_create = "https://pan.baidu.com/api/create?a=commit&channel=chunlei&web=1&app_id=250528" \
					 "&bdstoken=%s" \
					 "&logid=MTUyOTU4MjA1MTc3NTAuNzczNjM4NjM3MTk0OTIzOA==&clienttype=0" % self.bdstoken
		#print(url_create)
		form_data = {
			"path": path,
			"isdir": "1",
			"block_list": "[]",
		}

		resp = requests.post(url_create,headers = self.headers,cookies = self.cookies,data= form_data)
		print(resp.text)

	def transfer(self,shareid,uk,file_list,path_t_save):

		url_tran = "https://pan.baidu.com/share/transfer?" \
				   "shareid=" + shareid+ \
				   "&from=" + uk+ \
				   "&web=1" \
				   "&app_id=250528" \
				   "&bdstoken=" + self.bdstoken+ \
				   "&logid=MTUyOTU5Mjg1NzM5MTAuMzY5MTA1NDEyNzIzODAyNQ==" \
				   "&clienttype=0" \

		headers = {
			"Accept": "application/json, text/javascript, */*; q=0.01",
			"Accept-Encoding": "gzip, deflate, br",
			"Accept-Language": "zh-CN,zh;q=0.9",
			"Connection": "keep-alive",
			"Content-Length": "74",
			"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
			"Host": "pan.baidu.com",
			"Origin": "https://pan.baidu.com",
			"Referer": self.url,
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36",
			"X-Requested-With": "XMLHttpRequest"
		}
		file_list = "[\"" + file_list + "\"]"

		form_data = {
			"filelist":file_list,
			"path": path_t_save
		}
		#print(shareid ,uk ,self.bdstoken)
		resp = requests.post(url_tran, headers=headers, cookies=self.cookies, data=form_data)
		print(resp.text)

#PCSKYS_Windows7Loader_v3.27(激活）.rar
#\/PCSKYS_Windows7Loader_v3.27(\u6fc0\u6d3b\uff09.rar
#filelist: ["/PCSKYS_Windows7Loader_v3.27(激活).rar"]
#%5B%22%2FPCSKYS_Windows7Loader_v3.27(%E6%BF%80%E6%B4%BB%EF%BC%89.rar%22%5D
#%5B%22%2FPCSKYS_Windows7Loader_v3.27(%E6%BF%80%E6%B4%BB%EF%BC%89.rar%22%5D
#%5B%22%2FPCSKYS_Windows7Loader_v3.27(%E6%BF%80%E6%B4%BB%EF%BC%89.rar%22%5D




