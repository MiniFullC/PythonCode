'''
抓取百度贴吧---手写吧的内容
爬虫线路： requests - bs4
Python版本： 3.6.6
OS： manjaro linux 414
'''

import requests
import time
from bs4 import BeautifulSoup


def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()

        # r.endcodding = r.apparent_endconding
        r.encoding = 'utf-8'
        return r.text
    except:
        return " ERROR "


def get_content(url):
    comments = []
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')

    # 找到所有具有‘ j_thread_list clearfix’属性的li标签。返回一个列表类型。
    liTags = soup.find_all('li', attrs={'class': ' j_thread_list clearfix'})

    # 通过循环找到每个帖子里的我们需要的信息：
    for li in liTags:

        # 初始化一个空字典来存储文章信息
        comment = {}


        try:
        
            # 开始筛选信息，并保存到字典中
            comment['title'] = li.find(
                'a', attrs={'class': 'j_th_tit '}).text.strip()
            comment['link'] = "http://tieba.baidu.com/" + \
                li.find('a', attrs={'class': 'j_th_tit '})['href']
            comment['name'] = li.find(
                'span', attrs={'class': 'tb_icon_author '}).text.strip()
            comment['time'] = li.find(
                'span', attrs={'class': 'pull-right is_show_create_time'}).text.strip()
            comment['replyNum'] = li.find(
                'span', attrs={'class': 'threadlist_rep_num center_text'}).text.strip()
            comments.append(comment)
        except:
            print('出了点小问题')

    return comments


'''
将爬取到的文件写入到本地
保存到当前目录的 Handwrite.txt文件中。
'''

def Out2File(dict):

    with open('Handwrie.txt', 'a+') as f:
        for comment in dict:
            f.write('标题： {} \t 链接：{} \t 发帖人：{} \t 发帖时间：{} \t 回复数量： {} \n'.format(
                comment['title'], comment['link'], comment['name'], comment['time'], comment['replyNum']))

        print('当前页面爬取完成')


def main(base_url, deep):
    url_list = []

    # 将所有需要爬去的url存入列表
    for i in range(0, deep):
        url_list.append(base_url + '&pn=' + str(50 * i))
    print('所有的网页已经下载到本地！ 开始筛选信息***********')

    #循环写入所有的数据
    for url in url_list:
        content = get_content(url)
        Out2File(content)
    print('所有的信息都已经保存完毕！')


base_url = 'http://dq.tieba.com/f?kw=%E6%89%8B%E5%86%99&ie=utf-8'
# 设置需要爬取的页码数量
deep = 3

if __name__ == '__main__':
    main(base_url, deep)
