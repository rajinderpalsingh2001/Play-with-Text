from django.shortcuts import *
from django.http import *
# from django.views.decorators.csrf import *

def index(request):
    return render(request,'index.html')

# @csrf_exempt
def numberofwords(request):
    word=request.GET["main"]
    count=0
    for i in word:
        if(i==' '):
            count+=1
    count+=1
    return HttpResponse(count)