from django.shortcuts import render

# Create your views here.
def index(request) :
    context = dict()
    
    if request.GET.get('myword'):
        myword = request.GET.get('myword')
        context['myword'] = myword
        context['display_len'] = len(myword.replace(" ",""))

        word_list = myword.split(" ")
        checkcnt = dict()
    
        print("********",word_list)
    
        count_dict = {}
    
        for i in word_list:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1
            
        myword_len = len(myword)
    
        context['display_cnt'] = count_dict
    
    # print(request.GET.get('inputword'))
    # word_len = len(request.GET.get('inputword'))
    # context['display_len'] = word_len
        return render(request,'index.html',context)
    return render(request,'index.html',context)