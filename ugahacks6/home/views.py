from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import helper


# Create your views here.
@csrf_exempt
def home(request):
    return render(request, '../templates/home.html')


@csrf_exempt
def search(request):
    # query = request.POST['query']
    # data = helper.search_result(query)
    # return JsonResponse(data)
    pass
