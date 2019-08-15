class transCookie:
    def __init__(self, cookie):

        self.cookie = cookie

    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict

if __name__ == "__main__":
    cookie = "UM_distinctid=169ae2d44d6206-01e71b34e373ff-5d1f3b1c-144000-169ae2d44d7391; Hm_lvt_ecadf71bc8420c08afc6ccf1a4ab3466=1553405397; ASP.NET_SessionId=bgn340cjpdcjimwpiob3gnd3; CNZZDATA1271255678=1347482052-1553402687-%7C1553426690; Hm_lpvt_ecadf71bc8420c08afc6ccf1a4ab3466=1553426664"
    trans = transCookie(cookie)
    print(trans.stringToDict())