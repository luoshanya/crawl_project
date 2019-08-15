import requests
import json
from lxml import etree


url = 'https://36kr.com/api/search-column/mainsite?per_page=20&page=3&_=1553104796618'
# for i in range(1):
    # url = 'http://product.dangdang.com/index.php?r=comment/list&productId=25340451&pageIndex=1'
    # url = 'http://product.dangdang.com/index.php?r=comment/list&productId=25340451&categoryPath=01.07.07.04.00.00&mainProductId=25340451&mediumId=0&pageIndex={}'.format(i)
headers = {
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    # 'Cookies' : 'td_cookie=597808914; _xsrf=CqKHL10Ga8PIBZJkQ0LnfJAJWsvphH2q; _zap=b599d45d-c1e8-47b2-be4e-b9f17a40c56e; d_c0="AFCkd0HECw-PTmNj5njYHKcuhEW-5s5j4CE=|1551267682"; q_c1=4a6990f9a6474e1191721b945d79023e|1551346262000|1551346262000; tst=r; tgw_l7_route=060f637cd101836814f6c53316f73463; capsion_ticket="2|1:0|10:1553088915|14:capsion_ticket|44:M2M3MWM2Yzc0MTgzNGIwYjhmZGNmNWYyMWYzNGRmYjQ=|191c9e627731b7dc8e8403bf98b5d3a31ba24177cf1bf0cd2833383290dcbb7f"'
}
response = requests.get(url,headers=headers,
                        timeout=5)
print('='*40)
print(response)
json_text = response.text
# print('='*40)
# print(json_text)
text = json.loads(json_text)
print('='*40)
print(text)
    # etree_data = etree.HTML(text)
    # print(etree_data)
    # xpath_data = etree_data.xpath('//ul[@class="feed_ul"]/li')
    # print(xpath_data)
    # for i in xpath_data:
    #
    #     title = i.xpath('.//div[@class="intro"]/h3/text()')
    #     print(title)


