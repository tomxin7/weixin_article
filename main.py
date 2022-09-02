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
        'Referer': 'https://mp.weixin.qq.com/cgi-bin/appmsgpublish?sub=list&begin=0&count=10&token=1365441957&lang=zh_CN',
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


token = "1053990675"
cookie = "RK=sFrQ+6HvWT; ptcz=4ad36ffbeef612d306a296e78187bdf5f7b4378eef4151fd858542ddfa85fda0; tvfe_boss_uuid=b5ca66b0be9a2b07; ua_id=qGoLOOJAKmPFMYzCAAAAADlklV4S9dzXM3H2B4gaw9A=; wxuin=18646164787405; mm_lang=zh_CN; ts_uid=5662132727; fqm_pvqid=f4db72c6-37ed-4fe0-b536-3c7ce818e59b; o_cookie=865498311; iip=0; pac_uid=1_865498311; _ga_BZRZ902N6M=GS1.1.1638710126.1.0.1638710147.0; _ga_L60K2WSGBF=GS1.1.1638710148.1.1.1638710633.0; pgv_pvi=4307568640; _ga=GA1.2.389498448.1624170616; pgv_pvid=8151499213; _tc_unionid=6278008b-cceb-4439-af00-aa90b5c6207a; _clck=3072791820|1|f4j|0; uuid=e75265f52f0c60346e981ef551447a36; rand_info=CAESIHd1uy5g3qOjALgTolAdMEN/wQncI0BwdQh66Vuo+Q1V; slave_bizuin=3238306019; data_bizuin=3238306019; bizuin=3238306019; data_ticket=+2BTnHYML/PwrkImHnZwkuKBYYCeLZK0wBA5Tspt0sktVWA1wxcc3yoAA1rrSiAs; slave_sid=Q2VwVlRKeWNfeXZyWjQ2OTdFVjVhN0ZBY0h1am51MUg5UUdnWnZkU1VIYkhVUTR1ZkF2dG53VU80cDdLV1M4bGhoZlRvZWV0MllSOWpPc2pFTUFhbzFYNmNJUWtSUlhYTHFmdUtRZFNDY3lkRmNRdHZ5dGwwTEFaU0xSdlRrTURNYm1YeE5JWnBiV05RTnhG; slave_user=gh_4e336b7da458; xid=3a4ff07b9c1cc061520baf6dd53154e6"
if __name__ == '__main__':
    begin = 0
    i = 1
    while (flag):
        print("获取第" + str(i) + "页")
        main(begin)
        begin += 10
        i += 1
    print("导出完成")
