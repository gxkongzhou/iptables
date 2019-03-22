# -*- coding:utf-8 -*-

"""
Created in 20190129 by zkz
The main application
"""
# version 0.1

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

app = Flask(__name__)
app.secret_key = 'asbetaoiugljweotualkj'

app.config['SERVER_NAME'] = 'mountain.com:5000'


def wrapper(func):
    def inner(*args, **kwargs):
        if not session.get("user_info"):
            return redirect("/login")
        ret = func(*args, **kwargs)
        return ret

    return inner


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("adminlogin.html")
    else:
        # print(request.values) #
        username = request.form.get("username")
        password = request.form.get("password")
        if username == 'vicent' and password == 'hp2548HPL':
            session["user_info"] = username
            # session.pop["user_info"]  # 删除 sesssion
            return redirect("/index")
        else:
            return render_template("adminlogin.html", msg="用户名或密码错误")


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route("/404", endpoint='404')
def nofound():
    render_template("404.html")


@wrapper
def index():
    # if not session.get["user_info"]
    #   return redirect("/index")
    return render_template("index.html")


app.add_url_rule('/index', endpoint='new', view_func=index, methods=['GET', 'POST'])
app.view_functions['index'] = index


# test app.route
@app.route('/test1', endpoint="subd", subdomain="test")
def view1():
    """
    The flask support static subdomain
    This ia avaliable at subdomain.your.domain.tld
    :return:
    """
    v = url_for('subd')
    print v
    return v


@app.route('/sss', endpoint="youtu", subdomain="<vvv>")
def vs(vvv):
    tst = vvv + '.' + app.config['SERVER_NAME']
    # tvt = url_for("youhu")
    # print tvt
    return "your domain name is : {}".format(tst)


with app.test_request_context():
    print url_for('new')
    print url_for("login")
    print url_for("subd")
    # print url_for("youtu")

sl = """业务名称：腾讯微加信用卡
业务负责人：subkeyli(李野)，eattazhong(钟明恒)
服务器IP：10.123.6.24
服务器负责人：odinma(马晓东)
连接外部网络原因：业务中需要调用征信的cgi接口进行人脸识别验证，申请访问外网
申请期限： 3个月，业务开发长期需要。
"""
