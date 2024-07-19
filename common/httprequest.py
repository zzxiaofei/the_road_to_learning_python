import requests
import json
import base64


class HttpRequest:

    def __init__(self):
        self.session = requests.Session()  # 创建一个session会话保持cookies
        self.session.auth = ("admin", "123456")
        self.content_Type = {
            "Token": "qingfengtest",
            "Content-Type": "application/json",
        }
        self.init_headers(self.content_Type)

    def init_headers(self, headers):
        self.session.headers.update(headers)

    def json_to_dict(self, args):
        """json字符串和字典的转化"""
        if args:
            json_data = eval(args)
            return args

    def send_request(self, url, method, args, request_type=None, tiqu=None):
        args = self.json_to_dict(args)  # Get/form-data的入参格式是字典类型
        if request_type and request_type == 'json':
            args = json.dumps(args)
        elif request_type and request_type == 'form-data':
            self.init_headers({"Content-Type": "application/x-www-form-urlencoded"})
        res = self.session.request(url=url, method=method,
                                   params=args,
                                   data=args)

        self.init_headers(self.content_Type)
        return res.json()

    """
        :param  method: 请求方法 Get / Post
        :param  url: 请求地址
        :param  params: Get请求参数
        :param  headers: 请求头
        :param  json: json数据格式
        :param  data: 键值对，form表单
        :param  files:
        :param  kwargs: 不定长参数
        :param  Parameters: 请求参数传入方式 data/json
        :return
    """

    """
    1. 一个正常的 Get 请求
    """

    def request_get(self):
        """
        def get(url, params=None, **kwargs):
        :params
        {
            'key': 'value' # 字典传递参数，如果为NONE不会添加到url中
        }
        """

        # url = 'http://web.juhe.cn/finance/stock/hs'
        # apikey = '74c70200902ebe0e1330c54a8e0acb5d'
        # params = {
        #     'key': apikey,
        #     # 'gid': '',  # 股票编号，上海股市以sh开头，深圳股市以sz开头如：sh601009（type为0或者1时gid不传）
        #     'type': '0',  # 0代表上证综合指数，1代表深证成份指数(输入此字段时,gid字段不起作用)
        # }
        # print(params)
        # r = requests.get(url, params=params)
        # print(r.encoding)  # 获取当前的编码
        # r.encoding = 'utf-8'  # 设置编码
        # print(r.text)  # 字符串方式的响应体，会自动根据响应头部的字符编码进行解码。text适用于显示文本数据，编码根据服务器的响应来显示，也可以自己设置
        # print(r.content)  # 以字节形式（二进制）返回, content用来返回二进制数据，适用于保存二进制数据，例如图像，文件等
        # print(r.headers)  # 以字典对象存储服务器响应头
        # print(r.status_code)  # 响应状态码
        # print(r.json())  # 以json形式返回,前提返回的内容确保是json格式的，不然解析出错会抛异常

        """
        python字典和 json字符串直接的相互转化
        """
        # response = r.json()
        # print(response)
        #
        # response = r.json()  # 响应值response,字典类型
        # print('转化之前', type(response))
        # response = json.dumps(response)  # 把response字典转化为json字符串
        # print('转化之后', type(response))
        # response = json.loads(response)  # 把json字符串转化为字典
        # print('转化之后', type(response))

        # print(json.dumps(response, indent=4, ensure_ascii=False))  # 等于把显示在一行的字典，放bejson格式化校验
        # print(json.dumps(response, ensure_ascii=False, indent=4))
        # print(r.cookies)
        # print(r.url)

    def request_post(self):
        """

        """

    # '''接口2：获取用户信息'''
    #
    # h = {"token": "qingfengtest"}  # 定义的一个请求头，字典类型
    # p = {"limit": 1}  # 定义的参数，字典类型
    # res = requests.request(method='get',
    #                        url='http://127.0.0.1:7001/api/qingfeng/users',
    #                        params=p,
    #                        headers=h)
    #
    # print(res.status_code)
    # print(res.json())


#
#
# '''接口3:12306'''
# h = {
#     "Cookie": "_uab_collina=163171289127393441288275; JSESSIONID=A480B7E51DB427E671A9EAB429E0BF57; _jc_save_wfdc_flag=dc; _jc_save_fromStation=%u4E0A%u6D77%2CSHH; _jc_save_toStation=%u957F%u6C99%2CCSQ; BIGipServerotn=1173357066.50210.0000; BIGipServerpool_passport=233046538.50215.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; RAIL_EXPIRATION=1643100119736; RAIL_DEVICEID=sNfoLXTkSZyQ1Tk8feRzN3lS3MxlI5FBh2gCXgv5KRsU_DY4muckz0RS4M3FSq0NQVgclu6vPWcf_iS5q99UOyf58Px-VxHptormzrtjDPtelGTqyEtNunOscPbFFI6Zgs2IqJsx_X3JEaQ-z7RfDQ-T78O2LGDb; route=6f50b51faa11b987e576cdb301e545c4; _jc_save_toDate=2022-01-22; _jc_save_fromDate=2022-01-25"
# }
#
# res = requests.get(url='https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date=2022-01-25&leftTicketDTO.'
#                        'from_station=SHH&leftTicketDTO.to_station=CSQ&purpose_codes=ADULT',
#                    headers=h)
#
# # print(res.text)
# # print(res.content)
# print(res.json())
#
# ''''''
# '''第二个接口'''
# # url_text='http://127.0.0.1:7001/api/qingfeng/text'
# # d='qingfengtest'
# #
# # res=requests.request(method='post',url=url_text,data=d)
# # print('res.request.body',res.request.body)
# #
# # print(res.status_code)
# # print(res.json())
#
#
# '''第三个接口'''
# # url_json='http://127.0.0.1:7001/api/qingfeng/user'
# #
# # d={
# #     "username":"qingfeng",
# #     "phone":123455667
# # } #字典
# # res=requests.request(method='post',url=url_json,json=d)
# # print('res.request.body',res.request.body)
# # print(res.status_code)
# # print(res.json())
#
# #
# # '''第四个接口:json'''
# # url_json='http://127.0.0.1:7001/api/qingfeng/user'
# # d={
# #     "username":"qingfeng",
# #     "phone":123455667
# # } #字典
# #
# # h={
# #     "content-type":"application/json"
# # } #字典
# #
# # #字典转化json
# # d=json.dumps(d)
# # res=requests.request(method='post',url=url_json,data=d,headers=h) #res响应体
# # print('请求头信息headers',res.request.headers)
# # print('请求的参数res.request.body',res.request.body)
# #
# # print(res.status_code)
# # print('响应头信息headers',res.headers)
# #
# # print(res.json())
# #
# #
#
# '''接口自动化测试：导入requests库
# requests.request
# requests.get
# 底层调用的都是同一个请求
# '''
#
# import requests, json
#
# '''接口1：论坛项目 获取主题首页'''
#
# # 1.requests模块里面的request方法，发起http请求，2.接收http响应
# # requests.request('请求方法','接口地址')
# # res1=requests.request('get',
# #                 'http://1.13.5.210:3000/api/v1/topics')
#
# '''get类参数1.直接拼接在url
#            2.通过params传参'''
# # p={
# #     "limit":1,
# #     "tab":"share"
# # } #参数定义成一个字典
# #
# # # def test(**kwargs):
# # #     print(kwargs)
# # #
# # # test(params=p,test=1)
# # res1=requests.request('get',
# #                  'http://1.13.5.210:3000/api/v1/topics',params=p)
# # res2=requests.request(url='http://1.13.5.210:3000/api/v1/topics',method='get',)
#
# # res3=requests.get('http://1.13.5.210:3000/api/v1/topics')
#
# # 3.响应体res1（状态码，响应值，响应头信息）
# # print('状态码',res1.status_code) #状态码
# # print('响应值',type(res1.text),res1.text,)         #响应值,text方法获得的是字符串
# # print('响应值',type(res1.content),res1.content)    #响应值，bytes字节类型
# # print('响应值',type(res1.json()),res1.json())      #响应值，获取的是字典类型
#
# # respone=res1.json() #响应值respone,字典类型
# # print(respone)  #打印字典类型的响应值
# # print(json.dumps(respone,indent=4,ensure_ascii=False)) #等于把显示在一行的字典，放bejson格式化校验
# # respone=res1.json() #响应值respone,字典类型
# # print('转化之前',type(respone))
# # respone=json.dumps(respone) #把respone字典转化为json字符串
# # print('转化之后',type(respone))
#
# # respone=json.loads(respone) #把json字符串转化为字典
# # print('转化之后',type(respone))
#
#
# '''python字典和 json字符串直接的相互转化'''
#
# # print('响应头信息',res1.headers)     #响应头信息：接口返回给前端的头信息（返回的数据类型）
#
# # print(res2)
#
#
# '''接口2：获取用户信息'''
#
# # h={"token":"qingfengtest"} #定义的一个请求头，字典类型
# # p={"limit":1}#定义的参数，字典类型
# # res=requests.request(method='get',
# #                      url='http://127.0.0.1:7001/api/qingfeng/users',
# #                      params=p,
# #                      headers=h)
# #
# # print(res.status_code)
# # print(res.json())
#
#
# '''接口3:12306'''
# h = {
#     "Cookie": "_uab_collina=163171289127393441288275; JSESSIONID=A480B7E51DB427E671A9EAB429E0BF57; _jc_save_wfdc_flag=dc; _jc_save_fromStation=%u4E0A%u6D77%2CSHH; _jc_save_toStation=%u957F%u6C99%2CCSQ; BIGipServerotn=1173357066.50210.0000; BIGipServerpool_passport=233046538.50215.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; RAIL_EXPIRATION=1643100119736; RAIL_DEVICEID=sNfoLXTkSZyQ1Tk8feRzN3lS3MxlI5FBh2gCXgv5KRsU_DY4muckz0RS4M3FSq0NQVgclu6vPWcf_iS5q99UOyf58Px-VxHptormzrtjDPtelGTqyEtNunOscPbFFI6Zgs2IqJsx_X3JEaQ-z7RfDQ-T78O2LGDb; route=6f50b51faa11b987e576cdb301e545c4; _jc_save_toDate=2022-01-22; _jc_save_fromDate=2022-01-25"
# }
#
# res = requests.get(url='https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date=2022-01-25&leftTicketDTO.'
#                        'from_station=SHH&leftTicketDTO.to_station=CSQ&purpose_codes=ADULT',
#                    headers=h)
#
# # print(res.text)
# # print(res.content)
# print(res.json())
#
# '''reeuqes进行post 类型的请求
# post：
#     请求数据类型为form表单，或者text文件，通过data传参
#     请求数据类型为json类型，通过json传参
# request.body请求参数
# '''
# import json
# import requests
#
# d = {
#     "userid": 1,
# }  # 参数定义成一个字典
#
# url_form_data = 'http://127.0.0.1:7001/api/qingfeng/formdata'
# res = requests.request(method='post', url=url_form_data, data=d)
# print('res.request.body', res.request.body)
#
# print(res.status_code)
# print(res.json())
#
# '''第二个接口'''
# # url_text='http://127.0.0.1:7001/api/qingfeng/text'
# # d='qingfengtest'
# #
# # res=requests.request(method='post',url=url_text,data=d)
# # print('res.request.body',res.request.body)
# #
# # print(res.status_code)
# # print(res.json())
#
#
# '''第三个接口'''
# # url_json='http://127.0.0.1:7001/api/qingfeng/user'
# #
# # d={
# #     "username":"qingfeng",
# #     "phone":123455667
# # } #字典
# # res=requests.request(method='post',url=url_json,json=d)
# # print('res.request.body',res.request.body)
# # print(res.status_code)
# # print(res.json())
#
# #
# # '''第四个接口:json'''
# # url_json='http://127.0.0.1:7001/api/qingfeng/user'
# # d={
# #     "username":"qingfeng",
# #     "phone":123455667
# # } #字典
# #
# # h={
# #     "content-type":"application/json"
# # } #字典
# #
# # #字典转化json
# # d=json.dumps(d)
# # res=requests.request(method='post',url=url_json,data=d,headers=h) #res响应体
# # print('请求头信息headers',res.request.headers)
# # print('请求的参数res.request.body',res.request.body)
# #
# # print(res.status_code)
# # print('响应头信息headers',res.headers)
# #
# # print(res.json())
# #
# #
#
# '''文件上传:参数 files
# 格式：f=[(key,value)]
# '''
# # url_file='http://127.0.0.1:7001/api/qingfeng/upload'
# # f=[
# #     #key        value
# #     ('myfile',open(r'C:\Users\admin\Desktop\11111.png','rb')), #整体，代表上传一张图片
# #     #('myfile', open(r'C:\Users\admin\Desktop\QQ截图20211108133957.png', 'rb')),
# #
# # ]
# # res=requests.request(method='post',url=url_file,files=f)
# # print(res.status_code)
# # print(res.json())
#
#
# '''第二个接口：auth认证'''
# # url_auth = 'http://127.0.0.1:7001/api/qingfeng/auth'
# # d = {
# #     "id": 123456789
# # }
# # user,pwd='admin','123456'  #把用户名和密码转化成YWRtaW46MTIzNDU2
# # users=base64.b64encode(bytes(user,encoding='utf-8')+b":"+
# #                        bytes(pwd,encoding='utf-8')).decode('ascii')
# # print(users)
# # h={
# #     #YWRtaW4xMTExOjEyMzQ1NjIy
# #     "Authorization":"Basic {}".format(users)
# #     #"Authorization": "#Bearer tyuyiuiuuuoiuooif"
# #
# # }#请求头
# #
# #
# # res=requests.request(method='post',url=url_auth,json=d,headers=h)
# # print(res.status_code)
# # print(res.json())
#
#
# '''session:跨请求保持某些参数'''
# # h = {
# #     "Token": "qingfengtest",
# #     # "Authorization":"Basic {}".format(users)
# # }
#
# # url_users = 'http://127.0.0.1:7001/api/qingfeng/users'
# # url_one = 'http://127.0.0.1:7001/api/qingfeng/user/1'
#
# '''通过requests模块里面的request方法，俩次请求完全独立'''
# # res1=requests.request(method='get',url=url_users,headers=h)
# # print(res1.status_code)
# # print(res1.json())
# #
# # res2=requests.request(method='get',url=url_one,headers=h)
# # print(res2.status_code)
# # print(res2.json())
#
# '''通过session会话'''
# s = requests.Session()  # 定义一个session对象 s
# s.headers.update(
#     h
# )  # 会话统一设置headers,update并不是把现有的header的替换掉，而是去新增字段。如果字段以存在，就替换
# s.headers.update({"cookie": "cookietest"})
# s.auth = ('admin', '123456')
# s
# res1 = s.request(method='get', url=url_users, )
# res2 = s.request(method='get', url=url_one, )
# res3 = s.request(method='post', url=url_auth, json=d)
#
# print(res1.request.headers)
# print(res2.request.headers)
# print(res3.request.headers)
# # print(res1.status_code)
# # print(res1.json())
# # print(res2.status_code)
# # print(res2.json())
# print(res3.status_code)
# print(res3.json())
#
# '''接口1：论坛项目 获取主题首页'''
#
# # 1.requests模块里面的request方法，发起http请求，2.接收http响应
# # requests.request('请求方法','接口地址')
# # res1=requests.request('get',
# #                 'http://1.13.5.210:3000/api/v1/topics')
#
# '''get类参数1.直接拼接在url
#            2.通过params传参'''
# # p={
# #     "limit":1,
# #     "tab":"share"
# # } #参数定义成一个字典
# #
# # # def test(**kwargs):
# # #     print(kwargs)
# # #
# # # test(params=p,test=1)
# # res1=requests.request('get',
# #                  'http://1.13.5.210:3000/api/v1/topics',params=p)
# # res2=requests.request(url='http://1.13.5.210:3000/api/v1/topics',method='get',)
#
# # res3=requests.get('http://1.13.5.210:3000/api/v1/topics')
#
# # 3.响应体res1（状态码，响应值，响应头信息）
# # print('状态码',res1.status_code) #状态码
# # print('响应值',type(res1.text),res1.text,)         #响应值,text方法获得的是字符串
# # print('响应值',type(res1.content),res1.content)    #响应值，bytes字节类型
# # print('响应值',type(res1.json()),res1.json())      #响应值，获取的是字典类型
#
# # respone=res1.json() #响应值respone,字典类型
# # print(respone)  #打印字典类型的响应值
# # print(json.dumps(respone,indent=4,ensure_ascii=False)) #等于把显示在一行的字典，放bejson格式化校验
# # respone=res1.json() #响应值respone,字典类型
# # print('转化之前',type(respone))
# # respone=json.dumps(respone) #把respone字典转化为json字符串
# # print('转化之后',type(respone))
#
# # respone=json.loads(respone) #把json字符串转化为字典
# # print('转化之后',type(respone))
#
#
# '''python字典和 json字符串直接的相互转化'''
#
# # print('响应头信息',res1.headers)     #响应头信息：接口返回给前端的头信息（返回的数据类型）
#
# # print(res2)
#
#
# '''接口2：获取用户信息'''
#
# # h={"token":"qingfengtest"} #定义的一个请求头，字典类型
# # p={"limit":1}#定义的参数，字典类型
# # res=requests.request(method='get',
# #                      url='http://127.0.0.1:7001/api/qingfeng/users',
# #                      params=p,
# #                      headers=h)
# #
# # print(res.status_code)
# # print(res.json())
#
#
# '''接口3:12306'''
# h = {
#     "Cookie": "_uab_collina=163171289127393441288275; JSESSIONID=A480B7E51DB427E671A9EAB429E0BF57; _jc_save_wfdc_flag=dc; _jc_save_fromStation=%u4E0A%u6D77%2CSHH; _jc_save_toStation=%u957F%u6C99%2CCSQ; BIGipServerotn=1173357066.50210.0000; BIGipServerpool_passport=233046538.50215.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; RAIL_EXPIRATION=1643100119736; RAIL_DEVICEID=sNfoLXTkSZyQ1Tk8feRzN3lS3MxlI5FBh2gCXgv5KRsU_DY4muckz0RS4M3FSq0NQVgclu6vPWcf_iS5q99UOyf58Px-VxHptormzrtjDPtelGTqyEtNunOscPbFFI6Zgs2IqJsx_X3JEaQ-z7RfDQ-T78O2LGDb; route=6f50b51faa11b987e576cdb301e545c4; _jc_save_toDate=2022-01-22; _jc_save_fromDate=2022-01-25"
# }
#
# res = requests.get(url='https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date=2022-01-25&leftTicketDTO.'
#                        'from_station=SHH&leftTicketDTO.to_station=CSQ&purpose_codes=ADULT',
#                    headers=h)
#
# # print(res.text)
# # print(res.content)
# print(res.json())


if __name__ == '__main__':
    t = HttpRequest()
    t.request_get()
