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

def test(request): # ฟังกชันสำหรับการส่งตัวแปรไปยัง template
    dt = date.today()
    data = {
         'title':'Django framework',
         'message':'Hello word',
        'color' : ['red','green','blue'],
        'flowers' : {'a':'rose','b':'jasmine','c':'orchid'},
        'date': dt
    }
    return render(request,'test.html',data)
