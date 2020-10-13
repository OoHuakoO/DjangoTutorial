from django.http import HttpResponse
def index(request):
    return HttpResponse(f'welcome:')
def show_title(request,title):
    return HttpResponse(f'Title:{title}')
def drink(request,dnk):
    return HttpResponse(f'Drink: {dnk}')
def find(request,key,page):
    page = int(page)
    prev = ''
    if page > 1:
        prev = f'<a href="/find/{key}/{page-1}">Previous</a>'
    else:
        prev = ''
    next = f'<a href="/find/{key}/{page+1}">Next</a>'
    return HttpResponse(f'{prev} &nbsp;&nbsp;&nbsp; {next}')
def map(request):
    type = request.GET.get('type','default') # สามารถกำหนดค่า defaultได้เมื่อค่า parameterใน urlไม่ได้ใส่
    return HttpResponse(f'May type:{type}')