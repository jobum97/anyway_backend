#views.py
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Account
from .serializer import AccountSerializer
from rest_framework.parsers import JSONParser
# Create your views here.


# 회원들 전체 조회, 신규 회원 생성하는 역활
@csrf_exempt
def account_list(request):
    # 요청이 GET 이면 전체 조회
    if request.method == 'GET':
        query_set = Account.objects.all() # 모든 객체 다 읽어옴
        serializer = AccountSerializer(query_set, many=True) # serializer 로 json 형태로 반환
        return JsonResponse(serializer.data, safe=False) # JsonResponse 리턴해줌
    # 요청이 POST 이면 신규 생성 역활
    elif request.method == 'POST':
        data = JSONParser().parse(request) # json 파서를 통해 request 에서 만들어야 하는 객체 데이터를 파싱
        serializer = AccountSerializer(data=data) # 파싱한 데이터를 serializer 에 넣음
        # => serializer 가 올바르면 객체 만듬
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400) # 틀리면 에러 리턴

# 단건 조회 수정 삭제 기능
@csrf_exempt
def account(request, pk):

    obj = Account.objects.get(pk=pk) # pk 를 통해 찾는 객체 불러옴
    # GET 이면 조회
    if request.method == 'GET':
        serializer = AccountSerializer(obj)
        return JsonResponse(serializer.data, safe=False)
    # PUT 이면 수정
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AccountSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    # DELETE 이면 삭제
    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)


# 로그인 단건 조회처럼 객체 불러오지만 id 로 찾을 것
@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_userid = data['userid']
        obj = Account.objects.get(userid=search_userid)

        if data['userpw'] == obj.userpw:
            return HttpResponse(status=200) # 맞으면 성공
        else:
            return HttpResponse(status=400) # 틀리면 실패


