from django.http import HttpResponse
def index(request,count):
    return HttpResponse(f'welcome:{count}')
def about(request):
    return HttpResponse("kuy")
