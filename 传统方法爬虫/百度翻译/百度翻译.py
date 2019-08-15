import requests
import json
import execjs

class BaiDuFanYi():
    def __init__(self):
        query = input('请输入你需要翻译的语言:')
        self.query = query
        #需要加cookies
        self.headers = {'Cookie' : 'BAIDUID=DAB02B7154D1D96A66B95973178AC6B8:FG=1; BIDUPSID=DAB02B7154D1D96A66B95973178AC6B8; PSTM=1549356183; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=UVjb21xSUR6WkJjc3ZQVUJtNWdIUnNaVjlTV1BkdHc3VTZHeVpKQk9FdC1tTE5jQVFBQUFBJCQAAAAAAAAAAAEAAADx7-41WktMQVpITAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH4LjFx-C4xcd; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1427_21084_28772_28721_28558_28697_28584_28603_28627_28605; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=7; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1551345985,1552329254,1553851719,1553857245; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1553857245; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        self.lang_url = 'https://fanyi.baidu.com/langdetect'
        self.trans_url = 'https://fanyi.baidu.com/v2transapi'


    def parse_url(self,url,data):
        response = requests.post(url,data=data,headers=self.headers).content.decode('utf-8')
        # print(json.loads(response))
        return json.loads(response)


    def trans_data(self,data):

        # print(data)
        return  data['trans_result']['data'][0]['dst']

    def js_data(self):
        with open("baidu.js") as f:
            jsData = f.read()
            sign = execjs.compile(jsData).call("e", self.query)
            return sign


    def run(self):
        #首先得对这个网页进行分析 post请求 需要data数据 还有对语言的类型进行抓取
        #1.抓取语言类型 因为这直接影响了后面翻译需要使用的form数据
        lang_data = {'query': self.query}
        lang = self.parse_url(self.lang_url,lang_data)['lan']
        # print(lang)
        print(self.js_data())
        trans_data = {'from':'zh','to': 'en','query': self.query,'simple_means_flag':' 3','sign':self.js_data(),'token': '95c87156a5c19d6f17dde00cd4929146'} if lang == 'zh' else {'from':'en','to': 'zh','query': self.query,'simple_means_flag':' 3','sign':self.js_data(),'token': '95c87156a5c19d6f17dde00cd4929146'}
        print(trans_data)
        translation_result = self.parse_url(self.trans_url,trans_data)
        result = self.trans_data(translation_result)
        print(result)


if __name__ == '__main__':
    baidufanyi = BaiDuFanYi()
    baidufanyi.run()

#
# import requests
# import execjs
# import json
#
#
# class BaiDuTranslateWeb:
#     def __init__(self):
#         self.url = "https://fanyi.baidu.com/v2transapi"
#         self.headers = {
#             "Cookie": "BAIDUID=DAB02B7154D1D96A66B95973178AC6B8:FG=1; BIDUPSID=DAB02B7154D1D96A66B95973178AC6B8; PSTM=1549356183; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=UVjb21xSUR6WkJjc3ZQVUJtNWdIUnNaVjlTV1BkdHc3VTZHeVpKQk9FdC1tTE5jQVFBQUFBJCQAAAAAAAAAAAEAAADx7-41WktMQVpITAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH4LjFx-C4xcd; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1427_21084_28772_28721_28558_28697_28584_28603_28627_28605; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=7; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1551345985,1552329254,1553851719,1553857245; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1553857245; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D",
#             "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
#         }
#         self.data = {
#             "from": "zh",
#             "to": "en",
#             "query": None,
#             "transtype": "translang",
#             "simple_means_flag": 3,
#             "sign": None,
#             "token": "300f465c88543c5218f056447a33a348"
#         }
#
#     def get_baidu_sign(self):
#         with open("baidu.js") as f:
#             jsData = f.read()
#             sign = execjs.compile(jsData).call("e", self.input)
#             return sign
#
#     def run(self):
#         self.input = input("请输入要翻译的内容：")
#         self.get_baidu_sign()
#         self.data["query"] = self.input
#         self.data["sign"] = self.get_baidu_sign()
#         response = requests.post(url=self.url, data=self.data, headers=self.headers)
#         self.result_strs = response.content.decode()
#
#     def get_translate_result(self):
#         result_dict = json.loads(self.result_strs)
#         if 'trans_result' in result_dict:
#             result_dict = result_dict['trans_result']['data'][0] if len(
#                 result_dict['trans_result']['data']) > 0 else None
#             result_dict = result_dict['result'][0] if len(result_dict['result']) > 0 else None
#             result = result_dict[1] if len(result_dict) > 1 else None
#             print("翻译结果为：")
#             print(result)
#         else:
#             print("请输入内容再进行翻译")
#
#
# if __name__ == '__main__':
#     while True:
#         baidutranlate = BaiDuTranslateWeb()
#         baidutranlate.run()
#
#         baidutranlate.get_translate_result()
