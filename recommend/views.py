import recommend.searchBook as searchBook
import recommend.searchComp as searchComp
from django.http import JsonResponse
from django.http import HttpResponse


def getRecommendBook(request):
    res = request.GET['Tag']
    return_list = searchBook.getResqutes(res)
    # result = "["
    # for i in range(len(return_list) - 1):
    #     result += str(return_list[i])
    #     result += ","
    # result += str(return_list[-1])
    # result += "]"
    return JsonResponse(return_list)


def getRecommendComp(request):
    return_list = searchComp.getComp()
    # result = "["
    # for i in range(len(return_list) - 1):
    #     result += str(return_list[i])
    #     result += ","
    # result += str(return_list[-1])
    # result += "]"
    return JsonResponse(return_list)
