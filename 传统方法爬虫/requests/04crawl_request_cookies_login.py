import requests
import ssl


#ssl错误：requests.exceptions.SSLError: HTTPSConnectionPool(host='www.yaozh.com', port=443): Max retries exceeded with url: /login/ (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1051)')))

def crawl_simulation_login():
    login_url = "https://www.yaozh.com/login"
    center_url = "https://www.yaozh.com/member/"
    login_from_data = {
        "username": "zhukelin",
        "pwd": "as751286012",
        "formhash": "6E1A90D3A4",
        "backurl": "https%3A%2F%2Fwww.yaozh.com%2F"
    }
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    #session类 可以自动保存cookie ===cookiejar
    session = requests.session()
    # 代码登录 post请求
    login_response = session.post(login_url,data=login_from_data,verify=False)
    print(login_response)
    # 登录成功后 带着有效的cookies 访问请求目标数据
    data = session.get(center_url,headers=header).content.decode('utf-8')
    with open("simulation_login1.html","w",encoding='utf-8') as f:
        f.write(data)
crawl_simulation_login()
