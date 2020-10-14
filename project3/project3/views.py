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

    