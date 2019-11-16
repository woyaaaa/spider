import requests

url = "http://www.baidu.com"


###
# response.encoding = "utf-8"
# print(response.text)
###
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}
response = requests.get(url,headers=headers)
print(response.content.decode())