# #
# #
# #
# dict_data = 'acw_tc=2f624a0515512677621551497e3b45fc21cc4993bec3b66097298b4d2f5af6; _ga=GA1.2.1912755189.1551267759; _gid=GA1.2.1265000741.1551267759; MEIQIA_EXTRA_TRACK_ID=1HlDPR7oAd6PDoNK1fY0ZfeO5PX; think_language=zh-CN; _gat=1; yaozh_userId=700746; yaozh_uidhas=1; acw_tc=2f624a0515512677621551497e3b45fc21cc4993bec3b66097298b4d2f5af6; MEIQIA_VISIT_ID=1HlDPSplYHyyd7siY0XAKgfkoDK; MEIQIA_EXTRA_TRACK_ID=1HlDPR7oAd6PDoNK1fY0ZfeO5PX; UtzD_f52b_saltkey=NzGN3K1P; UtzD_f52b_lastvisit=1551264450; UtzD_f52b_ulastactivity=1551268037%7C0; UtzD_f52b_creditnotice=0D0D2D0D0D0D0D0D0D642384; UtzD_f52b_creditbase=0D0D0D0D0D0D0D0D0; UtzD_f52b_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95; PHPSESSID=fo15u1d4ongpgtkgebsrcd4356; MEIQIA_VISIT_ID=1HmsqntTEG0EiuP1HZM1bzIiO52; yaozh_logintime=1551322261; yaozh_user=700746%09zhukelin; db_w_auth=642384%09zhukelin; UtzD_f52b_lastact=1551322262%09uc.php%09; UtzD_f52b_auth=0399WzIhvn1Fu%2F47yHRCEdQnDn59FdE8ZuTYR1ONc%2BKlHDxRExiBnwuBVPQP3lM%2FskfcEMyd5%2FG6jJkbockEeJTdLuI; yaozh_mylogin=1551322265; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1551267759%2C1551267973%2C1551318793; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1551322269'
# cookie_dict = {}
# dict_list = dict_data.split('=')[0]
#
# # for dict_data in dict_list:
# #     cookie_dict[dict_data.split('=')[0]] = dict_data.split('=')[1]
#
#
# # cookie_dict = {dict_data.split('=')[0]:dict_data.split('=')[1] for dict_data in dict_data.split('; ')}
#
#
# # str_list = []
# test = [
#     "abs",
#     "bs",
#     "cd"
# ]
# # import json
# # data = json.dumps(test)
# # print(data)
# # for i in test:
# #     dicts = {}
# #     str_list.append(dicts)
# #     print(str_list)、
# a = ""
# for i in test:
#
#     url = a.format(i)
#     print(url)


# x = 1
# a = 'sacacniceiod'
# print('%dhttp://www.bejson.com/%s'% (x,a))
# def ab():
#     a = 8
#     if a > 9:
#         a += 1
#         return a
#     return a
#     e=0
#     for i in (10,20):
#         # global a
#         a += 1
#         print('=')
#         print(a)
#         for i in (10,20):
#             # if a >10:
#             e += 1
#             print('====')
#             print(e)
#             # return a
#         print('======')
#         print(a)
#         return a
# ab()
# print(ab())
#
# for i in range(0,5):
#     print(i)
# def apply_to_list(some_list, f):
#     return [f(x) for x in some_list]
#
# ints = [4, 0, 1, 5, 6]
# t = apply_to_list(ints, lambda x: x * 2)
# print(t)
# a = [1,2,3,4]
# t = list(map(lambda x:x* 2,a))
# print(t)


#
# strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
# #set去重
# strings.sort(key=lambda x: len(set(list(x))))
# print(strings)

def add_numbers(x, y):
    return x + y
t = lambda y:add_numbers(5,y)
print(t)
from functools import partial
add_five = partial(add_numbers, 5)
print(add_five)












