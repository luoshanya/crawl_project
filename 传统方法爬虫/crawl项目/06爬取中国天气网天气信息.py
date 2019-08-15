import  requests
from bs4 import BeautifulSoup




def request_data(url,headers):
    data = requests.get(url,headers=headers).content.decode('utf-8')
    parse_data(data)


def parse_data(data):
    soup = BeautifulSoup(data,'lxml')
    # bs4_data = soup.find_all(attrs={'class':'conMidtab'})[0]
    # bs4_data2 = soup.find_all('table')
    # print(bs4_data)
    list_data = []
    bs4_data = soup.select_one('.conMidtab')
    bs4_data2 = bs4_data.select('table tr')
    # print(bs4_data2)
    # bs3 = soup.select('.conMidtab table tr td')[18]
    # print(bs3)
    #
    for i in bs4_data2:
        name = i.select_one('a[target="_blank"]')
        print(name)
        # min_data = i.td[6]
        # print(min_data)
    #
    # for i in bs4_data:
    #     name = i.find_all('a')
    #     print(name)
    #
    #     for i in bs4_data:
    #         # print(i)
    #         dict_data = {}
    #         dict_data['name'] = i.find_all(name='a')[0]
    #         print(dict_data)
    #     dict_data['min_data'] = a.find_all('td')[6].string
    #     list_data.append(dict_data)
    #     print(dict_data)




def main():
    url = 'http://www.weather.com.cn/textFC/hb.shtml'
    headers = {
        'User-Agent' : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    #这里需要传参  这样前面的函数才会接收到数据
    request_data(url,headers)

if __name__ == '__main__':
    main()