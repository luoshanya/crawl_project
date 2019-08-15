# -*- coding: utf-8 -*-
from urllib import request,parse
import string


url = 'https://www.lagou.com/jobs/positionAjax.json?px=new&city=上海&needAddtionalResult=false&isSchoolJob=0'
#{"status":false,"msg":"您操作太频繁,请稍后再访问","clientIp":"112.96.182.89","state":2402}  如果出现这个错误 那代表请求头还不够，需要更多信息
headers = {
    # 'User-Agent' : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    # 'Referer' : 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    # 'Origin' : 'https://www.lagou.com',
    # 'Host' : 'www.lagou.com',
    # 'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'JSESSIONID=ABAAABAAAIAACBI50662FE3ABF087859A2BD8DBC42B6BDC; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1552135271; _ga=GA1.2.1542991.1552135271; _gid=GA1.2.949220323.1552135271; user_trace_token=20190309204111-9e7ac5a9-4268-11e9-87ae-525400f775ce; LGSID=20190309204111-9e7ac83d-4268-11e9-87ae-525400f775ce; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DKIqh9hZOaGfCjVK-AuinlYVfetg5COyRWithe72AnnO%26wd%3D%26eqid%3Dc574ea1f00116306000000065c83b45c; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGUID=20190309204111-9e7ac9d7-4268-11e9-87ae-525400f775ce; index_location_city=%E5%B9%BF%E5%B7%9E; TG-TRACK-CODE=search_code; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1552135582; LGRID=20190309204622-57b9b25d-4269-11e9-87c3-525400f775ce; SEARCH_ID=95eaedbd6d2b4defba6560f5dec32b1d',
    # 'Accept':'application/json, text/javascript, */*; q=0.01',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    # 'Connection': 'keep-alive',
    # 'Content-Length': 25,
    # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'X-Anit-Forge-Code': 0,
    # 'X-Anit-Forge-Token': 'None',
    # 'X-Requested-With': 'XMLHttpRequest'
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
'Connection': 'keep-alive',
'Content-Length': 25,
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': 'JSESSIONID=ABAAABAAAIAACBI50662FE3ABF087859A2BD8DBC42B6BDC; _ga=GA1.2.1542991.1552135271; _gid=GA1.2.949220323.1552135271; user_trace_token=20190309204111-9e7ac5a9-4268-11e9-87ae-525400f775ce; LGUID=20190309204111-9e7ac9d7-4268-11e9-87ae-525400f775ce; index_location_city=%E5%B9%BF%E5%B7%9E; TG-TRACK-CODE=search_code; X_MIDDLE_TOKEN=46d59f1928c11b5cff51c75f20dfefe0; WEBTJ-ID=20190309212033-169629cbeb527-08b735876bc8bb-5d1f3b1c-1327104-169629cbeb8f8; LGSID=20190309212047-267349f4-426e-11e9-8ed2-5254005c3644; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.Ks000001qLT2daZnZ8gNTZvsdDNEefwvsbHUH77sBi1ECp5bSOwtvnXu4YzKYp9QVtrmsonPbeL6EsXUGzMKApSjQgD0aHYOzd06wOhwuwGHmv86czy8SNm0onXM8p6O8fvPmSTSm2jd4CxGVKvuStnWvuIidGpqkyN4zjCgHUwb8-0Hh2nvWddCLfmTSq3UkPj5WmghFI6ZHA9yK0.7b_NR2Ar5Od663rj6tJQrGvKD7ZZKNfYYmcgpIQC8xxKfYt_U_DY2yr8M-eXKBqM76dkt_rrZ-dT5QgjujbLt8EgvUvU8gj4qrZul3IhOj4e_r1dsSEM9tSMj__se55j4qhZdL3Ih1j4qrZvvmxgkRdrYG4TXGmuCynMWklpd0.U1Yk0ZDqs2v4VnL30ZKGm1Ys0Zfqs2v4VPHdseHwSfKGUHYznjf0u1dBugK1nfKdpHdBmy-bIfKspyfqP0KWpyfqrjf0UgfqnH0kPdtknjD4g1csPWFxnH0zndt1PW0k0AVG5H00TMfqnHf30ANGujYkPjcLg1cknj6Yg1c3PW0Lg1c3PH6Yg1c3PHR3g1c3PW01g1c3PWcLg1c3PW0d0AFG5Hfsn-tznjwxnHRd0AdW5H6kPH0zPH6zP7tknj0kg1DsrHndPjTLrHNxnNts0Z7spyfqn0Kkmv-b5H00ThIYmyTqn0K9mWYsg100ugFM5H00TZ0qrH0YrjRkPjfk0A4vTjYsQW0snj0snj0s0AdYTjYs0AwbUL0qn0KzpWYs0Aw-IWdsmsKhIjYs0ZKC5H00ULnqn0KBI1Ykn0K8IjYs0ZPl5fK9TdqGuAnqTZnVuLG8TsKYIgnqPHmYP163rHc3nWTvPjbknjf3PsKzug7Y5HDdPHckn1TdrHckPWT0Tv-b5H64nvDdrHFBnj0srHuhnj60mLPV5RmsPW64f1mdP1wAwDNawWR0mynqnfKsUWYs0Z7VIjYs0Z7VT1Ys0ZGY5HD0UyPxuMFEUHYsg1Kxn7tsg100uA78IyF-gLK_my4GuZnqn7tsg1Kxn7ts0ZK9I7qhUA7M5H00uAPGujYs0ANYpyfqQHD0mgPsmvnqn0KdTA-8mvnqn0KkUymqn0KhmLNY5H00uMGC5H00uh7Y5H00XMK_Ignqn0K9uAu_myTqnfK_uhnqn0KWThnqnHnknWD%26word%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26ck%3D3796.15.96.331.553.214.555.273%26shh%3Dwww.baidu.com%26sht%3Dbaiduhome_pg%26us%3D1.0.2.0.3.1941.0%26bc%3D110101; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3D%26m_kw%3Dbaidufs_cpc_gz_1c0c29_ff49ad_%25E6%258B%2589%25E5%258B%25BE%25E6%2580%258E%25E4%25B9%2588%25E6%25A0%25B7; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1552135271,1552137635,1552137646,1552137654; LGRID=20190309212059-2df6d388-426e-11e9-87ed-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1552137659; SEARCH_ID=2e59e7669659493b849c07f0cba864f8',
'Host': 'www.lagou.com',
'Origin': 'https://www.lagou.com',
'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=sug&fromSearch=true&suginput=p',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
'X-Anit-Forge-Code': 0,
'X-Anit-Forge-Token': 'None',
'X-Requested-With': 'XMLHttpRequest'

}
data = {
    'first': 'true',
    'pn': '1',
    'kd': 'python'
}
data_encode = parse.urlencode(data)
#TypeError: can't concat str to bytes  出现这个错误代表需要用parse转类型
req = request.Request(url,headers=headers,data=parse.quote(data_encode,safe=string.printable).encode('utf-8'),method='POST')
requ =request.urlopen(req)
print(requ.read())