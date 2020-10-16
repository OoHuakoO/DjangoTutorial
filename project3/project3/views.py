from django.http import HttpResponse
from django.shortcuts import render
from datetime import date
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def detail(request):
    return render(request,'product/detail.html')
def order(request):
    return render(request,'product/order.html')

def variable(request): # ฟังกชันสำหรับการส่งตัวแปรไปยัง template
    dt = date.today()
    data = {
         'title':'Django framework',
         'message':'Hello word',
        'color' : ['red','green','blue'],
        'flowers' : {'a':'rose','b':'jasmine','c':'orchid'},
        'date': dt
    }
    return render(request,'variable.html',data)

def tag_if(request):
    vars = {
        'home_goals': 3, 
        'guest_goals': 2,
    }
    return render(request, 'tag-if.html', vars)
    
def tag_for(request):
    vars = {
        'range': range(1, 6),
        'list': ['red', 'green', 'blue', 'yellow'],
        'dict': {'a':'ant', 'b':'boy', 'c':'cat', 'd':'dog'}
    }
    return render(request, 'tag-for.html', vars)

def tag_other(request):
    return render(request, 'tag-other.html', {'list':[1, 3, 5, 7]})
    

def tag_auto_escape(request):
    data = {
        'html_str': '<b>\'Tom\' & "Jerry"</b>',
    }
    return render(request, 'tag-auto-escape.html', data)
    
def filter_str_list_num(request):
    data = {
        'var_str': 'Hello World',
        'var_list': ['One', 'Two', 'Three'],
        'var_int': 2475,
        'var_float': 3.14,
        'var_none': None
    }
    return render(request, 'filter-str-list-num.html', data)    