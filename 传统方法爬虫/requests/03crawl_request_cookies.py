import requests
import ssl


#ssl错误：requests.exceptions.SSLError: HTTPSConnectionPool(host='www.yaozh.com', port=443): Max retries exceeded with url: /login/ (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1051)')))

def crawl_simulation_login():
    login_url = "https://www.yaozh.com/member/"

    login_from_data = {
        "username": "zhukelin",
        "pwd": "as751286012",
        "formhash": "6E1A90D3A4",
        "backurl": "https%3A%2F%2Fwww.yaozh.com%2F"
    }
    #cookies字符串类型
    cookies = 'acw_tc=2f624a0515512677621551497e3b45fc21cc4993bec3b66097298b4d2f5af6; _ga=GA1.2.1912755189.1551267759; _gid=GA1.2.1265000741.1551267759; MEIQIA_EXTRA_TRACK_ID=1HlDPR7oAd6PDoNK1fY0ZfeO5PX; think_language=zh-CN; _gat=1; yaozh_userId=700746; yaozh_uidhas=1; acw_tc=2f624a0515512677621551497e3b45fc21cc4993bec3b66097298b4d2f5af6; MEIQIA_VISIT_ID=1HlDPSplYHyyd7siY0XAKgfkoDK; MEIQIA_EXTRA_TRACK_ID=1HlDPR7oAd6PDoNK1fY0ZfeO5PX; UtzD_f52b_saltkey=NzGN3K1P; UtzD_f52b_lastvisit=1551264450; UtzD_f52b_ulastactivity=1551268037%7C0; UtzD_f52b_creditnotice=0D0D2D0D0D0D0D0D0D642384; UtzD_f52b_creditbase=0D0D0D0D0D0D0D0D0; UtzD_f52b_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95; PHPSESSID=fo15u1d4ongpgtkgebsrcd4356; MEIQIA_VISIT_ID=1HmsqntTEG0EiuP1HZM1bzIiO52; yaozh_logintime=1551322261; yaozh_user=700746%09zhukelin; db_w_auth=642384%09zhukelin; UtzD_f52b_lastact=1551322262%09uc.php%09; UtzD_f52b_auth=0399WzIhvn1Fu%2F47yHRCEdQnDn59FdE8ZuTYR1ONc%2BKlHDxRExiBnwuBVPQP3lM%2FskfcEMyd5%2FG6jJkbockEeJTdLuI; yaozh_mylogin=1551322265; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1551267759%2C1551267973%2C1551318793; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1551322269'
    #但是cookies需要的是 字典类型  出现错误：TypeError: string indices must be integers
    #第一种方法，将字典划分
    cookies_dict = {}
    cookies_split = cookies.split('; ')

    # for cookies in cookies_split:
    #     print(type(cookies))
    #     cookies_dict[cookies.split('=')[0]] = cookies.split('=')[1]
    #第二种方法：字典推导式
    # print(cookies_split)
    cookies_dict1 = {cookies.split('=')[0]:cookies.split('=')[1] for cookies in cookies_split}
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }

    login_request = requests.get(login_url,headers=header,cookies=cookies_dict1,verify=False)

    data = login_request.content.decode("utf-8")
    with open("simulation_login.html","w",encoding='utf-8') as f:
        f.write(data)
crawl_simulation_login()
