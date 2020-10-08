from django.http import HttpResponse
def index(request,count):
    return HttpResponse(f'welcome:{count}')
def search(request,keyword,page):
    return HttpResponse(f'Search for:{keyword} page:{page}')
def show_acticle(request,id,title):
    return HttpResponse(f'ID:{id} <br> Title: {title}')
def drink(request,dnk):
    return HttpResponse(f'Drink: {dnk}')