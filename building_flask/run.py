# coding=utf-8
import base64
import os
import time

from flask import Flask, jsonify
from flask import request
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'xls', 'JPG', 'PNG', 'xlsx', 'gif', 'GIF', 'xmind'])

app.config['JSON_AS_ASCII'] = False
users = [
    {'name': '张三', 'phone': '15908767383', 'id': 1, 'gender': 'boy'},
    {'name': '李四', 'phone': '15908767383', 'id': 2, 'gender': 'girl'},
    {'name': '王五', 'phone': '15908767383', 'id': 3, 'gender': 'boy'},
    {'name': '老六', 'phone': '15908767383', 'id': 4, 'gender': 'girl'},
    {'name': '老七', 'phone': '15908767383', 'id': 5, 'gender': 'girl'}]


# 用于判断文件后缀
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


'''文件上传接口'''


@app.route('/api/qingfeng/upload', methods=['POST'], strict_slashes=False)
def api_upload():
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['myfile']  # 从表单的file字段获取文件，myfile为该表单的name值
    print(request.headers)
    if f and allowed_file(f.filename):  # 判断是否是允许上传的文件类型
        fname = secure_filename(f.filename)
        print('这是什么类型%s' % fname)
        ext = fname.rsplit('.', 1)[1]  # 获取文件后缀
        unix_time = int(time.time())
        new_filename = str(unix_time) + '.' + ext  # 修改了上传的文件名
        f.save(os.path.join(file_dir, new_filename))  # 保存文件到upload目录

        return jsonify({"errno": "000", "success": "true", })
    else:
        return jsonify({"errno": "1001", "errmsg": "false"})


'''登录接口'''


@app.route('/api/qingfeng/login', methods=['POST'], strict_slashes=False)
def api_login():
    data = request.get_json()
    # print(data)
    # print('<Request> url= {url}, body= {body}'.format(url=request.url, body=json.dumps(data, ensure_ascii=False)))
    if data["username"] == "admin" and data["password"] == '123456':
        # return jsonify({"code": '000', "msg": "登录成功", "token":'werdzfgfdgdg',"info":{"name":"admin","age":"18"},"logintime":""})
        return jsonify({
            "httpstatus": 200,
            "adress": {
                "city": "changsha"
            },
            "info": {
                "name": "admin",
                "age": 18
            },
            "msg": "success",
            "token": "qingfengtest"
        })
    else:
        return jsonify({"code": '001', "msg": "用户名或密码错误", })


'''新增用户'''


@app.route('/api/qingfeng/user', methods=['POST'], strict_slashes=False)
def addUser():
    '''
    用户名和密码：username,pwd
    :return:
    '''
    d = request.get_json()  # 获取用户的入参，字典，
    if 'username' not in d or 'phone' not in d:
        return jsonify({'code': 404, 'msg': "参数错误"})

    username = d['username']
    phone = d['phone']
    # 用户表插入一条数据
    users.append({'name': username, 'phone': phone, 'id': len(users) + 1, 'gender': "girl"})
    return jsonify({'code': 200, 'msg': "新增用户{}成功".format(username)})


'''获取单个用户的信息'''


@app.route('/api/qingfeng/user/<int:id>', methods=['GET'], strict_slashes=False)
def getone(id):
    '''假设id=1'''
    # for user in users:
    #     #{'name': '张三', 'phone': '15908767383', 'id': 1},
    #     if user['id']==id:
    #         return jsonify({"code":200,"data":user})
    # else:
    #     return jsonify({"code":401,"message":'数据不存在'})
    result = [user for user in users if user["id"] == id]
    if len(result) == 0:
        return jsonify({'code': 404})
    return jsonify({'code': 200, 'data': result[0]})


'''获取所有用户的信息'''


@app.route('/api/qingfeng/users', methods=['GET'], strict_slashes=False)
def getallUsers():
    '''json的数据'''
    '''
    参数1：limit,代表返回数据限制，比如 limit=3,只返回三条数据，
    参数2：tab,代表返回数据的类型，比如tab=girl,只返回性别为女的数据
    参数1+参数2： limit=2&tab=girl  ，又限制性别，又限制了数据的条数
    '''
    args = request.args
    token = request.headers.get('Token')
    if token == 'qingfengtest':
        if 'limit' in args and 'tab' in args:
            limit = args.get('limit')
            tab = args.get('tab')
            b = [data for data in users if data['gender'] == tab]
            a = b[:int(limit)]
            return jsonify({'code': 200, 'data': a})

        elif 'limit' in args:
            limit = args.get('limit')
            a = users[:int(limit)]
            return jsonify({'code': 200, 'data': a})
        elif 'tab' in args:
            tab = args.get('tab')
            b = [data for data in users if data['gender'] == tab]
            return jsonify({'code': 200, 'data': b})
        else:
            return jsonify({'code': 200, 'data': users})
    else:
        return jsonify({"code": '001', "msg": "用户未登录无权限访问", })


'''编辑用户'''


@app.route('/api/qingfeng/user', methods=['PUT'], strict_slashes=False)
def editUser():
    ''''''
    d = request.get_json()  # 获取用户的入参，字典，
    id = d['id']
    username = d['username']
    result = [user for user in users if user["id"] == id]
    if len(result) == 0:
        return jsonify({'code': 404, "msg": "没有此id"})
    else:
        result[0]['name'] = username
        index = users.index(result[0])
        users[index] = result[0]
        return jsonify({'code': 200, 'data': result[0]})


'''删除用户'''


@app.route('/api/qingfeng/user/<int:id>', methods=['DELETE'], strict_slashes=False)
def deleteUser(id):
    ''''''
    result = [user for user in users if user["id"] == id]
    if len(result) == 0:
        return jsonify({'code': 404, "msg": "没有此id"})
    else:
        users.remove(result[0])
        return jsonify({'code': 200, 'data': users})


# @app.route('/api/qingfeng/userList', methods=['GET'], strict_slashes=False)
# def api_user():
#         token = request.headers.get('Token')
#         if token=='qingfengtest':
#             return jsonify({"code": '000', "data": [{"name":"admin"},{"city":"changsha"}] })
#         else:
#             return jsonify({"code": '001', "msg": "用户未登录无权限访问", })


# @app.route('/api/qingfeng/userViplist', methods=['GET'], strict_slashes=False)
# def api_vipuser():
#         token = request.headers.get('Token')
#         if token=='qingfengtest':
#             return jsonify({"code": '000', "data": users })
#         else:
#             return jsonify({"code": '001', "msg": "用户未登录无权限访问", })


'''form表单接口用于测试'''


@app.route('/api/qingfeng/formdata', methods=['POST'], strict_slashes=False)
def api_userinfo():
    res = request.form.get('userid')
    if res:
        return jsonify({"code": '000', "data": [{"name": "admin"}, {"userid": "001"}]})


'''text接口用于测试'''


@app.route('/api/qingfeng/text', methods=['POST'], strict_slashes=False)
def api_text():
    res = request.get_data()
    res = str(res)
    if res:
        return jsonify({"code": '000', "data": res})


@app.route('/api/qingfeng/demo', methods=['GET'], strict_slashes=False)
def api_demo():
    data = request.args.get('limit')
    response = {"httpstatus": 200,
                "data": [{"from": "yinuo", "name": "hello,qingfeng"}, {"from": "yinuo", "name": "hello,muzi"},
                         {"from": "yinuo", "name": "hello,nuonuo"}]}
    if data == '1':
        return jsonify({"httpstatus": 200, "data": [{"from": "yinuo", "name": "hello,qingfeng"}]})

    elif data == '2':
        return jsonify({"httpstatus": 200,
                        "data": [{"from": "yinuo", "name": "hello,qingfeng"}, {"from": "yinuo", "name": "hello,muzi"}]})
    else:
        return jsonify(response)


'''Base Auth认证  ["Basic","YWRtaW46YWRtaW4xMjM="] '''


@app.route('/api/qingfeng/auth', methods=['POST'])
def post_auth():
    if request.method == 'POST':
        auth = request.headers.get("Authorization")
        if auth is None:
            return jsonify({"code": 10101, "message": "Authorization None"})
        else:
            auth = auth.split()
            auth_parts = base64.b64decode(auth[1]).decode('utf-8').partition(':')
            userid, password = auth_parts[0], auth_parts[2]
            if userid == "" or password == "":
                return jsonify({"code": 10102, "message": "Authorization null"})

            if userid == "admin" and password == "123456":
                data = request.get_json()
                if data['id']:
                    return jsonify({"code": 10200, "message": "Authorization success!", "id": data['id']})
                else:
                    return jsonify({"code": 10200, "message": "入参错误"})

            else:
                return jsonify({"code": 10103, "message": "Authorization fail!"})
    else:
        return jsonify({"code": 10101, "message": "request method error"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7001, debug=True)
