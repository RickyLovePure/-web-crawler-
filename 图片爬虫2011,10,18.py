import requests #引入requests模块用来处理请求
import os #引入os模块用来存储文件
if not os.path.exists('D:\\Desktop\\创建文件夹'):
    os.mkdir('D:\\Desktop\\创建文件夹')
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'
}
#粘贴图片地址
src= "http://img.soogif.com/0Hy0iUj4T0hwELRUd5umISJJUkOOI7OM.gif";
#根据图片地址定义文件名
imgName = src.split('/')[-1]
#获取图片数据
imgRes = requests.get(src,headers=headers,timeout=3)
#将图片保存到本地
with open(imgName,'wb') as f:
    f.write(imgRes.content)
# with open('D:\\Desktop\\创建文件夹', 'wb') as f:
#     f.write(imgRes.content)
import shutil
 
#将d盘下的123.txt文件复制到d盘下test目录中，并重命名为234.txt
shutil.copyfile('C://Users//12553//0Hy0iUj4T0hwELRUd5umISJJUkOOI7OM.gif','D://Desktop//创建文件夹//搞笑.gif')
os.remove("0Hy0iUj4T0hwELRUd5umISJJUkOOI7OM.gif")
print("下载成功")

'''os.mkdir('E:\\PY练习\\创建文件夹')如果创建的文件夹存在，程序报错，推荐先验证是否存在'''
 


