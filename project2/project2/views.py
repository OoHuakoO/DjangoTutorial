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
    type = request.GET.get('type','hybrid') # สามารถกำหนดค่า defaultได้เมื่อค่า parameterใน urlไม่ได้ใส่
    lat = request.GET.get('lat','13.7455') # สามารถกำหนดค่า defaultได้เมื่อค่า parameterใน urlไม่ได้ใส่
    lon = request.GET.get('lon','100.4930241') # สามารถกำหนดค่า defaultได้เมื่อค่า parameterใน urlไม่ได้ใส่
    zoom = request.GET.get('zoom',11) # สามารถกำหนดค่า defaultได้เมื่อค่า parameterใน urlไม่ได้ใส่
    zoom = int(zoom) # สามารถ convert string เป็น Int ได้ เพื่อนำไปคำนวน
    return HttpResponse(f'May type:{type} <br> \
                        Location:{lat},{lon} <br> \
                        Zoom:{zoom + 1}')