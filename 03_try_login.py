import requests

# 实例化session
mySession = requests.session() 

# 使用session 发送post请求，获取对方保存在本地的cookies

post_url = "https://www.battlenet.com.cn/login/zh/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}
#post_data = {"accountName": "woyaaaa", "password":"Liuyang!!5978"}
post_data = {"email": "woyaaaa@163.com", "password":"Liuyang!!5978"}
mySession.post(url= post_url,headers=headers,data=post_data)

#使用session后登录的uer网址
url= "https://account.blizzardgames.cn/overview"
response = mySession.get(url,headers = headers)

with open("test.html","w",encoding= "utf-8") as f:
    f.write(response.content.decode())