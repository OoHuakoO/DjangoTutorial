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
    return HttpRespones(f'{prev}&nbsp;&nbsp;&nbsp;{next}')