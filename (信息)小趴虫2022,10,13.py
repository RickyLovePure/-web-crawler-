import re #re 是正则表达式，来匹配数据
# import requests #获取网页内容
# def go():
#     #定义要爬的url
#     url = "https://www.beesproxy.com/free/page/2" #这是要爬的网站
#     print(get_page(url).text)
# def get_page(url):#获取网页内容函数
#     return requests.get(url=url,headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'})
# #url①是X上面传来的url,head用来伪装浏览器,用F12，点击网络，找user-agent
# if __name__ == '__name__':
#     go() #开局调用go函数
import requests        #导入requests包
url = 'https://www.beesproxy.com/free/page/2'
strhtml = requests.get(url)        #Get方式获取网页数据
# print(strhtml.text)  能把整个网页的源代码给爬下来
html=strhtml.text
a=re.findall(re.compile(r'<tr>(.*?)</tr>',re.S),html) #得到tr里面的信息,S好像是和换行符有关
# for i in a:
#     print(a)
# print(a[0])
# 得到：
# < th
# scope = "col" > IP < / th >
# < th
# scope = "col" > 端口 < / th >
# < th
# scope = "col" > 地理位置 < / th >
# < th
# scope = "col" > 匿名度 < / th >
# < th
# scope = "col" > 协议 < / th >
# < th
# # scope = "col" > 最后验证时间 < / th >
a.remove(a[0])
list_=[]
for i in a:
    b=re.findall(re.compile(r'<td>(.*?)</td>'),i)
    print(b)  #已经基本能看了
#     data ={
#         'ip':b[0],
#         'ip':b[1],
#     }
#     list_.append(data)
# print(list_)


