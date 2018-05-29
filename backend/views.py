from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render

from backend.funcs.data_funcs import *
from backend.funcs.user_funcs import *


def index(request):
    data = get_data_from_req(request)
    return HttpResponse(data)


# 记录的数据接口，总是返回json
def data(request):
    data = load_all_data()
    if not is_login(request):
        return HttpResponseRedirect('/auth/')
    result = parse_cmd(request)
    return HttpResponse(result, content_type="application/json")



# 用户登录管理接口
def auth(request):
    if request.method == 'POST':
        if check_login(request) == 0:
            return HttpResponse('<script>alert("密码错误");history.go(-1);</script>')
    elif request.GET.get('logout', '0') == '1':
        logout(request)

    if is_login(request):
        return render(request, 'index.html')
    else:
        return render(request, 'login.html')