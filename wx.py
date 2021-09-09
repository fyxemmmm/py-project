import re
from selenium import webdriver
import requests

url = 'https://mp.weixin.qq.com/s?__biz=MzUxODAzNDg4NQ==&mid=2247485318&idx=1&sn=0da0a684639106f548e9d4454fd49904&chksm=f98e432ccef9ca3ab4e10734fd011c898785f18d842ec3b148c7a8ee500790377858e0dbd8d6&scene=178&cur_album_id=1408057986861416450#rd'
prefix = "jctx"

i = 0


def save_image(url):
    global i
    img = requests.get(url)
    image_name = 'images/' + prefix + '-' + str(i) + ".jpg"
    with open(image_name, 'wb') as f:
        f.write(img.content)
        f.close()
    i += 1
    return


driver = webdriver.Chrome()
driver.get(url)
html = driver.page_source

lst = re.findall(r'data-src="(.*?)"', html)

image_url_list = []
for item in lst:
    if str(item).startswith("https://mmbiz.qpic.cn"):
        image_url_list.append(item)

for img_url in image_url_list:
    save_image(img_url)

driver.close()
