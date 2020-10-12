from django.http import HttpResponse
def index(request):
    return HttpResponse(f'welcome:')
def search(request,keyword,page):
    return HttpResponse(f'Search for:{keyword} page:{page}')
def redirect(request,url):
    return HttpResponse(f'<a href="{url}" > \
                        Click here to redirect</a>')
def date(request,day,month,year):
    return HttpResponse(f'Date:{day}-{month}-{year}')
def show_acticle(request,id,title):
    return HttpResponse(f'ID:{id} <br> Title: {title}')