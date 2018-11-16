import requests
# aa = [{'domain': '.baidu.com', 'expiry': 1561106066.337054, 'httpOnly': False, 'name': 'BAIDUID', 'path': '/', 'secure': False, 'value': '36ACA9FD8038A3975297D6645D3EBFC1:FG=1'}, {'domain': '.pan.baidu.com', 'expiry': 1532162072.730347, 'httpOnly': True, 'name': 'STOKEN', 'path': '/', 'secure': False, 'value': '1a3df303ab08d21db28f62f60bc23e985ff148a03ead8e286f4cfe0b371e91b3'}, {'domain': '.pan.baidu.com', 'expiry': 1561106081, 'httpOnly': False, 'name': 'Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0', 'path': '/', 'secure': False, 'value': '1529570075'}, {'domain': '.baidu.com', 'expiry': 2556057600, 'httpOnly': False, 'name': 'FP_UID', 'path': '/', 'secure': False, 'value': '94f055abfad1e58391f7cea9369a9802'}, {'domain': '.baidu.com', 'expiry': 1788770072.1992, 'httpOnly': True, 'name': 'BDUSS', 'path': '/', 'secure': False, 'value': 'XNVTXh3S2JUcldDMnJ5RmZNTDVNQ3U3SmlhVXo1Qklnb2RDVno4WHR5WVQ4RkpiQVFBQUFBJCQAAAAAAAAAAAEAAABHw33SeHBmZG93bmxvYWQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABNjK1sTYytbN'}, {'domain': '.pan.baidu.com', 'expiry': 1529656480.267498, 'httpOnly': True, 'name': 'PANPSC', 'path': '/', 'secure': False, 'value': '2557542760936141013%3A9qIJoSpryQ%2BSHDSX00ggOXiC6e0Ll37pnsoQ9bt%2FKHFm2IshwTJ1%2FIM6La9EbgvRaHvCT74H35%2BcirLYelOtHyryq5WQF2At3BiYY7fMLEW5e2NAaU%2B52eXH25HnNztW3%2B97bREolCSqWWjWU7Q6nhL1pF4HikBsKg6bXhEDmDbnWBd3obeFYeCZFY35Hy9z1NoL83Y93Vo%3D'}, {'domain': '.pan.baidu.com', 'expiry': 1561106072.423371, 'httpOnly': False, 'name': 'PANWEB', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.pan.baidu.com', 'expiry': 1532162072.730381, 'httpOnly': True, 'name': 'SCRC', 'path': '/', 'secure': False, 'value': '6bf6ebb514046b6c056ae39840c021ad'}, {'domain': '.pan.baidu.com', 'expiry': 1532162076.269103, 'httpOnly': False, 'name': 'BDCLND', 'path': '/', 'secure': False, 'value': '8EpxNtXQ828qebB1rJFRxweeq6Ylystx'}, {'domain': '.pan.baidu.com', 'httpOnly': False, 'name': 'Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0', 'path': '/', 'secure': False, 'value': '1529570082'}]
# for a in aa:
# 	if a["name"]=='STOKEN':
# 		stoken = a["value"]
# 	if a["name"]=="BDUSS":
# 		bduss = a["value"]
# print(stoken)
# print(bduss)

headers = {
	"Accept": "application/json, text/javascript, */*; q=0.01",
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "zh-CN,zh;q=0.9",
	"Connection": "keep-alive",
	"Content-Length": "74",
	"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
	"Host": "pan.baidu.com",
	"Origin": "https://pan.baidu.com",
	"Referer": "https://pan.baidu.com/s/1rhhKLdoJLdWh9-Dc-SUbsg",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36",
	"X-Requested-With": "XMLHttpRequest"
}

cookies = {
	"BAIDUID": "74879EA431EB3A87ED4BEA86C4D829CB:FG=1",
	"FP_UID":"3f54de73aa7f70f8bbb17bf3501e4dfc",
	"BDUSS":"J5LThGTjRxUDV6dEpHZFhCVXlZV3QyamNiMGpDT3QtQ2llSnlkY2xEMDExRk5iQVFBQUFBJCQAAAAAAAAAAAEAAABHw33SeHBmZG93bmxvYWQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADVHLFs1RyxbRn",
	"PANWEB":"1",
	"STOKEN":"6ab631ae7b7ff32eeed1ad1f54efdc82b7a263a08f3419e3bb19df185e30612a",
	"SCRC":"74a39a53a14be7b54962aadae22e07eb",
	"Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0":"1529628478",
	"BDCLND":"8EpxNtXQ829TdxRgIpDTklBHd%2BykaGnr",
	"Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0":"1529628485",
	"PANPSC":"6555002601273954923%3A9qIJoSpryQ%2BSHDSX00ggOXiC6e0Ll37pnsoQ9bt%2FKHFm2IshwTJ1%2FIM6La9EbgvRCRAlW0YE4hh9ZGuk%2BIvHUSryq5WQF2At3BiYY7fMLEW5e2NAaU%2B52eXH25HnNztW3%2B97bREolCSqWWjWU7Q6nhL1pF4HikBsKg6bXhEDmDbnWBd3obeFYeCZFY35Hy9z1NoL83Y93Vo%3D"
}

url = "https://pan.baidu.com/share/transfer?shareid=3195004918&from=75178857&channel=chunlei&web=1&app_id=250528&bdstoken=585d97c1b67719b49d4886062406beae&logid=MTUyOTYyODUxMjMzNzAuOTU4NTEwOTA5NTU4MDAwNA==&clienttype=0"

form_data = {
	"filelist": "[\"/java/JAVA_API_1.7中文.chm\"]",
	"path": "/"
}

resp = requests.post(url,data=form_data,headers=headers,cookies = cookies)
print(resp.text)