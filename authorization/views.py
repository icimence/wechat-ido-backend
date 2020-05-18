# -*- encoding=utf-8 -*-


import json

from django.http import JsonResponse, HttpResponse
from django.views import View
from utils.response import wrap_json_response, ReturnCode, CommonResponseMixin
from utils.auth import already_authorized, c2s

from .models import User
from utils.wx.code2session import code2session
from django.contrib.sessions.models import Session


def test_session(request):
    request.session['message'] = 'Test Django Session OK!'
    response = wrap_json_response(code=ReturnCode.SUCCESS)
    request.session.save()
    return JsonResponse(data=response, safe=False)


class UserView(View, CommonResponseMixin):
    def get(self, request):
        print('我来看看cookie信息')
        print(request.COOKIES)
        openid = request.GET['openid']
        if not already_authorized(openid):
            response = self.wrap_json_response(code=ReturnCode.SUCCESS)
            return JsonResponse(data=response, safe=False)
        # open_id = request.session.get('open_id')
        user = User.objects.get(open_id=openid)
        data = {}
        data['major'] = json.loads(user.major)
        data['mission'] = json.loads(user.mission)
        data['type'] = json.loads(user.type)
        data['collection'] = json.loads(user.collection)
        response = self.wrap_json_response(data=data, code=ReturnCode.SUCCESS)
        print(response)
        return JsonResponse(data=response, safe=False)
        pass

    def post(self, request):
        received_body = request.body.decode('utf-8')
        received_body = eval(received_body)
        openid = received_body.get('openid')
        if not already_authorized(openid):
            response = self.wrap_json_response(code=ReturnCode.SUCCESS)
            return JsonResponse(data=response, safe=False)
        # open_id = request.session.get('open_id')
        user = User.objects.get(open_id=openid)
        majors = received_body.get('major')
        missions = received_body.get('mission')
        types = received_body.get('type')
        collections = received_body.get('collection')
        user.major = json.dumps(majors)
        user.mission = json.dumps(missions)
        user.type = json.dumps(types)
        user.collection = json.dumps(collections)
        user.save()
        response = self.wrap_json_response(data=user.major, code=ReturnCode.SUCCESS, message='modify user info success')
        return JsonResponse(data=response, safe=False)
        pass


def __authorize_by_code(request):
    '''
    使用wx.login的到的临时code到微信提供的code2session接口授权
    '''
    post_data = request.body.decode('utf-8')
    post_data = json.loads(post_data)
    code = post_data.get('code').strip()
    app_id = post_data.get('appId').strip()
    nickname = post_data.get('nickname').strip()

    response = {}
    if not code or not app_id:
        response['message'] = 'authorized failed, need entire authorization data.'
        response['code '] = ReturnCode.BROKEN_AUTHORIZED_DATA
        return JsonResponse(data=response, safe=False)

    data = c2s(app_id, code)
    openid = data.get('openid')
    print('get openid: ', openid)
    print('get nickname: ', nickname)
    if not openid:
        response = wrap_json_response(code=ReturnCode.FAILED, message='auth failed')
        return JsonResponse(data=response, safe=False)

    request.session['open_id'] = openid
    request.session['is_authorized'] = True

    if not User.objects.filter(open_id=openid):
        new_user = User(open_id=openid, nickname=nickname)
        print('new user: open_id: %s, nickname: %s' % (openid, nickname) )
        new_user.save()

    response = wrap_json_response(data=openid, code=ReturnCode.SUCCESS, message='auth success.')
    return JsonResponse(data=response, safe=False)
    pass


def authorize(request):
    return __authorize_by_code(request)


def get_status(request):
    print('call get_status function...')
    if already_authorized(request):
        data = {"is_authorized": 1}
    else:
        data = {"is_authorized": 0}
    response = CommonResponseMixin.wrap_json_response(data=data, code=ReturnCode.SUCCESS)
    return JsonResponse(response, safe=False)
