from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django_redis import get_redis_connection
from redis import StrictRedis


def index(request):
    """进入首页"""

    # 创建一个StrictRedis对象
    # strict_redis = StrictRedis(host='127.0.0.1', port=6379, db=0)
    # decode_responses: 转换成字符串输出
    # strict_redis = StrictRedis(decode_responses=True)
    # 获取一个StrictRedis对象
    # strict_redis = get_redis_connection('default')
    strict_redis = get_redis_connection()

    # 通过StrictRedis对象操作Redis
    # 增
    strict_redis.set('aa', '111')
    strict_redis.set('bb', '222')

    # 查
    aa = strict_redis.get('aa')
    bb = strict_redis.get('bb')
    text = 'aa=%s, bb=%s' % (aa.decode(), bb)
    return HttpResponse(text)


def set_session(request):
    """"保存session数据"""

    request.session['username'] = 'Django'
    request.session['verify_code'] = '123456'
    return HttpResponse('保存session数据成功')


def get_session(request):
    """获取session数据"""

    username = request.session.get('username')
    verify_code = request.session.get('verify_code')
    text = 'username=%s, verify_code=%s' % (username, verify_code)
    return HttpResponse(text)


def hget_cart(request):
    return None