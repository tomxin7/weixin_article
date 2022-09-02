import re

import requests
import json
import time

'''
正则表达式返回整个匹配的列表
'''


def get_list(info, reStart, reEnd):
    regex = r'' + reStart + '(.*?)' + reEnd
    pat = re.compile(regex, re.S)
    content = re.findall(pat, info)
    return content


'''
正则表达式只返回第一个匹配的
'''


def get_first(info, reStart, reEnd):
    regex = r'' + reStart + '(.*?)' + reEnd
    pat = re.compile(regex, re.S)
    content = re.findall(pat, info)
    return content[0]


def write_new_txt(content):
    path = "weixin.html"
    with open(path, "a", encoding="utf-8") as f:
        f.write(content + "\n")


def get_info(url):
    payload = {}
    global cookie
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:103.0) Gecko/20100101 Firefox/103.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Cookie': cookie,
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'TE': 'trailers'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text


def get_detail(url):
    info = get_info(url)
    info = get_first(info, '<div class="rich_media_content',
                     '<script type="text/javascript"')
    info = '<div class="rich_media_content' + info
    info = info.replace("</strong>", "\n").replace("</span>", "\n")
    pattern = re.compile(r'<[^>]+>', re.S)
    result = pattern.sub('', str(info))
    return result


num = 1
flag = True

model = '''
<h3>{num}、{title}</h3>
<a target="_blank" href="{url}">点击跳转到微信文章</a>
<h3>内容：</h3>
<p style="font-size:16px;white-space: pre-line;">{detail}</p>
'''

def main(begin):
    global token
    global num
    global flag
    url = "https://mp.weixin.qq.com/cgi-bin/appmsgpublish?sub=list&begin={begin}&count=10&token={token}&lang=zh_CN".replace(
        "{begin}", str(begin)).replace("{token}", token)
    info = get_info(url)
    info = get_first(info, "publish_page =", "isPublishPageNoEncode")
    info = str(info).replace(" ", "").replace("};", "}").replace("&quot;", "")
    info = json.loads(info)
    publish_list = info['publish_list']
    write_new_txt('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />')
    if len(publish_list) < 10:
        flag = False
    for publish in publish_list:
        try:
            publish = str(publish)
            title = get_first(publish, "title:", ",is_deleted")
            content_url = get_first(publish, "content_url:.+?s?__biz", ",title:")
            content_url = "https://mp.weixin.qq.com/s?__biz" + content_url
            print(title)
            print(content_url)
            detail = get_detail(content_url)
            html = model.replace("{title}", title).replace("{url}", content_url).replace("{detail}", detail).replace(
                "{num}", str(num))
            write_new_txt(html)
            num += 1
        except Exception as e:
            print("文章已删除，跳过")
            print(e)
        time.sleep(1)


token = ""
cookie = ""
if __name__ == '__main__':
    begin = 0
    i = 1
    while (flag):
        print("获取第" + str(i) + "页")
        main(begin)
        begin += 10
        i += 1
    print("导出完成")
