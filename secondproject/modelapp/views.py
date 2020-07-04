from django.shortcuts import render
import random

# Create your views here.

lotto_list = list(range(1,46))

def index(request):
    context = dict()
    if request.GET.get("lotto"):
        result = random.sample(lotto_list,6)
        context['result'] = sorted(result)
    return render(request,'index.html',context)