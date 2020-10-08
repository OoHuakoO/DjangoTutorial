from django.http import HttpResponse
def index(request,count):
    return HttpResponse(f'welcome:{count}')
def search(request,keyword,page):
    return HttpResponse(f'Search for:{keyword} page:{page}')
def show_acticle(request,id,title):
    return HttpResponse(f'ID:{id} <br> Title: {title}')
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
    return HttpRespones(f'{prev}&nbsp;&nbsp;&nbsp;{next}')